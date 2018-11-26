"""

    Класс Pacman
---------------------

 - Сдеано отображение на поле со стенами
 - Реализовано полноценное движение (+ его CASH)

 ВАЖНО: движение по реализовано по ячейкам из
        предположения, что одна ячейка имеет
        размеры 16х16 пикселей. Это, возможно,
        не окончательный вариант перемещения,
        т.к. я пока точно не знаю, как одно
        должно реализовываться

--------------------

"""

import pygame
from constants import WIDTH, HEIGHT, MATRIX

pac_right = "pac-img.png"  # !! Временные картинки Пакмана. НУЖНО ЗАМЕНИТЬ
pac_left = "pac-img.png"
pac_down = "pac-img.png"
pac_up = "pac-img.png"


class Pacman:
    def __init__(self):
        self.image = pygame.image.load(pac_right)
        self.rect = self.image.get_rect()
        self.x = 14*16+2
        self.y = 15*16
        self.__update_system_position()
        self.direction = 0      # 0 - > | 1 - v | 2 - < | 3 - ^  -- направления движения
        self.cash = 3

    def __update_system_position(self):
        self.rect.x = self.x
        self.rect.y = self.y

    def check_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                if MATRIX[int(self.y/16)][int(self.x/16)-1] != 0:
                    self.cash = 2
                else:
                    self.direction = self.cash = 2
                    self.image = pygame.image.load(pac_left)
            if event.key == pygame.K_d:
                if MATRIX[int(self.y/16)][int(self.x/16)+1] != 0:
                    self.cash = 0
                else:
                    self.direction = self.cash = 0
                    self.image = pygame.image.load(pac_right)
            if event.key == pygame.K_s:
                if MATRIX[int(self.y/16)+1][int(self.x/16)] != 0:
                    self.cash = 1
                else:
                    self.direction = self.cash = 1
                    self.image = pygame.image.load(pac_down)
            if event.key == pygame.K_w:
                if MATRIX[int(self.y/16)-1][int(self.x/16)] != 0:
                    self.cash = 3
                else:
                    self.direction = self.cash = 3
                    self.image = pygame.image.load(pac_up)

    def check_cash(self):
        if self.cash == 0 and self.direction != 2 and MATRIX[int(self.y/16)][int(self.x/16)+1] == 0:
            self.direction = 0
            self.image = pygame.image.load(pac_right)
        if self.cash == 1 and self.direction != 3 and MATRIX[int(self.y/16)+1][int(self.x/16)] == 0:
            self.direction = 1
            self.image = pygame.image.load(pac_down)
        if self.cash == 2 and self.direction != 0 and MATRIX[int(self.y/16)][int(self.x/16)-1] == 0:
            self.direction = 2
            self.image = pygame.image.load(pac_left)
        if self.cash == 3 and self.direction != 1 and MATRIX[int(self.y/16)-1][int(self.x/16)] == 0:
            self.direction = 3
            self.image = pygame.image.load(pac_up)

    def move(self):
        print(self.y/16, self.x/16)
        if self.direction == 0 and self.x+16 < WIDTH and MATRIX[int(self.y/16)][int(self.x/16)+1] == 0:
            self.x += 16
        if self.direction == 0 and self.y/16 == 14 and self.x/16 == 27:
            self.x = -16
            self.y = 16*14

        if self.direction == 1 and self.y+16 < HEIGHT and MATRIX[int(self.y/16)+1][int(self.x/16)] == 0:
            self.y += 16

        if self.direction == 2 and self.x > 0 and MATRIX[int(self.y/16)][int(self.x/16)-1] == 0:
            self.x -= 16
        if self.direction == 2 and self.y/16 == 14 and (self.x-2)/16 == 0:
            self.x = 27*16
            self.y = 16*14

        if self.direction == 3 and self.y > 0 and MATRIX[int(self.y/16)-1][int(self.x/16)] == 0:
            self.y -= 16

    def logic(self):
        self.check_cash()
        self.move()
        self.__update_system_position()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
