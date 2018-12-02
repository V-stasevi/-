import pygame

from class_ghost import Ghost
from text import Text
from constants import SIZE, BLACK
from constants import picGhost_Clyde, picGhost_Inky
from pacman import Pacman
from field import Field
from blinky import Blinky
from pinky import Pinky

from Grains import smallGrain, enegrizer


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(SIZE)
        self.gameover = False
        self.objects = []
        #self.prepare_scene()
        self.pacman = Pacman()
        self.field = Field(0, 0, 15)

        ghost_x = 30  # Изначальный х приведений
        self.Blinky = Blinky(self.pacman)   # добавление Блинки
        self.Clyde = Ghost(picGhost_Clyde, ghost_x + 30)   # добавление Клайда
        self.Inky = Ghost(picGhost_Inky, ghost_x + 60)     # добавление Инки
        self.Pinky = Pinky(self.pacman)   # добавление Пинки
        self.ghosts = [self.Blinky, self.Clyde, self.Inky, self.Pinky]

    def main_loop(self):
        while not self.gameover:
            self.process_events()
            self.process_logic()
            self.process_drawing()
            pygame.time.wait(150)

    def process_events(self):
        for event in pygame.event.get():  # Получение всех событий
            if event.type == pygame.QUIT:  # Событие выхода
                self.gameover = True
            self.pacman.check_event(event)

    def process_logic(self):
        self.pacman.logic()
        self.Blinky.move()
        self.Pinky.move()

    def process_drawing(self):
        self.screen.fill(BLACK)
        self.field.draw(self.screen)
        self.pacman.draw(self.screen)
        self.Blinky.draw(self.screen)
        self.Pinky.draw(self.screen)
        pygame.display.flip()

    def pacman_rect(self):
        return self.pacman.rect
'''     
    def prepare_scene(self):
        self.objects.append(Text(100, 100))
        self.objects.append(smallGrain(456, 100))
        self.objects.append(enegrizer(345, 435))


'''