import pygame
from settings_control import ButtonControl

from class_ghost import Ghost
from text import Text
from constants import SIZE, BLACK, SIZE_B
from constants import picGhost_Blinky, picGhost_Clyde, picGhost_Inky, picGhost_Pinky
from pacman import Pacman
from field import Field
import Menu
import constants as cm

from Grains import smallGrain, enegrizer


class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode(SIZE)
        self.gameover = False
        self.isMenu = True
        self.objects = []
        self.menu = Menu.Menu(self.screen, cm.pic_play, cm.pic_records, cm.pic_options, cm.pic_bg, self.runGame,
                              self.showScore, self.showOption)
        self.pacman = Pacman()
        self.field = Field(0, 0, 15)
        self.prepare_scene()

        self.dict_functions = {"sound_control": self.turn_off_music,
                                "level_control": self.change_game_level,
                                "records_control": self.clear_records,
                          }

        self.settings_control = ButtonControl(self.screen, self.dict_functions)

    def main_loop(self):
        while not self.gameover:
            self.process_events()
            self.process_logic()
            self.process_drawing()
            pygame.time.wait(150)

    def prepare_scene(self):
        pass

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gameover = True
            if not self.isMenu:
                self.pacman.check_event(event)
            else:
                self.menu.events(event)

    def process_logic(self):
        self.pacman.logic()
        #for el in self.ghosts:
            #el.move()

    def process_drawing(self):
        self.screen.fill(BLACK)
        if self.isMenu:
            self.menu.draw(self.screen)
            for i in self.objects:
                i.draw(self.screen)
        else:
            self.field.draw(self.screen)
            self.pacman.draw(self.screen)

        #for item in self.ghosts:
            #item.draw(self.screen)
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
        #logic to turn off/on music
        '''
        if music class.is_playing:
            print("turning music off")
        else:
            print("turning music on")
        music class.is_playing = not music class.is_playing
        '''
        pass

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

'''     
    def prepare_scene(self):
        self.objects.append(Text(100, 100))
        self.objects.append(smallGrain(456, 100))
        self.objects.append(enegrizer(345, 435))


'''