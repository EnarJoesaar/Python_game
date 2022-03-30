import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Kuuli klass"""
    def __init__(self, game_setting, screen, ship):
        """Kuuli asukoha init laeva juures"""
        super().__init__()
        self.screen = screen
        # kuuli tegemine
        self.rect = pygame.Rect(0, 0, game_setting.bullet_width, game_setting.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # kuuli asukoht
        self.y = float(self.rect.y)
        # kuuli sätted
        self.color = game_setting.bullet_color
        self.speed_factor = game_setting.bullet_speed_factor
    def update(self):
        """Kuuli asukoha uuendamine"""
        self.y -= self.speed_factor
        self.rect.y = self.y
    def draw_bullet(self):
        """Kuuli asukoha tegmeine ekraanil"""
        pygame.draw.rect(self.screen, self.color, self.rect)