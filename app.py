import pygame
from screens import WelcomeScreen, GameScreen, GameOverScreen

class Game:

    def __init__(self):

        self.window = pygame.display.set_mode((800, 600))

    def run(self):
        screens = {
            "welcome": WelcomeScreen,
            "game": GameScreen,
            "game_over": GameOverScreen,
        }

        running = True
        current_screen = "welcome"
        while running:
            screen_class = screens.get(current_screen)
            screen = screen_class(self.window)

            screen.run()

            if screen.next_screen is False:
                running = False

            current_screen = screen.next_screen


if __name__ == "__main__":
    game = Game()
    game.run()