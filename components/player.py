import pygame

class Spaceship(pygame.sprite.Sprite):
    """Sprite for player"""
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./images/player.png")
        self.rect = self.image.get_rect()
        self.centerx = self.rect.centerx
        self.centery = self.rect.centery

    def set_position(self, x, y):
        self.rect.x = x - self.centerx
        self.rect.y = y - self.centery

    def collide(self, sprites):
        for sprite in sprites:
            if pygame.sprite.collide_rect(self, sprite):
                return sprite

