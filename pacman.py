import pygame
from pygame.locals import *

pygame.init()


width, height = 950, 950

background_color = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("PACMAN")
pygame.display.update()

# TEXT


def text(text, o, p, size, col):
    font = pygame.font.SysFont("algerian", size)
    tx = font.render(text, True, col)
    screen.blit(tx, (o, p))


while True:
    for event in pygame.event.get():
        if event.type == pygame.quit():
            print("Reached")
            pygame.quit()
            exit()

        else:
            continue


pygame.quit()
