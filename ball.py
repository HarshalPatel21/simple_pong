import pygame as pg 
from settings import *
import math

class Ball(pg.sprite.Sprite):


    def __init__(self, color,player_1_sprite,player_2_sprite):
        pg.sprite.Sprite.__init__(self)

        self.radius = 10
        self.image = pg.Surface((2*self.radius, 2*self.radius))
        self.image.fill((0, 0, 0))
        pg.draw.circle(self.image, (color), (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

        # movements
        self.speed = 2
       

        self.position = pg.Vector2((SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        self.velocity = pg.Vector2((self.speed*2,self.speed))
        
        self.new_x = SCREEN_WIDTH/2
        self.new_y = SCREEN_HEIGHT/2

        self.player_1_sprite = player_1_sprite
        self.player_2_sprite = player_2_sprite

        self.player_1_collide = False
        self.player_2_collide = False

    def collision_sprite(self, ball, player):
        if pg.sprite.collide_rect(ball,player):
            return True

        else: return False    

    def moving(self):
        
        # simply bounce
        
        if self.position.y > SCREEN_HEIGHT-10 or self.position.y < 10:
            self.velocity.y = -self.velocity.y

        if self.position.x > SCREEN_WIDTH-10 or self.position.x < 10:
            self.velocity.x = -self.velocity.x

        # player collisions
        if self.player_1_collide and self.position.x >= PLAYERS_X_POS[0]:
            self.velocity.x = - self.velocity.x
            self.position.x += 3
        
        if self.player_2_collide and self.position.x <= PLAYERS_X_POS[1]: 
            self.velocity.x = - self.velocity.x
            self.position.x -= 3

        self.position += self.velocity
        self.rect.center = self.position

    def update(self,dt):
        self.moving()
        self.player_1_collide = self.collision_sprite(self, self.player_1_sprite)
        self.player_2_collide = self.collision_sprite(self,self.player_2_sprite)