import sys

import pygame

from bullet import Bullet


def check_events(ai, screen, ship, bullets):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)




def check_keydown_events(event, ai, screen, ship, bullets):

    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(ai, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event,ship):

    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(bg_colour, screen, ship, bullets):
    for bullet in bullets.sprites():
       bullet.draw_bullet()
    screen.fill(bg_colour)
    ship.blitime()
    pygame.display.flip()  # refreshing screen