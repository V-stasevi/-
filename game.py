import pygame

from text import Text
from constants import SIZE, BLACK
import Menu
import constants_menu as cm

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(SIZE)  
        self.gameover = False
        self.objects = []
        self.prepare_scene()
        self.menu = Menu.Menu(self.screen, cm.pic_play, cm.pic_records, cm.pic_options, cm.pic_bg)

    def prepare_scene(self):
        pass

    def main_loop(self):
        while not self.gameover:  
            self.process_events()
            self.process_logic()
            self.process_drawing()
            pygame.time.wait(50)

    def process_events(self):
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                self.gameover = True
            self.menu.events(event)

    def process_logic(self):
        pass

    def process_drawing(self):
        self.screen.fill(BLACK)
        self.menu.draw(self.screen)
        pygame.display.flip()  
