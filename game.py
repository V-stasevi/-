import pygame

from constants import SIZE, BLACK
from pacman import Pacman


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(SIZE)  # Установка размеров окна
        self.gameover = False
        self.pac = Pacman()

    def main_loop(self):
        while not self.gameover:  # Основной цикл
            self.process_events()
            self.process_logic()
            self.process_drawing()
            pygame.time.wait(275)  # Ожидание отрисовки

    def process_events(self):
        for event in pygame.event.get():  # Получение всех событий
            if event.type == pygame.QUIT:  # Событие выхода
                self.gameover = True
            self.pac.check_event(event)

    def process_logic(self):
        self.pac.move()

    def process_drawing(self):
        self.screen.fill(BLACK)  # Заливка цветом
        self.pac.draw(self.screen)
        pygame.display.flip()  # Double buffering
