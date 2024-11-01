import pygame
from Library.fish import Fish

class RedFish(Fish):
    def __init__(self, position, velocity):
        super().__init__(position, velocity, image_path='Library/RedFish.png')
        self.image = pygame.transform.scale(self.image, (20, 20))  # Tilpasset størrelse til RedFish
