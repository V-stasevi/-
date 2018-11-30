from button  import ImageButton, Button
import pygame
from constants import HEIGHT, WIDTH, SIZE, BLACK, YELLOW, BUTTON_STYLE


class ButtonControl:

    image = "button/pacman-back.png"

    def __init__(self, surface, functions_dict):
        self.parent_surface = surface
        self.control_screen = pygame.Surface(SIZE)
        self.waiting = True
        self.set_b = ImageButton(5, 5, self.main_loop, self.dismiss_view)

        self.buttons = []
        self.buttons_func_dict = functions_dict

        #background image
        self.image = pygame.image.load(self.image)
        self.image = pygame.transform.scale(self.image, (737, 193))
        self.image_rect = self.image.get_rect()
        self.image_rect.centerx = WIDTH // 2
        self.image_rect.y = HEIGHT - self.image_rect.h - 40


    def prepare_screen(self):
        self.buttons = self._append_buttons()



    def draw(self, surface):
        self.control_screen.fill((BLACK))

        for i in range(len(self.buttons)):
            self.buttons[i].update(self.control_screen)

        self.control_screen.blit(self.image, self.image_rect)
        self.parent_surface.blit(self.control_screen, (0, 0))
        self.draw_control_button()

        pygame.display.flip()


    def draw_control_button(self):
        self.set_b.update(self.parent_surface)

    def process_logic(self):
        pass

    def process_event(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.set_b.check_event(event)

                for i in range(len(self.buttons)):
                    self.buttons[i].check_event(event)


    def main_loop(self):
        self.prepare_screen()
        while self.waiting:
            self.process_event()
            self.process_logic()
            self.draw(self.parent_surface)

        self.waiting = True


    def dismiss_view(self):
        self.waiting = False


    def check_control_button_event(self, event):
        self.set_b.check_event(event)

    def _append_buttons(self):
        button_w = 150
        button_h = 40
        button_x = WIDTH // 2 - button_w // 2
        button_y = 75
        button_rect = pygame.Rect(button_x, button_y, button_w, button_h)
        button_color = YELLOW

        titles_on = ["Sound OFF", "Level 1","Level 2","Level 3", "Clear Records"]
        titles_off = ["Sound ON",  "Level 1","Level 2","Level 3", "Clear Records"]
        return_values = [None, 1, 2, 3, None]

        functions = [self.buttons_func_dict["sound_control"],
                     self.buttons_func_dict["level_control"],
                     self.buttons_func_dict["level_control"],
                     self.buttons_func_dict["level_control"],
                     self.buttons_func_dict["records_control"]
                     ]

        for i in range(len(functions)):
            button = Button(button_rect, button_color, return_values[i], functions[i], text=titles_on[i],text2=titles_off[i], **BUTTON_STYLE)
            self.buttons.append(button)
            button_y += 50
            button_rect = pygame.Rect(button_x, button_y, button_w, button_h)

        return self.buttons

