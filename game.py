import pygame
from button import Button

from text import Text
from constants import SIZE, BLACK

RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
ORANGE = (255,180,0)

BUTTON_STYLE = {"hover_color" : BLUE,
                "clicked_color" : GREEN,
                "clicked_font_color" : BLACK,
                "hover_font_color" : ORANGE
                }

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(SIZE)  # Установка размеров окна
        self.gameover = False
        self.objects = []
        self.prepare_scene()

        self.settings_button = Button((5, 5, 50, 50), RED, self.show_settings_screen, text="he", **BUTTON_STYLE)

    def prepare_scene(self):
        self.objects.append(Text(100, 100))

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
        for i in self.objects:
            i.shift()

    def process_drawing(self):
        self.screen.fill(BLACK)  # Заливка цветом
        for i in self.objects:
            i.draw(self.screen)

        self.settings_button.update(self.screen)  # drawing settings button

        pygame.display.flip()  # Double buffering




    def show_settings_screen(self):
        print('settings screen reached')
