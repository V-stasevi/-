import pygame as pg
import functions_menu as f

class Button:
    def __init__(self, screen, name, x, y, b_name, func):
        self.picture = pg.image.load(name)
        self.pic_rec = self.picture.get_rect()
        self.pic_rec.centerx, self.pic_rec.centery = x, y
        self.button = b_name
        self.funcToDo = func

    def action(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            pos_x = self.pic_rec.x
            pos_y = self.pic_rec.y
            xm, ym = pg.mouse.get_pos()
            if (pos_x <= xm <= pos_x + self.pic_rec.width) and (
                    pos_y <= ym <= pos_y + self.pic_rec.height):
                f.b_function(self.button, self.funcToDo)

    def draw(self, screen):
        screen.blit(self.picture, self.pic_rec)

    def update_coordinates(self, new_x, new_y):
        self.x = new_x
        self.y = new_y