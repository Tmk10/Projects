import pygame


def run():
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    print(screen.get_rect())
    a = pygame.Rect((10, 10), (10, 10))

    while True:

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                a.move(10, 10)
                pygame.draw.rect(screen, (255, 255, 255), a)
                pygame.display.update()


run()
