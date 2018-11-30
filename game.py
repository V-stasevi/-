import pygame
from settings_control import ButtonControl

from text import Text
from constants import SIZE, BLACK, BUTTON_STYLE_REGULAR


class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode(SIZE)  # Установка размеров окна
        self.gameover = False
        self.objects = []
        self.prepare_scene()

        self.dict_functions = {"sound_control": self.turn_off_music,
                                "level_control": self.change_game_level,
                                "records_control": self.clear_records,
                          }

        self.settings_control = ButtonControl(self.screen, self.dict_functions)


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

            self.settings_control.check_control_button_event(event)



    def process_logic(self):
        for i in self.objects:
            i.shift()

    def process_drawing(self):
        self.screen.fill(BLACK)  # Заливка цветом
        for i in self.objects:
            i.draw(self.screen)

        self.settings_control.draw_control_button()
        pygame.display.flip()  # Double buffering


    def turn_off_music(self, result):
        #logic to turn off/on music
        '''
        if music class.is_playing:
            print("turning music off")
        else:
            print("turning music on")
        music class.is_playing = not music class.is_playing
        '''

    def change_game_level(self, result):
        #logic to change the level accordingly
        if result == 1:
            print("change level to 1")
        elif result == 2:
            print("change level to 2")
        elif result == 3:
            print("change level to 3")
        else:
            print("hmmm, unexpected level")


    def clear_records(self, result):
        # logic to clear records
        print("clearing records")
