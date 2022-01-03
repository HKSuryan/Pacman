import pygame
import random
import time
import sys
from pygame.locals import *
pygame.init()


width, height = 950, 950

background_color = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

screen = pygame.display.set_mode((width, height))
global running
pygame.display.set_caption('Pacman')
pygame.display.update()

pygame.draw.line(screen, white, (50, 80), (80, 100))
pygame.display.update()


def mainwin():

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.quit():
                print("reached")
                running = False
                pygame.quit()
                sys.exit()
                break
                quit()
                exit()
        # screen.fill(white)
            else:
                print("message")
                continue


mainwin()
