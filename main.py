import pygame
from my_colors import *

pygame.init()
screen = pygame.display.set_mode((500, 500))
screen.fill(GRAY)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.quit()
