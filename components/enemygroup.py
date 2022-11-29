import pygame
from .enemy import Enemy

class EnemyGroup(pygame.sprite.Group):
    def __init__(self, x_pos, y_pos, h_speed, v_speed):
        super().__init__()
        enemy = Enemy(xpos=x_pos, ypos=y_pos, horizontal_speed=h_speed, vertical_speed=v_speed)

        self.add(enemy)