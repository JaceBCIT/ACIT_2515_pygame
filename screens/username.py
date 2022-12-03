import pygame
from screens import BaseScreen
from components import text

class UsernameScreen(BaseScreen):
    """Screen for user to type their name"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state["name"] = ""

    def draw(self):
        """Display Text on the screen"""
        self.window.fill((0, 0, 0))
        self.title = text('Enter your name', self.window, 400, 175, (255, 255, 255))
        self.input = text(self.state["name"], self.window, 400, 250, (255, 255, 255))

    def manage_event(self, event):
        """Key events to control screens"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.next_screen = "game"
                self.running = False
            elif event.key == pygame.K_BACKSPACE:
                self.state["name"] = self.state["name"][:-1]
            else:
                self.state["name"] += str(event.unicode)
        