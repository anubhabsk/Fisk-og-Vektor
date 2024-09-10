import pygame

from Python.vector2 import Vector
    
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

fish_img = pygame.image.load('Fish.png')
fish_img = pygame.transform.scale(fish_img, (50, 50))

position = Vector(400, 300)
velocity = Vector(1, 1)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update position
    position = position + velocity
    
    # Boundary conditions
    if position.x < 0 or position.x > 800 - 50:  # Fish width is 50
        velocity.x = -velocity.x
    if position.y < 0 or position.y > 600 - 50:  # Fish height is 50
        velocity.y = -velocity.y
    
    screen.fill((0, 128, 255))
    screen.blit(fish_img, (position.x, position.y))
    
    # Implement animations here if needed
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
