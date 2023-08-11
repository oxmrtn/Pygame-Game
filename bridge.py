import pygame

class Bridge:
    def __init__(self,screen):
        self.screen = screen
        self.color = (255,0,0)
        self.rect = pygame.Rect(200,0,400,600)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
