import pygame
from mapapi_PG import show_map

pygame.init()
SIZE = WIDTH, HEIGHT = 500, 500


def game():
    running = True
    while running:
        for event in pygame.event.get():
            ll, span = '43.141580551356746,51.5570779896406', '0.001,0.001'
            show_map(f'll={ll}&spn={span}')
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    game()






