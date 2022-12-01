import pygame
import random
from .bomb import Bomb

class BombGroup(pygame.sprite.Group):
    """Bomb skill will be saved to this sprite group"""
    def __init__(self, x_bomb=random.randint(30, 770), y_bomb=random.randint(30, 570)):
        super().__init__()
        bomb = Bomb(x=x_bomb, y=y_bomb)
        
        self.add(bomb)