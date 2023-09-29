import pygame as pg 
from settings import *

class Player(pg.sprite.Sprite):

    def __init__(self, index) -> None:
        super().__init__()

        self.image = pg.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(PLAYERS_COLORS[index])
        self.rect = self.image.get_rect()
        self.index = index
        self.rect.center = (PLAYERS_X_POS[self.index] , SCREEN_HEIGHT/2)
        self.position = pg.Vector2(PLAYERS_X_POS[self.index], SCREEN_HEIGHT/2)
        self.velocity = pg.Vector2(x=0,y=1)

    def input(self):

        keys = pg.key.get_pressed()
        
        # down
        if keys[PLAYERS_MOVEMENT[self.index][0]]:
            self.position += self.velocity

            if self.position.y > SCREEN_HEIGHT - PLAYER_HEIGHT/2 - 7 : 
                self.position.y = SCREEN_HEIGHT - PLAYER_HEIGHT/2 -7

        # up
        if keys[PLAYERS_MOVEMENT[self.index][1]]:
            self.position -= self.velocity

            if self.position.y < PLAYER_HEIGHT/2 + 7 : 
                self.position.y = PLAYER_HEIGHT/2 + 7
        
        self.rect.center = self.position

    def update(self):
        self.input()
