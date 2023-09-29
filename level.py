import pygame as pg
from settings import *
from player import Player
from ball import Ball

class  Level :

    def __init__(self) -> None:
        self.display_surf = pg.display.get_surface()
        self.background = pg.Surface(self.display_surf.get_size())
        self.background.fill((0, 0, 0))

        self.player_1 = Player(0)
        self.player_2 = Player(1)
        self.ball = Ball(pg.color.Color("green"),self.player_1,self.player_2)
        
        # sprites
        self.all_sprites = pg.sprite.Group(self.ball,self.player_1,self.player_2)

        # font
        self.font = pg.font.Font(None, 36)

        # self.text = self.font.render(str(self.player_1.score), True, (255, 255, 255))
        # self.text_rect = self.text.get_rect()
        # self.text_rect.center = (SCREEN_WIDTH // 2 - 50,150 )

        # self.screen.blit(self.text, self.text_rect)
        
    def score(self,player):
        self.text = self.font.render(str(player.score), True, (255, 255, 255))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (SCREEN_WIDTH // 2 - 150 + 300*player.index, 30)
        self.display_surf.blit(self.text, self.text_rect)

    def run(self ,dt):

        self.display_surf.fill((0, 0, 0))

        self.score(self.player_1)
        self.score(self.player_2)

        self.all_sprites.clear(self.display_surf,self.background)
        self.all_sprites.update(dt)
        self.all_sprites.draw(self.display_surf)

      