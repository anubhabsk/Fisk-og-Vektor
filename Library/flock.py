import random
from Library.vector import Vector
from Library.fish import Fish
from Library.bluefish import BlueFish
from Library.redfish import RedFish

class Flock:
    def __init__(self):
        self.fish_list = []
        for _ in range(5):
            random_position = Vector(random.randint(0, 750), random.randint(0, 550))
            velocity = Vector(random.uniform(-1, 1), random.uniform(-1, 1))
            fish = Fish(position=random_position, velocity=velocity, image_path='Library/Fish.png')
            self.fish_list.append(fish)
        for _ in range(3):
            random_position = Vector(random.randint(0, 750), random.randint(0, 550))
            velocity = Vector(random.uniform(-1, 1), random.uniform(-1, 1))
            blue_fish = BlueFish(position=random_position, velocity=velocity)
            self.fish_list.append(blue_fish)
        for _ in range(5):
            random_position = Vector(random.randint(0, 750), random.randint(0, 550))
            velocity = Vector(random.uniform(-1, 1), random.uniform(-1, 1))
            red_fish = RedFish(position=random_position, velocity=velocity)
            self.fish_list.append(red_fish)

    def add_fish(self, fish):
        self.fish_list.append(fish)

    def update_and_draw(self, screen):
        for fish in self.fish_list:
            fish.update(self.fish_list)
            fish.draw(screen)