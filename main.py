import pygame
import random
from pygame.locals import *
from Python.vector2 import Vector
from Python.fish import Fish
from Python.flock import Flock

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

# Jeg har oprettet en liste af fisk med tilfældige positioner
fish_list = []
for _ in range(15): # Har så valgt at oprette 10 fisk
    random_position = Vector(random.randint(0, 750), random.randint(0, 550)) # Tilfældige x og y inden for skærmen
    velocity = Vector(1, 1) # Alle fisk har samme hastighed i starten med denne kode
    fish = Fish(position=random_position, velocity=velocity, image_path='Python/Fish.png')
    fish_list.append(fish)

flock = Flock(fish_list)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Nu opdater og tegner programmet hver fisk i listen
    screen.fill((0, 128, 255))
    flock.update()
    flock.draw(screen)
    
    pygame.display.flip()
    clock.tick(100)

pygame.quit()
