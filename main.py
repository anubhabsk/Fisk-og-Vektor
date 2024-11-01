import pygame
import random
from pygame.locals import *
from Library.vector import Vector
from Library.fish import Fish
from Library.flock import Flock
from Library.bluefish import BlueFish
from Library.redfish import RedFish

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

flock = Flock()
for _ in range(0):
    flock.add_fish(BlueFish(Vector(random.randint(0, 800), random.randint(0, 600)), Vector(random.uniform(-1, 1), random.uniform(-1, 1))))
for _ in range(0):
    flock.add_fish(RedFish(Vector(random.randint(0, 800), random.randint(0, 600)), Vector(random.uniform(-1, 1), random.uniform(-1, 1))))

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 128, 255))
    flock.update_and_draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()