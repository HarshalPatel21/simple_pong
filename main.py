import pygame as pg 
import sys
from level import Level
from settings import *

class Game:

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption('Pong')
        self.level = Level()
        self.clock = pg.time.Clock()
    
        self.font = pg.font.Font(None, 50)

        
    def run(self):
        while True :
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            global GAME_ACTIVE
            global HOME_SCREEN

            if GAME_ACTIVE :
                dt = self.clock.tick(60)/1000
                self.level.run(dt)

            else:
                if HOME_SCREEN :
                    self.text = self.font.render("Home Screen", True, (255, 255, 255)) #text color
                    self.text_rect = self.text.get_rect()
                    self.text_rect.center = (SCREEN_WIDTH // 2 , SCREEN_HEIGHT//2)
                    self.screen.blit(self.text, self.text_rect)

                    if pg.key.get_pressed()[pg.K_SPACE]:
                        GAME_ACTIVE = True
                        HOME_SCREEN = False

                # else:
                #     self.text = self.font.render("Player Won !!", True, (255, 255, 255))
                #     self.text_rect = self.text.get_rect()
                #     self.text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT//2)
                #     self.screen.blit(self.text, self.text_rect)

                #     if pg.key.get_pressed()[pg.K_SPACE]:
                #         HOME_SCREEN = True
            
            pg.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()
