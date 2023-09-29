import pygame as pg

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

PLAYER_WIDTH = 20
PLAYER_HEIGHT = 100

PLAYERS_COLORS = ['red','blue']
PLAYERS_MOVEMENT = [
    [pg.K_s,pg.K_w],
    [pg.K_DOWN, pg.K_UP]
]
PLAYERS_X_POS = [100,900]