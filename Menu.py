import pygame
import constants as cm
import button

class Menu:
    def __init__(self, screen, pic_play, pic_records, pic_options, pic_bg, playFunc, recFunc, opFunc):
        self.play = button.Button(screen, pic_play, cm.x_play, cm.y_play, "play", playFunc)
        self.records = button.Button(screen, pic_records, cm.x_records, cm.y_records, "rec", recFunc)
        self.options = button.Button(screen, pic_options, cm.x_options, cm.y_options, "opt", opFunc)
        self.backgrond = pygame.image.load(pic_bg)
        self.bg_rec = self.backgrond.get_rect()
        self.screen = screen

    def events(self, event):
        self.play.action(event)
        self.records.action(event)
        self.options.action(event)

    def draw(self, screen):
        screen.blit(self.backgrond, self.bg_rec)
        self.play.draw(screen)
        self.records.draw(screen)
        self.options.draw(screen)