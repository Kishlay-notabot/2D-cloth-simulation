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
    shape.color = (0, 150, 0, 0)
    space.add(body, shape)
    shape.elasticity = 0.9
    shape.friction = 0.4
    return shape

# def add_ball(space):
#     body = pymunk.Body()
#     body.position = (500, 500)
#     shape = pymunk.Circle(body, 20)
#     shape.mass = 1
#     shape.friction = 0.7
#     space.add(body, shape)
#     return body

def create_ball_a(space, radius, mass):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = (500, 300)
    shape = pymunk.Circle(body, radius)
    shape.mass = mass
    shape.color = (55, 0, 0, 100)
    space.add(body, shape)
    shape.elasticity = 0.9
    shape.friction = 0.4
    return shape

def create_ball_b(space, radius, mass):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = (550, 300)
    shape = pymunk.Circle(body, radius)
    shape.mass = mass
    shape.color = (55, 0, 0, 100)
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
    big_ball = create_ball(space, 10, 10)
    joina = create_ball_a(space, 5, 10)
    joinb = create_ball_b(space, 5, 10)
    #DO NOT CHANGE ABOVE



    #May 27 continued test
    #INDEPENDENT BODY WITHOUT PREDEFINED FUNCTION
    space = space
    radius = 45
    mybod = pymunk.Body()
    mybod.position = position
    shape = pymunk.Circle(mybod, radius)
    shape.mass = 12
    shape.color = (55, 34, 57, 123)
    space.add(mybod, shape, position)
    shape.elasticity = 0.9
    shape.friction = 0.4
    space.add(pymunk.DampedSpring(shape.body, joina.body, (0, 0), (0, 0), 65, 90, 0))















    #DO NOT CHANGE BELOW

    # j = pymunk.DampedSpring(big_ball.body, joina.body, (0, 0), (0, 0), 5, 70, 0)
    # space.add(j) 
    # REMOVED THIS UPPER TEST BODY
    space.add(pymunk.DampedSpring(big_ball.body, joinb.body, (0, 0), (0, 0), 100, 100, 10))
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
