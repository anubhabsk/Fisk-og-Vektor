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

# Jeg har oprettet en liste af fisk med tilfældige positioner
fish_list = []
for _ in range(10):
    random_position = Vector(random.randint(0, 750), random.randint(0, 550))
    velocity = Vector(1, 1)
    fish = Fish(position=random_position, velocity=velocity, image_path='Python/Fish.png')
    fish_list.append(fish)

flock = Flock(fish_list)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
    screen.fill((0, 128, 255))
    flock.update()
    flock.draw(screen)
    
    pygame.display.flip()
    clock.tick(100)

pygame.quit()