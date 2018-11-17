"""

    Класс Pacman
---------------------

 - Пока что сделано только отображение на пустом поле
 - Временная реализация движения

 ВАЖНО: движение по реализовано по ячейкам из
        предположения, что одна ячейка имеет
        размеры 16х16 пикселей. Это, возможно,
        не окончательный вариант перемещения,
        т.к. я пока точно не знаю, как одно
        должно реализовываться

--------------------

"""

import pygame
from constants import WIDTH, HEIGHT

filename = "images/tmp_pacman.png"  # !! Временная картинка Пакмана. НУЖНО ЗАМЕНИТЬ


class Pacman:
    def __init__(self):
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()
        self.x = WIDTH/2 - 16
        self.y = HEIGHT/2 - 16
        self.__update_system_position()
        self.direction = 0      # 0 - > | 1 - v | 2 - < | 3 - ^  -- направления движения
        # self.cash - заготовка для кеширования направления движения

    def __update_system_position(self):
        self.rect.x = self.x
        self.rect.y = self.y

    def check_event(self, event):
        if event.type == pygame.KEYDOWN:        # !! Здесь ещё нет проверки на возможные
            if event.key == pygame.K_a:         # пересечения с другими объектами, т.к.
                self.direction = 2              # их классов ещё нет
            if event.key == pygame.K_d:
                self.direction = 0
            if event.key == pygame.K_s:
                self.direction = 1
            if event.key == pygame.K_w:
                self.direction = 3

    def move(self):
        if self.direction == 0 and self.x+16 < WIDTH:
            self.x += 16
            self.__update_system_position()
        if self.direction == 1 and self.y+16 < HEIGHT:
            self.y += 16                                # !! Здесь также пока нет
            self.__update_system_position()             # проверки на коллизию
        if self.direction == 2 and self.x > 0:
            self.x -= 16
            self.__update_system_position()
        if self.direction == 3 and self.y > 0:
            self.y -= 16
            self.__update_system_position()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
