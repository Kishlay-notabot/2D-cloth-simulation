"""
Pymunk constraints demo. Showcase of all the constraints included in Pymunk.

Adapted from the Chipmunk Joints demo:
https://github.com/slembcke/Chipmunk2D/blob/master/demo/Joints.c
"""


import pygame

import pymunk
import pymunk.pygame_util
from pymunk.vec2d import Vec2d

pygame.init()
screen = pygame.display.set_mode((1200, 600))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 24)


space = pymunk.Space()
space.gravity = (0.0, 900.0)
draw_options = pymunk.pygame_util.DrawOptions(screen)


box_size = 200
w = screen.get_width()
h = screen.get_height()
for i in range(2):
    sw = pymunk.Segment(space.static_body, (0, i * box_size), (w, i * box_size), 1)
    sw.friction = 1
    sw.elasticity = 1
    sh = pymunk.Segment(
        space.static_body, (i * box_size, 0), (i * box_size, h - box_size), 1
    )
    sh.friction = 1
    sh.elasticity = 1
    space.add(sw, sh)


def add_ball(space, pos, box_offset):
    body = pymunk.Body()
    body.position = Vec2d(*pos) + box_offset
    shape = pymunk.Circle(body, 5)
    shape.mass = 10
    shape.friction = 0.7
    space.add(body, shape)
    return body



box_offset = box_size, 0
b1 = add_ball(space, (50, 60), box_offset)
b2 = add_ball(space, (150, 60), box_offset)
c = pymunk.SlideJoint(b1, b2, (20, 0), (-20, 0), 40, 80)
space.add(c)
b3 =  add_ball(space, (200, 60), box_offset)
b4 =  add_ball(space, (250, 120), box_offset)
d =  pymunk.SlideJoint(b2, b3, (20, 0), (-20, 0), 40, 80)
space.add(d)
e =  pymunk.SlideJoint(b3, b4, (20, 0), (-20, 0), 40, 80)
space.add(e)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            exit()



    screen.fill(pygame.Color("white"))
    space.step(1.0 / 60)

    space.debug_draw(draw_options)
    pygame.display.flip()

    clock.tick(60)
    pygame.display.set_caption(f"fps: {clock.get_fps()}")
