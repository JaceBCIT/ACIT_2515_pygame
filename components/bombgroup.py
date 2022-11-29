import pygame
from .bomb import Bomb

class BombGroup(pygame.sprite.Group):
    def __init__(self, x_bomb, y_bomb):
        super().__init__()
        bomb = Bomb(x=x_bomb, y=y_bomb)
        
        self.add(bomb)