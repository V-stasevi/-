import pygame
from inky  import Inky
from constants import SIZE, BLACK, MATRIX
from pacman import Pacman
from field import Field


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(SIZE)
        self.gameover = False
        self.pacman = Pacman()
        self.inky = Inky()
        self.field = Field(1, 1, 15)

    def main_loop(self):
        while not self.gameover:
            self.process_events()
            self.process_logic()
            self.process_drawing()
            pygame.time.wait(225)

    def process_events(self):
        for event in pygame.event.get():  # Получение всех событий
            if event.type == pygame.QUIT:  # Событие выхода
                self.gameover = True
            self.pacman.check_event(event)

    def process_logic(self):
        self.pacman.logic()
        self.inky.logic();

    def process_drawing(self):
        self.screen.fill(BLACK)
        self.field.draw(self.screen)
        self.pacman.draw(self.screen)
        self.inky.draw(self.screen)
        pygame.display.flip()
