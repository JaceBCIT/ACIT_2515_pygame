import pygame
from screens import BaseScreen
from components import text

class WelcomeScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def draw(self):
        self.window.fill((0, 0, 0))
        self.title = text('Dodge Aliens', self.window, 400, 175, (102, 0, 204))
        self.play_button = text("Press 'S' to play", self.window, 400, 300, (255, 255, 255))
        self.quit_button = text("Press 'Q' to quit", self.window, 400, 350, (255, 255, 255))


    def manage_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                self.next_screen = "username"
                self.running = False
            elif event.key == pygame.K_q:
                self.running = False
                self.next_screen = False
