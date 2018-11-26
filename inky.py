import pygame
import math
from constants import MATRIX,WIDTH,HEIGHT

inky_pic = "images/tmp_pacman_down.png"


def dist(cur_x,cur_y, dist_x, dist_y):
    return math.sqrt(pow(cur_x - dist_x, 2) + pow(cur_y - dist_y, 2))//16
''',pacman_x,pacman_y'''
class Inky:
    def __init__(self):
        self.image = pygame.image.load(inky_pic)
        self.rect = self.image.get_rect()
        self.x = 256
        self.y = 176
        #self.pacman_x = pacman_x
        #self.pacman_y = pacman_y
        self.__update_system_position()
        self.direction = 0   # 0 - > | 1 - v | 2 - < | 3 - ^  -- направления движения

    def __update_system_position(self):
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def logic(self):
        if self.cross():
            self.choose_way(416,464)
        self.move()
        self.__update_system_position()

    def cross(self):
        count = 0
        if MATRIX[int(self.y / 16) - 1][int(self.x / 16)] == 0:
            count += 1
        if MATRIX[int(self.y / 16) + 1][int(self.x / 16)] == 0:
            count += 1
        if MATRIX[int(self.y / 16)][int(self.x / 16) - 1] == 0:
            count += 1
        if MATRIX[int(self.y / 16)][int(self.x / 16) - 1] == 0:
            count += 1
        return True if count > 2 else False

    def choose_way(self,dist_x,dist_y):
        pairs = dict()
        if self.y-16 < HEIGHT and MATRIX[int(self.y/16)-1][int(self.x/16)] == 0: #going up
            pairs['3'] = dist(self.x, self.y-16, dist_x, dist_y)

        if self.y + 16 > 0 and MATRIX[int(self.y/16)+1][int(self.x/16)] == 0: #going down
            pairs['1'] = dist(self.x, self.y+16, dist_x, dist_y)

        if self.x - 16 > 0 and MATRIX[int(self.y/16)][int(self.x/16)-1] == 0: #going left
            pairs['2'] = dist(self.x-16, self.y, dist_x, dist_y)

        if self.x + 16 < WIDTH and MATRIX[int(self.y/16)][int(self.x/16)+1] == 0: #going right
            pairs['0'] = dist(self.x+16, self.y, dist_x, dist_y)
        minv = min(pairs.values())
        for dir, length in pairs.items():
            if length == minv:
                self.direction = int(dir)
                break

    '''def turn(self):
        if MATRIX[int(self.y/16)][int(self.x/16)+1] == 0 and self.direction != 0:
            self.direction = 0
            self.x += 16
        if MATRIX[int(self.y/16)+1][int(self.x/16)] == 0 and self.direction != 1:
            self.direction = 1
            self.y += 16
        if MATRIX[int(self.y/16)][int(self.x/16)-1] == 0 and self.direction != 2:
            self.direction = 2
            self.x -= 16
        if MATRIX[int(self.y/16)-1][int(self.x/16)] == 0 and self.direction != 3:
            self.direction = 3
            self.y -= 16
        print("turned - {}. At {}, {}".format(self.direction, self.x//16, self.y//16))'''

    def move(self):
        if self.direction == 0 and self.x+16 < WIDTH and MATRIX[int(self.y/16)][int(self.x/16)+1] == 0:
            self.x += 16
        '''elif MATRIX[int(self.y/16)][int(self.x/16)+1] == 1 and not self.cross():
            self.turn()'''

        if self.direction == 1 and self.y+16 < HEIGHT and MATRIX[int(self.y/16)+1][int(self.x/16)] == 0:
            self.y += 16
        '''elif MATRIX[int(self.y/16)+1][int(self.x/16)] == 1 and not self.cross():
            self.turn()'''

        if self.direction == 2 and self.x > 0 and MATRIX[int(self.y/16)][int(self.x/16)-1] == 0:
            self.x -= 16
        '''elif MATRIX[int(self.y/16)][int(self.x/16)-1] == 1 and not self.cross():
            self.turn()'''

        if self.direction == 3 and self.y > 0 and MATRIX[int(self.y/16)-1][int(self.x/16)] == 0:
            self.y -= 16
        '''elif MATRIX[int(self.y/16)-1][int(self.x/16)] == 1 and not self.cross():
            self.turn()'''
