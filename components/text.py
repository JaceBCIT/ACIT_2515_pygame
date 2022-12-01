import pygame

pygame.font.init()

default_font = pygame.font.get_default_font()

def text(text, surface, x, y, color):
    """Method for text"""
    font = pygame.font.Font(default_font, 28)
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.centerx = x
    text_rect.centery = y
    surface.blit(text_obj, text_rect)