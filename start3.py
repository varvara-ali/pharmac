import pygame
from input import InputBox, Button


WIDTH = 800
HEIGHT = 1000


def show_text(screen: pygame.Surface,
              text: list,
              x: int, y: int,
              font_size: int = 30,
              font_color: pygame.Color = pygame.Color('#776e65')):
    font = pygame.font.Font(None, font_size)
    text_coord = y
    for line in text:
        string_rendered = font.render(line, True, font_color)
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = x
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)


class Start_screen:
    def __init__(self, screen):
        self.screen = screen
        self.coord = InputBox(270, 300, 140, 32)
        self.scale = InputBox(270, 350, 140, 32)
        self.start_button = Button(300, 450, 140, 32, 'Начать')

    def hello(self):
        intro_text = ["",
                      "Введите координаты и масштаб карты "]
        coord_input = ['Введите координаты:']
        scale_input = ['Введите масштаб:']
        self.screen.fill(pygame.Color("#faf8ef"))
        show_text(self.screen, intro_text, 50, 60)
        show_text(self.screen, coord_input, 40, 300, 30, pygame.Color('#550055'))
        show_text(self.screen, scale_input, 40, 350, 30, pygame.Color('#550055'))

