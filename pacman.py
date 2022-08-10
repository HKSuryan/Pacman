import pygame
from pygame.locals import *

# Initializing Pygame
pygame.init()


width, height = 950, 950

background_color = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)

# Adding icon and caption to the game
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("PACMAN")
pygame.display.update()
icon = pygame.image.load('icon.jpeg')
pygame.display.set_icon(icon)

# For Presenting text on the screen


def text(text, o, p, size, col):
    font = pygame.font.SysFont("algerian", size)
    tx = font.render(text, True, col)
    screen.blit(tx, (o, p))


running = True


def blocks():
    def drawrect(x, y, length, breadth):
        pygame.draw.rect(screen, red, (x, y, length, breadth), 25)

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
    pygame.display.update()

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
    pygame.display.update()

    # Right Column
    drawrect(650, 50, 250, 50)
    drawrect(650, 100, 50, 200)
    drawrect(700, 250, 50, 50)
    drawrect(850, 100, 50, 200)
    drawrect(800, 250, 50, 50)
    drawrect(750, 150, 50, 50)
    pygame.display.update()

    # Right Middle
    drawrect(650, 350, 50, 250)
    drawrect(750, 400, 150, 50)
    drawrect(750, 500, 150, 50)
    pygame.display.update()

    # Right Bottom
    drawrect(650, 850, 250, 50)
    drawrect(650, 650, 50, 200)
    drawrect(700, 650, 50, 50)
    drawrect(850, 650, 50, 200)
    drawrect(800, 650, 50, 50)
    drawrect(750, 750, 50, 50)
    pygame.display.update()

    # Bottom
    drawrect(350, 650, 250, 50)
    drawrect(400, 750, 50, 150)
    drawrect(500, 750, 50, 150)
    pygame.display.update()

    # Middle
    drawrect(350, 350, 250, 50)
    drawrect(350, 400, 50, 200)
    drawrect(400, 550, 50, 50)
    drawrect(550, 400, 50, 200)
    drawrect(500, 550, 50, 50)
    drawrect(450, 450, 50, 50)
    pygame.display.update()


def main(running):
    blocks()
    isjump = False
    vel = 5
    x, y = 150, 450
    jumpcount = 10
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Reached")
                running = False
                pygame.quit()
                exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x > 50:
            x -= vel

        elif keys[pygame.K_RIGHT] and x < 850:
            x += vel

        elif not(isjump):
            if keys[pygame.K_DOWN] and y < 850:
                y += vel

            if keys[pygame.K_UP] and y > 50:
                y -= vel

            if keys[pygame.K_SPACE]:
                isjump = True
        else:
            if jumpcount >= -10:
                neg = 1
                if jumpcount < 0:
                    neg = -1
                y -= (jumpcount**2)*0.5*neg
                jumpcount -= 1
            else:
                isjump = False
                jumpcount = 10

        pygame.draw.rect(screen, blue, (x, y, 50, 50))
        pygame.display.update()
        pygame.time.delay(200)
        pygame.draw.rect(screen, background_color, (x, y, 50, 50))


main(running)
pygame.quit()
