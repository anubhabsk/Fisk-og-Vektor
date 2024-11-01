import pygame
from Library.fish import Fish

class BlueFish(Fish):
    def __init__(self, position, velocity):
        super().__init__(position, velocity, image_path='Library/BlueFish.png')
        self.image = pygame.transform.scale(self.image, (15, 15))
