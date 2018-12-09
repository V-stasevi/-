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
from constants import WIDTH_B as WIDTH, HEIGHT_B as HEIGHT, MATRIX, pacman_down, pacman_left, pacman_right, pacman_up
from text import Text

pac_right =  pacman_right # !! Временные картинки Пакмана. НУЖНО ЗАМЕНИТЬ
pac_left = pacman_left
pac_down = pacman_down
pac_up = pacman_up
common = True
fear = False


class Pacman:
    def __init__(self, mat, sounds):
        self.image = pacman_right
        self.rect = self.image.get_rect()
        self.x = 14*16+2
        self.y = 12*16
        self.__update_system_position()
        self.direction = 0      # 0 - > | 1 - v | 2 - < | 3 - ^  -- направления движения
        self.cash = 3
        self.state = common
        self.matrix = mat
        self.sounds = sounds

        self.isGameOver = False
        self.textGameOver = Text(WIDTH//4, 16*14, "GAME OVER", size=52, color=(255, 0, 255))

        self.startTime = None

    def __update_system_position(self):
        self.rect.x = self.x
        self.rect.y = self.y

    def check_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                if MATRIX[int(self.y//16)][int(self.x//16)-1] != 0:
                    self.cash = 2
                else:
                    self.direction = self.cash = 2
                    self.image = pacman_left
            if event.key == pygame.K_d:
                if MATRIX[int(self.y//16)][int(self.x//16)+1] != 0:
                    self.cash = 0
                else:
                    self.direction = self.cash = 0
                    self.image = pacman_right
            if event.key == pygame.K_s:
                if MATRIX[int(self.y//16)+1][int(self.x//16)] != 0:
                    self.cash = 1
                else:
                    self.direction = self.cash = 1
                    self.image = pacman_down
            if event.key == pygame.K_w:
                if MATRIX[int(self.y//16)-1][int(self.x//16)] != 0:
                    self.cash = 3
                else:
                    self.direction = self.cash = 3
                    self.image = pacman_up

    def check_cash(self):
        if self.cash == 0 and self.direction != 2 and MATRIX[int(self.y//16)][int(self.x//16)+1] == 0:
            self.direction = 0
            self.image = pacman_right
        if self.cash == 1 and self.direction != 3 and MATRIX[int(self.y//16)+1][int(self.x//16)] == 0:
            self.direction = 1
            self.image = pacman_down
        if self.cash == 2 and self.direction != 0 and MATRIX[int(self.y//16)][int(self.x//16)-1] == 0:
            self.direction = 2
            self.image = pacman_left
        if self.cash == 3 and self.direction != 1 and MATRIX[int(self.y//16)-1][int(self.x//16)] == 0:
            self.direction = 3
            self.image = pacman_up

    def move(self):
        if self.direction == 0 and self.x+16 < WIDTH and MATRIX[int(self.y//16)][int(self.x//16)+1] == 0:
            self.x += 16
        if self.direction == 0 and self.y//16 == 14 and self.x//16 == 27:
            self.x = -16
            self.y = 16*14

        if self.direction == 1 and self.y+16 < HEIGHT and MATRIX[int(self.y//16)+1][int(self.x//16)] == 0:
            self.y += 16

        if self.direction == 2 and self.x > 0 and MATRIX[int(self.y//16)][int(self.x//16)-1] == 0:
            self.x -= 16
        if self.direction == 2 and self.y//16 == 14 and self.x//16 == 0:
            self.x = 27*16
            self.y = 16*14

        if self.direction == 3 and self.y > 0 and MATRIX[int(self.y//16)-1][int(self.x//16)] == 0:
            self.y -= 16

    def eatGrain(self, score):
        if self.matrix[self.y//16][self.x//16].grain.isEaten is False:
            self.matrix[self.y//16][self.x//16].grain.isEaten = True
            if score.count != 300:
                score.logic()
                self.sounds.playEatSeedSound()

        if self.matrix[self.y//16][self.x//16].isFruit is True:
            if self.matrix[self.y // 16][self.x // 16].cherry.is_eaten is False:
                self.matrix[self.y // 16][self.x // 16].cherry.is_eaten = True
                score.points += 50

        if self.matrix[self.y//16][self.x//16].isBig is True:
            if self.matrix[self.y // 16][self.x // 16].energizer.is_eaten is False:
                self.matrix[self.y // 16][self.x // 16].energizer.is_eaten = True
                score.points += 50
                self.state = fear
                self.startTime = pygame.time.get_ticks()

    def checkTime(self):
        if self.state == fear:
            if (pygame.time.get_ticks() - self.startTime) // 1000 >= 5:
                self.state = common


    def logic(self, score):
        self.check_cash()
        self.move()
        self.eatGrain(score)
        self.checkTime()
        self.__update_system_position()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        if self.isGameOver:
            self.textGameOver.draw(screen)

    def is_dead(self):
        self.x = 14*16+2
        self.y = 15*16
        self.__update_system_position()
        self.direction = 0

    def gameOver(self):
        self.isGameOver = True
