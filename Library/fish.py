import pygame
from Library.vector import Vector
from math import degrees
import random

class Fish:
    def __init__(self, position, velocity, image_path):
        self.position = position
        self.velocity = velocity
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (70, 50))
        self.copy = self.image.copy()
        self.maxvelocity = 10
        self.vision_distance = random.randint(30, 70)

    def boundary_bounce(self):
        new_velocity = self.velocity
        if self.position.x < 0 or self.position.x > 800 - 50:
            new_velocity = Vector(-self.velocity.x, self.velocity.y)
        if self.position.y < 0 or self.position.y > 600 - 50:
            new_velocity = Vector(self.velocity.x, -self.velocity.y)
        return new_velocity

    def screenConfinement(self):
        d = self.vision_distance
        if self.position.x < d:
            self.velocity.x += (1 - (self.position.x / d) ** 2)
        if self.position.x > 800 - d:
            self.velocity.x -= (1 - ((800 - self.position.x) / d) ** 2)
        if self.position.y < d:
            self.velocity.y += (1 - (self.position.y / d) ** 2)
        if self.position.y > 600 - d:
            self.velocity.y -= (1 - ((600 - self.position.y) / d) ** 2)

    def update(self):
        self.position += self.velocity
        self.screenConfinement()
        self.image = pygame.transform.rotate(self.copy, -degrees(self.velocity.polar360))

    def draw(self, screen):
        screen.blit(self.image, (self.position.x, self.position.y))
