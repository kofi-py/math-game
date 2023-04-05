# Import the modules
import pygame
from my_colors import *


# Set up window
pygame.init()
screen = pygame.display.set_mode((500, 500))
screen.fill(GRAY)
pygame.display.set_caption("Math Practice for Kids")

# Fonts
sysfont = pygame.font.get_default_font()
print('system font :', sysfont)
font = pygame.font.SysFont(None, 48)
img1 = font.render('Math Practice', True, RED)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(img1, (125, 0))
    pygame.display.update()
pygame.quit()
