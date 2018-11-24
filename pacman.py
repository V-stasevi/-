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

pac_right = "images/tmp_pacman_right.png"  # !! Временные картинки Пакмана. НУЖНО ЗАМЕНИТЬ
pac_left = "images/tmp_pacman_left.png"
pac_down = "images/tmp_pacman_down.png"
pac_up = "images/tmp_pacman_up.png"


class Pacman:
    def __init__(self):
        self.image = pygame.image.load(pac_right)
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
                self.image = pygame.image.load(pac_left)
            if event.key == pygame.K_d:
                self.direction = 0
                self.image = pygame.image.load(pac_right)
            if event.key == pygame.K_s:
                self.direction = 1
                self.image = pygame.image.load(pac_down)
            if event.key == pygame.K_w:
                self.direction = 3
                self.image = pygame.image.load(pac_up)

    def move(self):
        if self.direction == 0 and self.x+16 < WIDTH:
            self.x += 16                                   # !! Здесь также пока нет
        if self.direction == 1 and self.y+16 < HEIGHT:     # проверки на коллизию
            self.y += 16
        if self.direction == 2 and self.x > 0:
            self.x -= 16
        if self.direction == 3 and self.y > 0:
            self.y -= 16
        self.__update_system_position()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
