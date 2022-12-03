import pygame
from screens import WelcomeScreen, GameScreen, GameOverScreen, UsernameScreen

class Game:
    """Main class for the application"""
    def __init__(self):

        self.window = pygame.display.set_mode((800, 600))

    def run(self):
        """Main method, manages interaction between screens"""
        screens = {
            "welcome": WelcomeScreen,
            "username": UsernameScreen,
            "game": GameScreen,
            "game_over": GameOverScreen,
        }

        running = True
        current_screen = "welcome"
        state = {}
        while running:
            screen_class = screens.get(current_screen)
            screen = screen_class(self.window, state)

            screen.run()

            if screen.next_screen is False:
                running = False

            current_screen = screen.next_screen
            state = screen.state


if __name__ == "__main__":
    game = Game()
    game.run()