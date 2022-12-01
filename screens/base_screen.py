import pygame

class BaseScreen:
    """Base class for all game screens"""
    def __init__(self, window, state):
        self.window = window
        self.next_screen = False
        self.state = state

    def run(self):
        """
        This is the main method of the class.
        It manages the event loop, and:
        * ticks the clock at 60 FPS
        * calls `update` and `draw`
        * calls `manage_event` for each event received
        * quits the game if the quit button is clicked, or the Escape key is pressed
        """
        clock = pygame.time.Clock()
        self.running = True
        while self.running:
            clock.tick(60)
            self.update()
            self.draw()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.next_screen = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.running = False
                    self.next_screen = False

                self.manage_event(event)

    @property
    def rect(self):
        return self.window.get_rect()

    def draw(self):
        pass

    def update(self):
        pass

    def manage_event(self, event):
        pass
