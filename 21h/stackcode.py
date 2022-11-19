import pygame
import pymunk
import pymunk.pygame_util
import math

# --- constants ---  # PEP8: `UPPER_CASE_NAMES`

WIDTH = 800
HEIGHT = 700
FPS = 60

# --- functions ---  # PEP8: all function before main code

def draw(space, window, draw_options):
    window.fill("white")
    space.debug_draw(draw_options)
    pygame.display.update()

def wall(space, width, height):
    rects = [
        [(width/2, height - 10), (width, 20)],
        [(width/2, 10), (width, 20)]
    ]
    
    for pos, size in rects:
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.ion = pos
        
        shape  = pymunk.Poly.create_box(body, size)
        shape.elasticity = 0.4
        shape.friction = 0.5
        
        space.add(body, shape)

def create_ball(space, radius, mass):
    body = pymunk.Body()
    body.position = (500, 350)
    
    shape = pymunk.Circle(body, radius)
    shape.mass = mass
    shape.color = (55, 0, 0, 100)
    shape.elasticity = 0.9
    shape.friction = 0.4

    space.add(body, shape)
    
    return shape

def add_ball(space):
    body = pymunk.Body()
    body.position = (500, 500)
    
    shape = pymunk.Circle(body, 20)
    shape.mass = 1
    shape.friction = 0.7
    
    space.add(body, shape)
    
    return body

def create_ball_a(space, radius, mass):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = (500, 300)
    
    shape = pymunk.Circle(body, radius)
    shape.mass = mass
    shape.color = (55, 0, 0, 100)
    shape.elasticity = 0.9
    shape.friction = 0.4
    
    space.add(body, shape)
    
    return shape

def create_ball_b(space, radius, mass):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = (550, 300)
    
    shape = pymunk.Circle(body, radius)
    shape.mass = mass
    shape.color = (55, 0, 0, 100)
    shape.elasticity = 0.9
    shape.friction = 0.4

    space.add(body, shape)
    
    return shape


def create_ball_universal(space, radius, mass, positon):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = positon
    shape = pymunk.Circle(body, radius)
    shape.mass = mass
    shape.color = (55, 0, 0, 100)
    space.add(body, shape)
    shape.elasticity = 0.9
    shape.friction = 0.4
    return shape

def add_spring(space, body1, body2):
    dlx = pymunk.DampedSpring(body1, body2, (0, 0), (0, 0), 5, 70, 0)
    
    space.add(dlx)
    
    return dlx

def run(WIDTH, HEIGHT):
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    dt = 1 / FPS
    clock = pygame.time.Clock()
    space = pymunk.Space()
    space.gravity = (0, 981)
    wall(space, WIDTH, HEIGHT)
    draw_options = pymunk.pygame_util.DrawOptions(window)

    # OBJECTS START HERE --------------------------------------
    big_ball = create_ball(space, 30, 10)
    joina = create_ball_a(space, 5, 10)
    joinb = create_ball_b(space, 5, 10)
    
    # FUNCTIONS START HERE --------------------------------------
    add_spring(space, joina.body, big_ball.body)
    add_spring(big_ball.body, joinb.body)
    
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
        draw(space, window, draw_options)
        
        space.step(dt)
        clock.tick(FPS)
        
    pygame.quit()

if __name__ == "__main__":
    run(WIDTH, HEIGHT)