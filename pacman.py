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
        self.clock = pygame.time.Clock()
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
        self.player = Player(self, 1, 2)
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


class walls(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(blue)

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


g = game()
g.new()
while g.running:

    g.main()
    g.blocks()
    pygame.display.update()
    g.gameover()
pygame.quit()
