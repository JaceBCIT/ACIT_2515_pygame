import pygame

class Bomb(pygame.sprite.Sprite):
    def __init__(self, x, y):
        """Class for in-game Bomb skill sprite"""
        super(Bomb, self).__init__()
        self.image = pygame.image.load("./images/bomb.png")
        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.centerx
        self.rect.y = y - self.rect.centery
