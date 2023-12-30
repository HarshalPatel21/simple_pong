import pygame as pg

GAME_ACTIVE = False
HOME_SCREEN = True

x = 3
SCREEN_WIDTH = 318*x
SCREEN_HEIGHT = 159*x

PLAYER_WIDTH = 10
PLAYER_HEIGHT = 100

PLAYERS_COLORS = ['red','blue']
PLAYERS_MOVEMENT = [
    [pg.K_s,pg.K_w],
    [pg.K_DOWN, pg.K_UP]
]
PLAYERS_X_POS = [100,900]