import pygame
from start3 import Start_screen, WIDTH, HEIGHT
import pygame
import requests
import sys
import os


class MapParams(object, coord, scale):
    def __init__(self):
        self.lat = coord[0]
        self.lon = coord[1]
        self.zoom = scale
        self.type = "map"

    def ll(self):
        return str(self.lon) + "," + str(self.lat)


def load_map(mp):
    map_request = "http://static-maps.yandex.ru/1.x/?ll={ll}&z={z}&l={type}".format(ll=mp.ll(), z=mp.zoom,
                                                                                    type=mp.type)
    response = requests.get(map_request)
    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    # Запись полученного изображения в файл.
    map_file = "map.png"
    try:
        with open(map_file, "wb") as file:
            file.write(response.content)
    except IOError as ex:
        print("Ошибка записи временного файла:", ex)
        sys.exit(2)
    return map_file


def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    mp = MapParams()
    running = True
    while running:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            running = False
        map_file = load_map(mp)
        screen.blit(pygame.image.load(map_file), (0, 0))
        pygame.display.flip()
    pygame.quit()
    os.remove(map_file)



if __name__ == '__main__':
    pygame.init()
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    background_color = 'white'
    fps = 60

    start_screen = Start_screen(screen)


    running = True
    start_screen_flag = True

    while start_screen_flag:  # цикл стартового экрана
        # обработка событий
        for event in pygame.event.get():
            if start_screen.coord.handle_event(event) or start_screen.start_button.handle_event(event) or \
                    start_screen.scale.handle_event(event):
                start_screen_flag = False
            if event.type == pygame.QUIT:
                pygame.quit()

            start_screen.coord.update()
            start_screen.scale.update()
            start_screen.hello()
            start_screen.coord.draw(screen)
            start_screen.scale.draw(screen)
            start_screen.start_button.draw(screen)

        pygame.display.flip()
        clock.tick(fps)

    map = MapParams(start_screen.coord.text, start_screen.scale.text)
