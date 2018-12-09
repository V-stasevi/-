import pygame
from constants import picGhost_Dead, up, right, down, left

common = True

class Ghost:
    def __init__(self, picture, x):
        self.image = picture
        self.normalState = picture
        self.rect = self.image.get_rect()
        self.x = x
        self.y = 15*16
        self.state = common
        self.direction = up
        self.__update_system_position()
        self.speed = 16
        self.dead = False
        self.startTime = pygame.time.get_ticks()

    def __update_system_position(self):
        self.rect.x = self.x
        self.rect.y = self.y

    def move(self):
        pass

    def check_border(self, window_width, window_height):
        pass

    def move_straight(self):
        self.__update_system_position()
        if self.direction == up:
            self.y -= self.speed
        elif self.direction == down:
            self.y += self.speed
        elif self.direction == right:
            self.x += self.speed
        elif self.direction == left:
            self.x -= self.speed

    def logic(self, window_width, window_height):
        self.__update_system_position()

    def is_dead(self):
        self.image = picGhost_Dead            #pacman.rect нужно нормльно привязать
        self.direction = up
        self.x = 15 * 16 - 16
        self.y = 15 * 16
        self.__update_system_position()


    def retcom(self):
        self.image = self.normalState

    def collision(self, pacman, score):
        if self.rect.colliderect(pacman.rect) and pacman.state == common:
            pacman.gameOver()

        if self.rect.colliderect(pacman.rect) and pacman.state != common:
            self.state = False
            score.addGhostPoints()
            self.is_dead()

        if pacman.state == common:
            self.state = common
            self.retcom()
