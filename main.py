import pygame
import random
from pygame.locals import *
from Library.vector import Vector
from Library.fish import Fish
from Library.flock import Flock

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

flock = Flock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 128, 255))
    flock.update()
    flock.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()