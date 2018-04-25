

import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    start = True
    ai = Settings()
    pygame.init()
    screen = pygame.display.set_mode((ai.screen_width, ai.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai, screen)
    bullets = Group()

    while True:
        ship.update()
        bullets.update()
        gf.check_events(ai, screen, ship, bullets)
        gf.update_screen(ai.bg_colour, screen, ship, bullets)



run_game()