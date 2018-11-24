import pygame

from text import Text
from constants import SIZE, BLACK
from field import Field


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(SIZE)  # Установка размеров окна
        self.gameover = False
        self.field = Field(1, 1, 16)

    def main_loop(self):
        while not self.gameover:  # Основной цикл
            self.process_events()
            self.process_logic()
            self.process_drawing()
            pygame.time.wait(10)  # Ожидание отрисовки

    def process_events(self):
        for event in pygame.event.get():  # Получение всех событий
            if event.type == pygame.QUIT:  # Событие выхода
                self.gameover = True

    def process_logic(self):
        pass

    def process_drawing(self):
        self.screen.fill(BLACK)  # Заливка цветом
        self.field.draw(self.screen)
        pygame.display.flip()  # Double buffering
