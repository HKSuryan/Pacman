from re import A
import pygame
from pygame.locals import *
from sprites import *
from config import *
import sys
# Initializing Pygame
pygame.init()


width, height = 950, 950

background_color = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
Black = (0, 0, 0)


class Spritesheet:
    def __init__(self, file):
        self.sheets = pygame.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pygame.surface([width, height])
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        sprite.set_colorkey(Black)
        return sprite


class game:

    def __init__(self):
        pygame.init()
        '''image_to_load = pygame.image.load("walls.jpg.webp")
        self.running = True
        self.image.blit(image_to_load, (0, 0))'''
        self.running = True
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.clock()
        pygame.display.set_caption("PACMAN")
        pygame.display.update()
        self.icon = pygame.image.load('icon.jpeg')
        pygame.display.set_icon(self.icon)
        self.character_spritesheet = Spritesheet('img.png')
        self.terrain = Spritesheet('walls.jpg.webp')

    def new(self):
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.player = Player()
        self.attacks = pygame.sprite.LayeredUpdates()

    def text(self, text, o, p, size, col):
        font = pygame.font.SysFont("algerian", size)
        tx = font.render(text, True, col)
        self.screen.blit(tx, (o, p))

    def drawrect(self, x, y, length, breadth):
        other_rect = pygame.Rect(x, y, length, breadth)
        pygame.draw.rect(self.screen, red, other_rect, 25)

    def blocks(self):
        # Left column
        self.drawrect(50, 50, 250, 50)
        self.drawrect(50, 100, 50, 200)
        self.drawrect(100, 250, 50, 50)
        self.drawrect(250, 100, 50, 200)
        self.drawrect(200, 250, 50, 50)
        self.drawrect(150, 150, 50, 50)
        pygame.display.update()

        # Left Middle column
        self.drawrect(50, 400, 150, 50)
        self.drawrect(50, 500, 150, 50)
        self.drawrect(250, 350, 50, 250)
        pygame.display.update()

        # Left Bottom column
        self.drawrect(50, 650, 50, 200)
        self.drawrect(50, 850, 250, 50)
        self.drawrect(100, 650, 50, 50)
        self.drawrect(250, 650, 50, 200)
        self.drawrect(200, 650, 50, 50)
        self.drawrect(150, 750, 50, 50)
        pygame.display.update()

        # Top Column
        self.drawrect(400, 50, 50, 150)
        self.drawrect(500, 50, 50, 150)
        self.drawrect(350, 250, 250, 50)
        pygame.display.update()

        # Right Column
        self.drawrect(650, 50, 250, 50)
        self.drawrect(650, 100, 50, 200)
        self.drawrect(700, 250, 50, 50)
        self.drawrect(850, 100, 50, 200)
        self.drawrect(800, 250, 50, 50)
        self.drawrect(750, 150, 50, 50)
        pygame.display.update()

        # Right Middle
        self.drawrect(650, 350, 50, 250)
        self.drawrect(750, 400, 150, 50)
        self.drawrect(750, 500, 150, 50)
        pygame.display.update()

        # Right Bottom
        self.drawrect(650, 850, 250, 50)
        self.drawrect(650, 650, 50, 200)
        self.drawrect(700, 650, 50, 50)
        self.drawrect(850, 650, 50, 200)
        self.drawrect(800, 650, 50, 50)
        self.drawrect(750, 750, 50, 50)
        self, pygame.display.update()

        # Bottom
        self.drawrect(350, 650, 250, 50)
        self.drawrect(400, 750, 50, 150)
        self.drawrect(500, 750, 50, 150)
        pygame.display.update()

        # Middle
        self.drawrect(350, 350, 250, 50)
        self.drawrect(350, 400, 50, 200)
        self.drawrect(400, 550, 50, 50)
        self.drawrect(550, 400, 50, 200)
        self.drawrect(500, 550, 50, 50)
        self.drawrect(450, 450, 50, 50)
        pygame.display.update()


class walls(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(blue)

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


class player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = self.game.character_spritesheet.get_sprite(3, 2, 32, 32)


def main(running):
    A = game()
    A.blocks()
    isjump = False
    vel = 10
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
        if x > 850:
            #x = 50
            vel = -vel
        elif x < 50:
            # x = 850
            vel = -vel
        if y < 50:
            vel = - vel
            #y = 850
        elif y > 850:
            vel = -vel
            # y = 50
        if (x == 450 and x < 500) and (y == 50):
            y = 850
        elif (x == 450 and x < 500) and (y == 850):
            y = 50
        if (y == 450 and y < 500) and (x == 50):
            x = 850
        elif (y == 450 and y < 500) and (x == 850):
            x = 50
        moving_rect = pygame.Rect(x, y, 50, 50)
        pygame.draw.rect(A.screen, blue, moving_rect)
        pygame.display.update()
        pygame.time.delay(200)
        pygame.draw.rect(A.screen, background_color, moving_rect)


running = True
main(running)
pygame.quit()
