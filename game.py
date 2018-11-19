import pygame

from class_ghost import Ghost
from text import Text
from constants import SIZE, BLACK
from constants import picGhost_Blinky, picGhost_Clyde, picGhost_Inky, picGhost_Pinky

#from constants import picGhost_Blinky_Move, picGhost_Clyde_Move, picGhost_Inky_Move, picGhost_Pinky_Move, picGhost_Dead_Move,


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(SIZE)  # Установка размеров окна
        self.gameover = False
        self.objects = []
        self.prepare_scene()

        ghost_x = 30  # Изначальный х приведений
        self.Blinky = Ghost(picGhost_Blinky, ghost_x)      # добавление Блинки
        self.Clyde = Ghost(picGhost_Clyde, ghost_x + 30)   # добавление Клайда
        self.Inky = Ghost(picGhost_Inky, ghost_x + 60)     # добавление Инки
        self.Pinky = Ghost(picGhost_Pinky, ghost_x + 90)   # добавление Пинки
        self.ghosts = [self.Blinky, self.Clyde, self.Inky, self.Pinky]

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
        # for el in self.ghosts:
        #     el.move()

    def process_drawing(self):
        self.screen.fill(BLACK)  # Заливка цветом
        for i in self.objects:
            i.draw(self.screen)
        for item in self.ghosts:
            item.draw(self.screen)

        pygame.display.flip()  # Double buffering
