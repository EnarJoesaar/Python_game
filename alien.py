import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Klass tulnuka kirjeldamiseks"""
    def __init__(self, game_settings, screen):
        """Tulnuka objekti init ja selle asukoha määramine"""
        super().__init__()
        self.screen = screen
        self.game_settings = game_settings
        # tulnuka pildi laadimine ja selle atribuut
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # tulnuka asukohga määramine
        self.x = float(self.rect.x)
    def blitme(self):
        """Tulnuka tema asukohta panemine"""
        self.screen.blit(self.image, self.rect)
    def update(self):
        """Tulnuka asukoha paremale ja vasakule liigutamine"""
        self.x += self.game_settings.alien_speed_factor * self.game_settings.fleet_direction
        self.rect.x = self.x
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True