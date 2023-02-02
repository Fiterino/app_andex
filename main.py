import os

import pygame
from mapapi_PG import show_map

pygame.init()
SIZE = WIDTH, HEIGHT = 500, 500


def game():
    running = True
    screen = pygame.display.set_mode(SIZE)
    ll, span = f'43.141580551356746,51.5570779896406', '0.001,0.001'
    map_file = show_map(f'll={ll}&spn={span}')
    pygame.display.set_caption('Большая задача по Maps API. Часть №1')
    screen.blit(pygame.image.load('map.png'), (0, 0))
    pygame.display.flip()
    while running:
        map_file = show_map(f'll={ll}&spn={span}')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_PAGEUP:
                    print(1)
                if event.key == pygame.K_PAGEDOWN:
                    print(2)
        screen.blit(pygame.image.load('map.png'), (0, 0))
        pygame.display.flip()
    pygame.quit()
    os.remove(map_file)


if __name__ == '__main__':
    game()






