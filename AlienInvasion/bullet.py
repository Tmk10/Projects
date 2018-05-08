import pygame

from pygame.sprite import Sprite # Sprite used for grouping elements and making action on whole group

class Bullet(Sprite):

    def __init__(self, ai, screen, ship):
        super(Bullet,self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0,0,ai.bullet_width, ai.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        self.color = ai.bullet_colour
        self.speed_factor = ai.bullet_speed_factor

    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
