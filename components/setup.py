import random
from .enemy import Enemy

def setup(speed):
    """Method to setup where Aliens spawn"""
    random_direction = random.randint(1, 4)
    if random_direction == 1:
        return Enemy(random.randint(0, 800), 0, 0, speed)
    elif random_direction == 2:
            return Enemy(800, random.randint(0, 600), -speed, 0)
    elif random_direction == 3:
        return Enemy(random.randint(0, 800), 600, 0, -speed)
    elif random_direction == 4:
        return Enemy(0, random.randint(0, 600), speed, 0)

