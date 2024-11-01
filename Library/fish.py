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
        self.max_force = 1
        self.vision_distance = random.randint(30, 70)
    
    def dist(self, a, b):
        return (a - b).length

    def separation(self, l: list, tooClose: int, sepfac: float):
        sep_vec = Vector(0, 0)
        count = 0
        for fish in l:
            if fish is not self:
                if self.dist(self.position, fish.position) < tooClose:
                    v = (self.position - fish.position).normalize()
                    v /= self.dist(self.position, fish.position)
                    sep_vec += v
                    count += 1
        if count > 0:
            sep_vec /= count  
        return sep_vec * sepfac

    def alignment(self, other_fishes, alignment_factor):
        avg_velocity = Vector(0, 0)
        count = 0
        for fish in other_fishes:
            if fish is not self:
                avg_velocity += fish.velocity
                count += 1
        if count > 0:
            avg_velocity /= count
            avg_velocity = avg_velocity.normalize() * self.maxvelocity
        return avg_velocity * alignment_factor
    
    def cohesion(self, other_fishes, cohesion_factor, isolation_distance):
        if self.is_isolated(other_fishes, isolation_distance):
            return Vector(0, 0)
        avg_position = Vector(0, 0)
        count = 0
        for fish in other_fishes:
            if fish is not self: 
                avg_position += fish.position
                count += 1
        if count > 0:
            avg_position /= count
            desired = (avg_position - self.position).normalize() * self.maxvelocity
            steer = (desired - self.velocity).limit(self.max_force)
            return steer * cohesion_factor
        return Vector(0, 0)
    
    def is_isolated(self, other_fishes, isolation_distance):
        for fish in other_fishes:
            if fish is not self:
                distance = self.dist(self.position, fish.position)
                if distance < isolation_distance:
                    return False
        return True

    def steer(self, target):
        desired = (target - self.position).normalize() * self.maxvelocity
        steer = (desired - self.velocity).limit(self.max_force)
        return steer

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

    def update(self, fish_list):
        alignment_factor = 0.001
        cohesion_factor = 0.1
        isolation_distance = 100
        self.velocity += self.separation(fish_list, 30, 2)
        self.velocity += self.alignment(fish_list, alignment_factor)
        self.velocity += self.cohesion(fish_list, cohesion_factor, isolation_distance)
        self.position += self.velocity
        self.screenConfinement()
        self.image = pygame.transform.rotate(self.copy, -degrees(self.velocity.polar360))

    def draw(self, screen):
        screen.blit(self.image, (self.position.x, self.position.y))