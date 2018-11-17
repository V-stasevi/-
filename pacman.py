import pygame
from constants import WIDTH, HEIGHT


class Pacman:
    def __init__(self):
        self.image = pygame.image.load("images/tmp_pacman.png")
        self.rect = self.image.get_rect()
        self.x = WIDTH/2 - 16
        self.y = HEIGHT/2 - 16
        self.__update_system_position()
        self.direction = 0              # 0 - > | 1 - v | 2 - < | 3 - ^
        # self.cash

    def __update_system_position(self):
        self.rect.x = self.x
        self.rect.y = self.y

    def check_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.direction = 2
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
            self.y += 16
            self.__update_system_position()
        if self.direction == 2 and self.x > 0:
            self.x -= 16
            self.__update_system_position()
        if self.direction == 3 and self.y > 0:
            self.y -= 16
            self.__update_system_position()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
