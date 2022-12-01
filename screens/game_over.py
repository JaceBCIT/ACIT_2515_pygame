import pygame
import json
import webbrowser
from screens import BaseScreen
from components import text
from subprocess import Popen


class GameOverScreen(BaseScreen):
    """Class for game over screen"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.logo = text("Game Over", self.window, 400, 140, (102, 0, 204))
        self.score = text(f"{self.state['name']}'s Score: {self.state['score']}", self.window, 400, 250, (255, 255, 154))
        self.play_button = text("Press 'S' to play again ", self.window, 400, 350, (255, 255, 255))
        self.web = text("Press 'P' to View Scores Online", self.window, 400, 400, (255, 255, 255))
        self.quit_button = text("Press 'Q' to Quit", self.window, 400, 450, (255, 255, 255))
        

        pygame.mouse.set_visible(True)
        self.write_json()

    def write_json(self):
        """
        Method to update json file
        Only stores 2 scores, highest and most recent.
        """
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
        """
        Manage key events
        If player press 'P' key, run the flask and
        open the browser to see the scoreboard.
        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                self.next_screen = "welcome"
                self.running = False
            elif event.key == pygame.K_p:
                self.next_screen = False
                self.running = False
                Popen('python app.py')
                webbrowser.open('http://127.0.0.1:5002')
            elif event.key == pygame.K_q:
                self.running = False
                self.next_screen = False
