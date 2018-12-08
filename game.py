import pygame
from settings_control import ButtonControl

from constants import SIZE, BLACK, SIZE_B
from pacman import Pacman
from field import Field
import Menu
import constants as cm
from score import Score

from sound_system import Sounds

class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode(SIZE)
        self.gameover = False
        self.isMenu = True
        self.objects = []
        self.score = -40

        self.sounds = Sounds()
        self.menu = Menu.Menu(self.screen, cm.pic_play, cm.pic_records, cm.pic_options, cm.pic_bg, self.runGame,
                              self.showScore, self.showOption)
        self.field = Field(0, 0, 15)
        self.pacman = Pacman(self.field.matrix, self.sounds)
        self.score = Score(15, 35, self.screen, self.field)


        self.prepare_scene()

        self.dict_functions = {"sound_control": self.turn_off_music,
                                "level_control": self.change_game_level,
                                "records_control": self.clear_records,
                          }

        self.settings_control = ButtonControl(self.screen, self.dict_functions)

    def prepare_scene(self):
        self.field.matrix[3][1].isBig = True
        self.field.matrix[23][1].isBig = True
        self.field.matrix[23][26].isBig = True
        self.field.matrix[3][26].isBig = True

    def main_loop(self):
        self.sounds.playIntroSound()
        while not self.gameover:
            self.process_events()
            self.process_logic()
            self.process_drawing()
            pygame.time.wait(150)

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gameover = True
            if not self.isMenu:
                self.pacman.check_event(event)
            else:
                self.menu.events(event)

    def process_logic(self):
        if self.isMenu:
            pass
        else:
            self.pacman.logic(self.score)

    def process_drawing(self):
        self.screen.fill(BLACK)
        if self.isMenu:
            self.menu.draw(self.screen)
        else:
            self.field.draw(self.screen)
            self.pacman.draw(self.screen)
            self.score.draw()

        pygame.display.flip()

    def pacman_rect(self):
        return self.pacman.rect

    def runGame(self):
        self.isMenu = False
        self.screen = pygame.display.set_mode(SIZE_B)

    def showScore(self):
        print('showScore')

    def showOption(self):
        self.settings_control.main_loop()


    def turn_off_music(self, result):
        if self.sounds.volume == 1:
            self.sounds.updateVolume(0)
        else:
            self.sounds.updateVolume(1)

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