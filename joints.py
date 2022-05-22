import pygame

import pymunk
import pymunk.pygame_util
from pymunk.vec2d import Vec2d
pygame.init()
screen = pygame.display.set_mode((1200, 600))
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = (0.0, 900.0)
draw_options = pymunk.pygame_util.DrawOptions(screen)

def add_ball(space, pos, box_offset):
    body = pymunk.Body()
    body.position = Vec2d(*pos) + box_offset
    shape = pymunk.Circle(body, 20)
    shape.mass = 1
    shape.friction = 0.7
    space.add(body, shape)
    return body






box_offset = 200, 0
b1 = add_ball(space, (50, 60), box_offset)
b2 = add_ball(space, (150, 60), box_offset)
c = pymunk.SlideJoint(b1, b2, (20, 0), (-20, 0), 40, 80)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            exit()
            


space.step(1.0 / 60)
