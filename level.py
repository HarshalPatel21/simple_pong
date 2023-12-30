import pygame as pg
from settings import *
from player import Player
from ball import Ball

class  Level :

    def __init__(self) -> None:
        
        # global variable 
        global GAME_ACTIVE
        
        self.display_surf = pg.display.get_surface()
        self.background = pg.Surface(self.display_surf.get_size())
        self.background.fill((0, 0, 0)) # home screen

        # players 
        self.player_1 = Player(0)
        self.player_2 = Player(1)

        # ⚽⚽⚽
        self.ball = Ball(pg.color.Color('blue'),self.player_1,self.player_2)
        
        # sprites
        self.all_sprites = pg.sprite.Group(self.ball,self.player_1,self.player_2)

        # font 
        self.font = pg.font.Font(None, 36) 
        self.bg = pg.image.load('bg.jpg').convert_alpha()
        self.bg = pg.transform.rotozoom(self.bg,0,3)
        self.bg_rect = self.bg.get_rect()


    def score(self,player):
        self.text = self.font.render(str(player.score), True, (255, 255, 255)) # score color
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (SCREEN_WIDTH // 2 - 150 + 300*player.index, 30)
        self.display_surf.blit(self.text, self.text_rect)

        # if player.score >= 10 :
        #     GAME_ACTIVE = False

    def run(self ,dt):

        self.display_surf.fill((0, 0, 0))
        self.display_surf.blit(self.bg,self.bg_rect)

        self.score(self.player_1)
        self.score(self.player_2)

        self.all_sprites.clear(self.display_surf,self.background)
        self.all_sprites.update(dt)
        self.all_sprites.draw(self.display_surf)

      