import pygame
import requests
import sys
import os
from start3 import Start_screen


class MapParams(object):
    def __init__(self):
        self.lat = 61.665279
        self.lon = 50.813492
        self.zoom = 16
        self.type = "map"

    def ll(self):
        return str(self.lon) + "," + str(self.lat)


def load_map(mp):
    map_request = "http://static-maps.yandex.ru/1.x/?ll={ll}&z={z}&l={type}".format(ll=mp.ll(), z=mp.zoom, type=mp.type)
    response = requests.get(map_request)
    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

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
    screen = pygame.display.set_mode(800, 1000)
    clock = pygame.time.Clock()

    background_color = 'white'
    fps = 60

    mp = MapParams()
    running = True
    while running:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            running = False
        # Создаем файл
        map_file = load_map(mp)
        screen.blit(pygame.image.load(map_file), (0, 0))
        pygame.display.flip()
    pygame.quit()
    os.remove(map_file)

    start_screen_flag = True

    while start_screen_flag:  # цикл стартового экрана
        # обработка событий
        for event in pygame.event.get():
            if start3.coord.handle_event(event) or start3.start_button.handle_event(event) \
                    or start3.scale.handle_event(event):
                start_screen_flag = False
            if event.type == pygame.QUIT:
                pygame.quit()

            start3.name.update()
            start3.hello()
            start3.name.draw(screen)
            start3.start_button.draw(screen)

        pygame.display.flip()
        clock.tick(fps)


if __name__ == "__main__":
    main()