import pygame

from text import Text
from constants import SIZE, BLACK
#from pacman import Pacman
from field import Field


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(SIZE)
        self.gameover = False
        self.objects = []
        self.prepare_scene()
        #self.pacman = Pacman()
        self.field = Field(20, 20)

    def prepare_scene(self):
        self.objects.append(Text(100, 100))

    def main_loop(self):
        while not self.gameover:
            self.process_events()
            self.process_logic()
            self.process_drawing()
            pygame.time.wait(10)

    def process_events(self):
        for event in pygame.event.get():  # Получение всех событий
            if event.type == pygame.QUIT:  # Событие выхода
                self.gameover = True
            #self.pacman.check_event(event)

    def process_logic(self):
        #self.pacman.logic()
        pass

    def process_drawing(self):
        self.screen.fill(BLACK)
        self.field.draw(self.screen)#What?
        #self.pacman.draw(self.screen)
        pygame.display.flip()
