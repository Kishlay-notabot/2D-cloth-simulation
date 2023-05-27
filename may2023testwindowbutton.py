import pygame

pygame.init()
wid, hei = 800, 700
window = pygame.display.set_mode((wid, hei))

# Function to check if a point is inside a rectangle
def point_in_rect(point, rect):
    x, y = point
    rx, ry, rw, rh = rect
    return rx < x < rx + rw and ry < y < ry + rh

def draw_button(window, button_rect, button_text, text_color, button_color):
    pygame.draw.rect(window, button_color, button_rect)
    font = pygame.font.Font(None, 30)
    text = font.render(button_text, True, text_color)
    text_rect = text.get_rect(center=button_rect.center)
    window.blit(text, text_rect)

def run(window, wid, hei):
    run = True
    clock = pygame.time.Clock()
    fps = 60

    button_rect = pygame.Rect(10, 10, 100, 50)
    button_text = "Run Pymunk"
    text_color = (255, 255, 255)
    button_color = (0, 0, 255)
#######pymunk start code
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
    #INDEPENDENT BODY WITHOUT PREDEFINED
    space = space
    radius = 45
    mybod = pymunk.Body()
    mybod.position = (300, 300)
    shape = pymunk.Circle(mybod, radius)
    shape.mass = 1
    shape.color = (55, 34, 57, 123)
    space.add(mybod, shape)
    shape.elasticity = 0.9
    shape.friction = 0.4
    


    






































    #DO NOT CHANGE BELOW
    j = pymunk.DampedSpring(big_ball.body, joina.body, (0, 0), (0, 0), 5, 70, 0)
    space.add(j)
    space.add(pymunk.DampedSpring(big_ball.body, joinb.body, (0, 0), (0, 0), 100, 100, 10))
    wall(space, wid, hei)
    draw_options = pymunk.pygame_util.DrawOptions(window)

















#pygamecode
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if point_in_rect(mouse_pos, button_rect):
                    # Pymunk code to be executed
                    draw(space, window, draw_options)
                    space.step(dt)
                    pygame.quit()
                    print("Running Pymunk code")

        window.fill("white")
        draw_button(window, button_rect, button_text, text_color, button_color)
        pygame.display.update()
        clock.tick(fps)
        

