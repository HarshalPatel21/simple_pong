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
        self.ball = Ball(pg.color.Color("green"))
        
        # sprites
        self.all_sprites = pg.sprite.Group(self.ball,self.player_1,self.player_2)
    

    def collision_sprite(self , ball,player):
        if pg.sprite.collide_rect(ball,player):
            print("Collision detected!")


    def run(self ,dt):

        self.display_surf.fill((0, 0, 0))
       
        self.collision_sprite(self.ball,self.player_1)
        self.collision_sprite(self.ball,self.player_2)
        self.all_sprites.clear(self.display_surf,self.background)
        self.all_sprites.update(dt)
        self.all_sprites.draw(self.display_surf)

