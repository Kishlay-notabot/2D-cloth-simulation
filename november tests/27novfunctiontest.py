import pygame
import pymunk
import pymunk.pygame_util
import math

pygame.init()
wid, hei = 800, 700
window = pygame.display.set_mode((wid, hei))


def draw(space, window, draw_options):
    window.fill("white")
    space.debug_draw(draw_options)
    pygame.display.update()

def wall(space, wid, hei):
    rects = [
        [(wid/2, hei - 10), (wid, 20)],
        [(wid/2, 10), (wid, 20)]
    ]
    for pos, size in rects:
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = pos
        shape  = pymunk.Poly.create_box(body, size)
        shape.elasticity = 0.4
        shape.friction = 0.5
        space.add(body, shape)

def create_ball(space, radius, mass):
    body = pymunk.Body()
    body.position = (500, 350)
    shape = pymunk.Circle(body, radius)
    shape.mass = mass
    shape.color = (0, 200, 0, 100)
    space.add(body, shape)
    shape.elasticity = 0.9
    shape.friction = 0.4
    return shape

def add_ball(space):
    body = pymunk.Body()
    body.position = (500, 500)
    shape = pymunk.Circle(body, 20)
    shape.mass = 1
    shape.friction = 0.7
    space.add(body, shape)
    return body

def create_ball_a(xloc, yloc):
    radius = 5
    mass = 10
    space = pymunk.Space()
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = (xloc, yloc)
    shape = pymunk.Circle(body, radius)
    shape.mass = mass
    shape.color = (0, 70, 0, 100)
    space.add(body, shape)
    shape.elasticity = 0.9
    shape.friction = 0.4
    return shape

def create_ball_b(xloc, yloc):
    radius = 20
    mass = 10
    space = pymunk.Space()
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = (xloc, yloc)
    shape = pymunk.Circle(body, radius)
    shape.mass = mass
    shape.color = (0, 0, 0, 100)
    space.add(body, shape)
    shape.elasticity = 0.9
    shape.friction = 0.4
    return shape
# def add_spring(var1, var2):
#     dlx = pymunk.DampedSpring(var1, var2, (0, 0), (0, 0), 5, 70, 0)
#     space.add(dlx)



def run(window, wid, hei):
    run = True
    clock = pygame.time.Clock()
    fps = 60
    dt = 1 / fps
    space = pymunk.Space()
    space.gravity = (0, 981)
    big_ball = create_ball(space, 30, 10)
    joina = create_ball_a(700, 100)
    joinb = create_ball_b(100, 100)
    j = pymunk.DampedSpring(joinb.body, joina.body, (0, 0), (0, 0), 1, 100, 0)
    space.add(j)
    # space.add(pymunk.DampedSpring(big_ball.body, joinb.body, (0, 0), (0, 0), 100, 100, 10))
    wall(space, wid, hei)
    draw_options = pymunk.pygame_util.DrawOptions(window)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        draw(space, window, draw_options)
        space.step(dt)
        clock.tick(fps)
    pygame.quit()

if __name__ == "__main__":
    run(window, wid, hei)
