import pygame

class Player:
    def __init__(self, screen, x, y) :
        self.screen = screen
        self.color = (0,0,0)
        self.rect = pygame.Rect(x,y,20,20)
        self.loose = False
    
    def movement(self, keys):
        if keys == "droite":
            self.rect.x += 5
        if keys == "gauche":
            self.rect.x -= 5
        if self.rect.x <= 200:
            self.rect.x = 400
            self.loose = True
        if self.rect.x >= 600:
            self.rect.x = 400
            self.loose = True
    
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

        
