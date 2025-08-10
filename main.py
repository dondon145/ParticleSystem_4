import pygame
from pygame.locals import *
import emitter_2

pygame.init()

WIDTH = 800
HEIGHT = 800
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))

FPS = 60
clock = pygame.time.Clock()

# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

particle_group = pygame.sprite.Group()
basic_emitter = emitter_2.FountainEmitter(1000, particle_group)

running = True

while running:
    DISPLAY.fill(BLACK)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
        if event.type == KEYDOWN:
            basic_emitter.emitt()
            
    
    basic_emitter.update()
    particle_group.update()
    particle_group.draw(DISPLAY)

    #print(int(clock.get_fps()))
    pygame.display.flip()
    clock.tick(FPS)
