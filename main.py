import sys
import pygame 
import config
import random
from Boundary import Boundary
from Particle import Particle
pygame.init()

screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))

pygame.display.set_caption("2D Ray Casting")

bounds = [
    Boundary((random.randint(0,config.HEIGHT),random.randint(0,config.WIDTH)), (random.randint(0,config.HEIGHT),random.randint(0,config.WIDTH)))
    for _ in range(5)
]

particles = [
    Particle((config.HEIGHT//2, config.WIDTH//2),5,1000)
]

def draw():
    # Fill the screen with black color
    screen.fill((0, 0, 0))
    
    for b in bounds:
        b.draw(pygame, screen)

    for p in particles:
        p.draw(pygame, screen)
        p.cast(bounds,pygame, screen)
        
    # Update the display
    pygame.display.flip()


def handle_mouse_events(event):
    """
    Checks if the given Pygame event is a mouse button click or a mouse wheel scroll.
    
    Parameters:
    event (pygame.event.Event): The event to check.
    
    Returns:
    bool: True if the event is a mouse button click or a wheel scroll, False otherwise.
    """
    global bounds
    global particles
    # Mouse button click
    if event.button in [1, 2, 3]:  # Left, Middle, Right mouse buttons
        bounds = [
                Boundary((random.randint(0,config.HEIGHT),random.randint(0,config.WIDTH)), 
                         (random.randint(0,config.HEIGHT),random.randint(0,config.WIDTH))
                         ,
                         color = (255,255,255))
                for _ in range(5)
            ]
    # Mouse wheel scroll
    elif event.button ==5 :  # Wheel up (4) or Wheel down (5)
        particles = [
            Particle((config.HEIGHT//2, config.WIDTH//2),particles[0].increments+.05,1000)
        ]
    elif event.button == 4 :  # Wheel up (4) or Wheel down (5)
        particles = [
            Particle((config.HEIGHT//2, config.WIDTH//2),particles[0].increments-.05,1000)
        ]


clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            handle_mouse_events(event)

    mouse_pos = pygame.mouse.get_pos()
    particles[0].set_pos(mouse_pos)

    draw()

    clock.tick(60)


# Quit Pygame
pygame.quit()
sys.exit()
