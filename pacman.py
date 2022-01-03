import pygame
from pygame.locals import *

# Initializing Pygame
pygame.init()


width, height = 950, 950

background_color = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Adding icon and caption to the game
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("PACMAN")
pygame.display.update()
icon = pygame.image.load('icon.jpeg')
pygame.display.set_icon(icon)


def text(text, o, p, size, col):
    font = pygame.font.SysFont("algerian", size)
    tx = font.render(text, True, col)
    screen.blit(tx, (o, p))


running = True


def blocks():
    pass


def main(running):
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Reached")
                running = False
                pygame.quit()
                exit()


main(running)
pygame.quit()
