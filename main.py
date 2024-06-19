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
    Particle((config.HEIGHT//2, config.WIDTH//2),10,1000)
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


clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_pos = pygame.mouse.get_pos()
    particles[0].set_pos(mouse_pos)

    draw()

    clock.tick(60)


# Quit Pygame
pygame.quit()
sys.exit()
