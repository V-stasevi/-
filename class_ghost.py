import pygame
from constants import picGhost_Dead, up, right, down, left
from pacman import Pacman

common = True

class Ghost:
    def __init__(self, picture, x):
        self.image = picture
        self.rect = self.image.get_rect()
        self.x = x
        self.y = 15*16
        self.state = common
        self.direction = up
        self.__update_system_position()
        self.speed = 16
        self.dead = False

    def __update_system_position(self):
        self.rect.x = self.x
        self.rect.y = self.y

    def start(self):
        self.y -= self.speed

    def move(self):
        pass

    def check_border(self, window_width, window_height):
        pass

    def move_straight(self):
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
        self.image = pygame.image.load(picGhost_Dead)
        if self.rect.colliderect(Pacman.rect) and self.state != common:            #pacman.rect нужно нормльно привязать
            self.direction = up
            self.x = 15 * 16 - 16
            self.y = 15 * 16
            self.__update_system_position()

    # def collision(self, image):
    #     if self.rect.colliderect(Pacman.rect) and Pacman.state == common:
    #         pass
    #         where pacman dies
    #         or
    #         dies ghost: self.is_dead()
    #         self.image = image()

    def collosion(self):
        if self.rect.colliderect(Pacman.rect) and self.state == common:
            Pacman.is_dead()                                                    #pacman.rect и pacman.is_dead!