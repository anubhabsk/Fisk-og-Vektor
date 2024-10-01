from Library.fish import Fish
from Library.vector import Vector
import random

class Flock:
    def __init__(self):
        self.fish_list = []
        for _ in range(10):
            random_position = Vector(random.randint(0, 750), random.randint(0, 550))
            velocity = Vector(random.randint(-1,1), random.randint(-1,1))
            fish = Fish(position=random_position, velocity=velocity, image_path='Library/Fish.png')
            self.fish_list.append(fish)

    def update(self):
        for fish in self.fish_list:
            fish.update()

    def draw(self, screen):
        for fish in self.fish_list:
            fish.draw(screen)