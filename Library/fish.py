import pygame
from Library.vector2 import Vector
from math import degrees

class Fish:
    def __init__(self, position, velocity, image_path):
        self.position = position
        self.velocity = velocity
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (70, 50))
        self.copy = self.image.copy()

    def boundary_bounce(self):
        new_velocity = self.velocity
        if self.position.x < 0 or self.position.x > 800 - 50:
            new_velocity = Vector(-self.velocity.x, self.velocity.y)
        if self.position.y < 0 or self.position.y > 600 - 50:
            new_velocity = Vector(self.velocity.x, -self.velocity.y)
        return new_velocity
    
    def screenConf(self, d=30):
        if not(d < self.position.x < 800-50):
            self.velocity.x += 1-(self.position.x/(d*10))**2
        if self.position.y < 0 or self.position.y > 600 - 50:
            self.velocity.y += 1-(self.position.y/(d*10))**2

    def update(self):
        self.position += self.velocity
        #self.velocity = self.boundary_bounce()
        self.screenConf()
        self.image = pygame.transform.rotate(self.copy, -degrees(self.velocity.polar360))
    
    def draw(self, screen):
        screen.blit(self.image, (self.position.x, self.position.y))
