from turtle import width
import pygame
from config import *
import math
import random


class Spritesheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self, x, y, height, width):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        sprite.set_colorkey(BLACK)
        return sprite


class Player(pygame.sprite.Sprite):
    SCORES = 0
    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites

        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x*TILESIZE
        self.y = y*TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.facing = 'left'
        self.animation_loop = 1

        self.image = self.game.character_spritesheet.get_sprite(
            756, 127, self.width, self.height)

        self.image.set_colorkey(BLACK)

        self.x_change = 0
        self.y_change = 0

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.movement()
        self.animate()
        self.collide_enemy()
        self.collide_coin()

        self.rect.x += self.x_change
        self.collide_blocks('x')
        self.rect.y += self.y_change
        self.collide_blocks('y')

        self.x_change = 0
        self.y_change = 0

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x_change -= PLAYER_SPEED
            self.facing = 'left'
        if keys[pygame.K_RIGHT]:
            self.x_change += PLAYER_SPEED
            self.facing = 'right'
        if keys[pygame.K_UP]:
            self.y_change -= PLAYER_SPEED
            self.facing = 'up'
        if keys[pygame.K_DOWN]:
            self.y_change += PLAYER_SPEED
            self.facing = 'down'

    def collide_enemy(self):  # Killing enemies
        hits = pygame.sprite.spritecollide(self, self.game.enemies, False)
        if hits:
            self.kill()
            self.game.playing = False

    def collide_blocks(self, direction):
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left-self.rect.width
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right

        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top-self.rect.height
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom

    def collide_coin(self):
        for x in self.game.coins:
            hits = pygame.sprite.collide_circle_ratio(0.5)(self, x)
            if hits:
                self.SCORES += 1
                x.kill()
                break


    def animate(self):
        down_animations = [self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(
                               92, 81, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(137, 80, self.width, self.height)]

        up_animations = [self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height),
                         self.game.character_spritesheet.get_sprite(
                             94, 40, self.width, self.height),
                         self.game.character_spritesheet.get_sprite(136, 42, self.width, self.height)]

        left_animations = [self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(
                               48, 40, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(48, 84, self.width, self.height)]

        right_animations = [self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height),
                            self.game.character_spritesheet.get_sprite(
                                0, 40, self.width, self.height),
                            self.game.character_spritesheet.get_sprite(0, 84, self.width, self.height)]

        if self.facing == "up":
            if self.y_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(
                    0, 0, self.width, self.height)
            else:
                self.image = up_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == "down":
            if self.y_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(
                    0, 0, self.width, self.height)
            else:
                self.image = down_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == "left":
            if self.x_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(
                    0, 0, self.width, self.height)
            else:
                self.image = left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == "right":
            if self.x_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(
                    0, 0, self.width, self.height)
            else:
                self.image = right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1


class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x*TILESIZE
        self.y = y*TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_spritesheet.get_sprite(
            336, 44, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class Walls(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x*TILESIZE
        self.y = y*TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_spritesheet.get_sprite(
            40, 138, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.enemies

        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x*TILESIZE
        self.y = y*TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        
        self.x_change = 0
        self.y_change = 0

        self.facing = 'right'
        self.animation_loop = 1
        self.movement_loop_x = 0
        self.movement_loop_y = 0
        self.max_travel_x = 90
        self.max_travel_y = 90
        self.image = self.game.enemy_spritesheet.get_sprite(
            32, 41, self.width, self.height)
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.x_change = 0.5
        self.y_change = 0.5
        self.movement()
        self.rect.x += self.x_change
        self.collide_blocks('x')
        self.rect.y += self.y_change
        self.collide_blocks('y')

    def movement(self):
        if self.facing == 'left':
            self.x_change -= ENEMY_SPEED
            self.movement_loop_x -= 1
            if self.movement_loop_x <= -self.max_travel_x:
                self.facing = 'up'

        elif self.facing == 'right':
            self.x_change += ENEMY_SPEED
            self.movement_loop_x += 1
            if self.movement_loop_x >= self.max_travel_x:
                self.facing = 'down'

        elif self.facing == 'up':
            self.y_change -= ENEMY_SPEED
            self.movement_loop_y -= 1
            if self.movement_loop_y <= -self.max_travel_y:
                self.facing = 'right'

        elif self.facing == 'down':
            self.y_change += ENEMY_SPEED
            self.movement_loop_y += 1
            if self.movement_loop_y >= self.max_travel_y:
                self.facing = 'left'

    def collide_blocks(self, direction):
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left-self.rect.width
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right

        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top-self.rect.height
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom


class Button:
    def __init__(self, x, y, width, height, bg, fg, content, fontsize):
        self.font = pygame.font.SysFont("algerian", fontsize)
        self.content = content
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.fg = fg
        self.bg = bg

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.bg)
        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y

        self.text = self.font.render(self.content, True, self.fg)
        self.text_rect = self.text.get_rect(
            center=(self.width/2, self.height/2))
        self.image.blit(self.text, self.text_rect)

    def is_pressed(self, pos, pressed):
        if self.rect.collidepoint(pos):
            if pressed[0]:
                return True
            return False
        return False


class Coins(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = COIN_LAYER
        self.groups = self.game.all_sprites, self.game.coins
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x*TILESIZE
        self.y = y*TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.coin_spritesheet.get_sprite(
            460, 213, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    '''def collide_player():
            Coins.kill()
            #Coins(self, self.j, self.i)
            pass'''

    '''def __del__(self):
        print('Destructor called, Employee deleted.')'''
