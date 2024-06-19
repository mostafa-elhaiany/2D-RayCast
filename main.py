import sys
import pygame 
import config
from Boundary import Boundary
from Ray import Ray

pygame.init()

screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
pygame.display.set_caption("2D Ray Casting")

bounds = [
    Boundary((10,10), (20,40))
]

rays = [
    Ray((config.HEIGHT//2,config.WIDTH//2), 20)
]

def draw():
    # Fill the screen with black color
    screen.fill((0, 0, 0))
    
    for b in bounds:
        b.draw(pygame, screen)

    for r in rays:
        r.draw(pygame,screen)


    # Update the display
    pygame.display.flip()


clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    rays[0].rotate(1)

    draw()

    clock.tick(60)


# Quit Pygame
pygame.quit()
sys.exit()
