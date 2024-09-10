import pygame
from Python.vector2 import Vector

class Fish:
    def __init__(self, position, velocity, image_path):
        self.position = position
        self.velocity = velocity
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (70, 50))

    def check_bounds_and_bounce(self):
        # Denne her kode tjekker om fisken rammer kanterne og bounce den, hvis det er nødvendigt
        new_velocity = self.velocity
        if self.position.x < 0 or self.position.x > 800 - 50:
            new_velocity = Vector(-self.velocity.x, self.velocity.y)
        if self.position.y < 0 or self.position.y > 600 - 50:
            new_velocity = Vector(self.velocity.x, -self.velocity.y)
        return new_velocity
    
    def update(self):
        self.position += self.velocity
        # Den her kode opdaterer hastigheden baseret på bounce logikken
        self.velocity = self.check_bounds_and_bounce()
    
    def draw(self, screen):
        screen.blit(self.image, (self.position.x, self.position.y))
