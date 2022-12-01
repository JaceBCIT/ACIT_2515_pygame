import pygame
import math
import random
import time
from screens import BaseScreen
from components import Spaceship, Bomb, BombGroup, setup, text


class GameScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.score = 0
        self.background = pygame.image.load("./images/background.png")
        self.min_enemy_speed = 1
        self.max_enemy_speed = 1
        self.occur_enemies = 1
        self.occur_prob = 15
        self.bomb_count = 1
        self.start_time = pygame.time.get_ticks()

        self.player = Spaceship()
        self.bomb = Bomb(random.randint(30, 770), random.randint(30, 570))
        self.bombs = BombGroup()
        self.enemies = pygame.sprite.Group()

        pygame.mouse.set_visible(False)
        self.player.set_position(*pygame.mouse.get_pos())
    
    def backgrounds(self, background):
        bg_rect = background.get_rect()
        for i in range(int(math.ceil(800 / bg_rect.width))):
            for j in range(int(math.ceil(600 / bg_rect.height))):
                self.window.blit(background, pygame.Rect(i * bg_rect.width, j * bg_rect.height, bg_rect.width, bg_rect.height))
    
    def update(self):
        now = pygame.time.get_ticks()
        time = round(((now - self.start_time) / 1000), 1)
        self.occur_enemies = 1 + int(time / 40)
        self.min_enemy_speed = 1 + int(time / 20)
        self.max_enemy_speed = 1 + int(time / 10)
        #self.occur_enemies = 1 + int(self.score / 500)
        #self.min_enemy_speed = 1 + int(self.score / 400)
        #self.max_enemy_speed = 1 + int(self.score / 300)
        self.backgrounds(self.background)

        if random.randint(1, self.occur_prob) == 1:
            for i in range(self.occur_enemies):
                self.enemies.add(setup(random.randint(self.min_enemy_speed, self.max_enemy_speed)))
                self.score += 1
            
            if random.randint(1, self.occur_prob * 10) == 1:
                self.bomb
                self.bombs.add(self.bomb)
                

        text('Score: {}'.format(self.score), self.window, 80, 20, (255, 255, 255))
        text('Bombs: {}'.format(self.bomb_count), self.window, 700, 20, (255, 255, 255))
        text('Aliens: {}'.format(len(self.enemies)), self.window, 400, 20, (255, 255, 255))
        #text('Timer: {}'.format(round((now - self.start_time) / 1000), 1), self.window, 400, 50, (255, 255, 255))

        self.enemies.update()
        self.bombs.update()
        self.enemies.draw(self.window)
        self.bombs.draw(self.window)
        

        if self.player.collide(self.enemies):
            self.enemies.empty()
            self.running = False
            self.next_screen = 'game_over'
            self.state["score"] = self.score
        elif self.player.collide(self.bombs):
            self.bomb_count += 1
            self.bombs.empty()

        self.window.blit(self.player.image, self.player.rect)

    def manage_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_pos[0] <= 10:
                pygame.mouse.set_pos(790, mouse_pos[1])
            elif mouse_pos[0] >= 790:
                pygame.mouse.set_pos(10, mouse_pos[1])
            elif mouse_pos[1] <= 10:
                pygame.mouse.set_pos(mouse_pos[0], 590)
            elif mouse_pos[1] >= 590:
                pygame.mouse.set_pos(mouse_pos[0], 10)
            self.player.set_position(*mouse_pos)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.bomb_count > 0:
                self.bomb_count -= 1
                time.sleep(1)
                self.enemies.empty()