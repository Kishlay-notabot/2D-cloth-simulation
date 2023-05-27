import pygame
import pymunk
import time

# Initialize Pygame
pygame.init()

# Set window dimensions
wid, hei = 800, 600
window = pygame.display.set_mode((wid, hei))
pygame.display.set_caption("Button Example")

# Set button dimensions and position
button_width, button_height = 100, 50
button_x, button_y = wid // 2 - button_width // 2, hei // 2 - button_height // 2

# Create a button surface
button_surface = pygame.Surface((button_width, button_height))
button_rect = button_surface.get_rect()
button_rect.center = (button_x, button_y)

# Set colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Initialize the button state and success dot state
button_clicked = False
show_success_dot = False
success_dot_color = GREEN
success_dot_position = (10, 10)

def run(window, wid, hei):
    # Clear the screen
    window.fill(WHITE)
    
    # Draw the success dot
    pygame.draw.circle(window, success_dot_color, success_dot_position, 10)

    # Update the display
    pygame.display.update()

    # Wait for 1 second
    time.sleep(1)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the button is clicked
            if button_rect.collidepoint(event.pos):
                button_clicked = True

    # Clear the window
    window.fill(WHITE)

    # Draw the button
    if button_clicked:
        run(window, wid, hei)
        show_success_dot = True

    # Draw the success dot if the button was clicked
    if show_success_dot:
        pygame.draw.circle(window, success_dot_color, success_dot_position, 10)
        show_success_dot = False

    # Draw the button rectangle
    pygame.draw.rect(window, GREEN, button_rect)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()

