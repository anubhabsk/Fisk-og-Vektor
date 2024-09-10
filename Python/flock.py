from Python.fish import Fish

class Flock:
    def __init__(self, fish_list):
        self.fish_list = fish_list

    def update(self):
        for fish in self.fish_list:
            fish.update()

    def draw(self, screen):
        for fish in self.fish_list:
            fish.draw(screen)
