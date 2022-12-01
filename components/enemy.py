import pygame

class Enemy(pygame.sprite.Sprite):
    """Sprite class for Aliens"""
    def __init__(self, xpos, ypos, horizontal_speed, vertical_speed):
        super().__init__()
        self.image = pygame.image.load("./images/enemy.png")
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.hspeed = horizontal_speed
        self.vspeed = vertical_speed

        self.set_direction()
    
    def set_direction(self):
        """Rotate the alien image depending on which side alien comes from"""
        if self.hspeed > 0:
            self.image = pygame.transform.rotate(self.image, 270)
        elif self.hspeed < 0:
            self.image = pygame.transform.rotate(self.image, 90)
        elif self.vspeed > 0:
            self.image = pygame.transform.rotate(self.image, 180)
    
    def update(self):
        """Remove Alien if collide"""
        self.rect.x += self.hspeed
        self.rect.y += self.vspeed
        if self.collide():
            self.kill()

    def collide(self):
        """If Aliens reach to end of screen, remove them"""
        if self.rect.x < 0 - self.rect.height or self.rect.x > 800:
            return True
        elif self.rect.y < 0 - self.rect.height or self.rect.y > 600:
            return True