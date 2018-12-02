import pygame

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
        #self.prepare_scene()
        self.pacman = Pacman()
        self.field = Field(0, 0, 15)
        self.menu = Menu.Menu(self.screen, cm.pic_play, cm.pic_records, cm.pic_options, cm.pic_bg, self.runGame, self.showScore, self.showOption)
        '''
        ghost_x = 30  # Изначальный х приведений
        self.Blinky = Ghost(picGhost_Blinky, ghost_x)      # добавление Блинки
        self.Clyde = Ghost(picGhost_Clyde, ghost_x + 30)   # добавление Клайда
        self.Inky = Ghost(picGhost_Inky, ghost_x + 60)     # добавление Инки
        self.Pinky = Ghost(picGhost_Pinky, ghost_x + 90)   # добавление Пинки
        self.ghosts = [self.Blinky, self.Clyde, self.Inky, self.Pinky]'''

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
        print("show score")

    def showOption(self):
        print("show option")

'''     
    def prepare_scene(self):
        self.objects.append(Text(100, 100))
        self.objects.append(smallGrain(456, 100))
        self.objects.append(enegrizer(345, 435))


'''