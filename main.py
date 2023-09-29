import pygame as pg 
import sys
from level import Level
from settings import *

class Game:

    def __init__(self) -> None:
        pg.init()
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption('Pong')
        self.level = Level()
        self.clock = pg.time.Clock()

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            dt = self.clock.tick()/1000
            self.level.run(dt)
            pg.display.update()
            



if __name__ == "__main__":
    game = Game()
    game.run()
