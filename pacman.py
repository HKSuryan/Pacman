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
    def drawrect(x, y, length, breadth):
        pygame.draw.rect(screen, red, (x, y, length, breadth))

    # Left column
    drawrect(50, 50, 250, 50)
    drawrect(50, 100, 50, 200)
    drawrect(100, 250, 50, 50)
    drawrect(250, 100, 50, 200)
    drawrect(200, 250, 50, 50)
    drawrect(150, 150, 50, 50)
    pygame.display.update()

    # Left Middle column
    drawrect(50, 400, 150, 50)
    drawrect(50, 500, 150, 50)
    drawrect(250, 350, 50, 250)

    # Left Bottom column
    drawrect(50, 650, 50, 200)
    drawrect(50, 850, 250, 50)
    drawrect(100, 650, 50, 50)
    drawrect(250, 650, 50, 200)
    drawrect(200, 650, 50, 50)
    drawrect(150, 750, 50, 50)
    pygame.display.update()

    # Top Column
    drawrect(400, 50, 50, 150)
    drawrect(500, 50, 50, 150)
    drawrect(350, 250, 250, 50)

    # Right Column
    drawrect(650, 50, 250, 50)
    drawrect(650, 100, 50, 200)
    drawrect(700, 250, 50, 50)
    drawrect(850, 100, 50, 200)
    drawrect(800, 250, 50, 50)
    drawrect(750, 150, 50, 50)

    # Right Middle
    drawrect(650, 350, 50, 250)
    drawrect(750, 400, 150, 50)
    drawrect(750, 500, 150, 50)

    # Right Bottom
    drawrect(650, 850, 250, 50)
    drawrect(650, 650, 50, 200)
    drawrect(700, 650, 50, 50)
    drawrect(850, 650, 50, 200)
    drawrect(800, 650, 50, 50)
    drawrect(750, 750, 50, 50)

    # Bottom
    drawrect(350, 650, 250, 50)
    drawrect(400, 750, 50, 150)
    drawrect(500, 750, 50, 150)

    # Middle
    drawrect(350, 350, 250, 50)
    drawrect(350, 400, 50, 200)
    drawrect(400, 550, 50, 50)
    drawrect(550, 400, 50, 200)
    drawrect(500, 550, 50, 50)
    drawrect(450, 350, 50, 50)
    pygame.display.update()


def main(running):
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Reached")
                running = False
                pygame.quit()
                exit()

        blocks()


main(running)
pygame.quit()
