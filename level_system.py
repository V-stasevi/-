import pygame
from settings_control  import _append_buttons

class level_system:


    def __init__(self, _append_buttons):
        self.speps=0;
        self.level= _append_buttons;    # неуверен ту ли функцию подключил, но другой не нашёл
    
    
    def speed(self):            # Вроде функция должа возращать скорость перемещения
        if self.level== 1:
            self.speeds= 10
            return self.speeds
        elif self.level== 2:
            self.speeds= 20
            return self.speeds
        elif self.level== 3:
            self.speeds= 30
            return self.speeds
        
        