import pygame
import json
from screens import BaseScreen
from components import text


class GameOverScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.logo = text("Game Over", self.window, 400, 140, (255, 255, 255))
        self.score = text(f"{self.state['name']} Score: {self.state['score']}", self.window, 400, 250, (255, 255, 255))
        self.play_button = text("Press 'S' to play again ", self.window, 400, 350, (255, 255, 255))
        self.quit_button = text("Press 'Q' to Quit", self.window, 400, 400, (255, 255, 255))
        

        pygame.mouse.set_visible(True)
        self.write_json()

    def write_json(self):
        with open("./data/data.json", "r") as f:
            self.data = json.load(f)
        
        if self.state['name'] not in self.data.keys():
            self.data[self.state['name']] = []

        if len(self.data[self.state['name']]) == 0:
            self.data[self.state['name']].append(self.state['score'])
        else:
            self.data[self.state['name']] = [
                max(max(self.data[self.state['name']]), self.state['score']),
                self.state['score']
            ]
        
        with open("./data/data.json", "w") as f:
            json.dump(self.data, f)
            
    def manage_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                self.next_screen = "welcome"
                self.running = False
            elif event.key == pygame.K_q:
                self.running = False
                self.next_screen = False
