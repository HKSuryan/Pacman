from re import A
from tarfile import BLOCKSIZE
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
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface([width, height])
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
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("PACMAN")
        pygame.display.update()
        self.icon = pygame.image.load('icon.jpeg')
        pygame.display.set_icon(self.icon)

        self.character_spritesheet = Spritesheet('img.png')
        self.terrain_spritesheet = Spritesheet('walls.jpg.webp')

    def createTilemap(self):
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                if column == "B":
                    Block(self, j, i)
                if column == "P":
                    Player(self, j, i)

    def new(self):

        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()

        self.attacks = pygame.sprite.LayeredUpdates()
        self.createTilemap()

    def text(self, text, o, p, size, col):
        font = pygame.font.SysFont("algerian", size)
        tx = font.render(text, True, col)
        self.screen.blit(tx, (o, p))

    def drawrect(self, x, y, length, breadth):
        other_rect = pygame.Rect(x, y, length, breadth)
        pygame.draw.rect(self.screen, red, other_rect, 25)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    def main(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False

    def gameover(self):
        pass

    def intro_screen(self):
        pass


class walls(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(blue)

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


g = game()
g.intro_screen()
g.new()
while g.running:

    g.main()
    g.blocks()
    pygame.display.update()
    g.gameover()
pygame.quit()
