from re import A
from tarfile import BLOCKSIZE
import pygame
from pygame.locals import *
from sprites import *
from config import *
import sys
# Initializing Pygame
pygame.init()


width, height = 750, 570

background_color = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
Black = (0, 0, 0)


class game:

    def __init__(self):
        pygame.init()
        self.running = True

        self.screen = pygame.display.set_mode(
            (width, height), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("PACMAN")
        pygame.display.update()
        self.icon = pygame.image.load('icon.jpeg')
        pygame.display.set_icon(self.icon)
        self.font = pygame.font.SysFont("algerian", 30)
        self.enemy_spritesheet = Spritesheet('pacsp.png')
        self.character_spritesheet = Spritesheet('pac_sprites.png')
        self.terrain_spritesheet = Spritesheet('walls.jpg.webp')
        self.coin_spritesheet = Spritesheet('pacsp.png')
        self.intro_background = pygame.image.load('images.jpeg')
        #self.go_background = pygame.image.load('endscreen1.jpeg')

    def createTilemap(self):
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                if column == "B":
                    Block(self, j, i)
                if column == "P":
                    Player(self, j, i)
                if column == "L":
                    Walls(self, j, i)
                if column == "E":
                    Enemy(self, j, i)
                if column == "C":
                    Coins(self, j, i)

    def new(self):

        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.walls = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()
        self.coins = pygame.sprite.LayeredUpdates()
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

    def gameover(self):
        text = self.font.render('GAME OVER', True, WHITE)
        text_rect = text.get_rect(center=(WIN_WIDTH/2, WIN_HEIGHT/2))

        restart_button = Button(10, WIN_HEIGHT-60, 120,
                                50, WHITE, BLACK, 'RESTART', 30)

        for sprite in self.all_sprites:
            sprite.kill()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if restart_button.is_pressed(mouse_pos, mouse_pressed):
                self.new()
                self.main()

            self.screen.fill(BLACK)
            self.screen.blit(text, text_rect)
            self.screen.blit(restart_button.image, restart_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()

    def intro_screen(self):
        intro = True
        play_button = Button(50, 50, 100, 50, WHITE, BLACK, 'PLAY', 32)
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if play_button.is_pressed(mouse_pos, mouse_pressed):
                intro = False

            self.screen.blit(self.intro_background, (375, 240))

            self.screen.blit(play_button.image, play_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()


g = game()
g.intro_screen()
g.new()
while g.running:

    g.main()

    pygame.display.update()
    g.gameover()
pygame.quit()
