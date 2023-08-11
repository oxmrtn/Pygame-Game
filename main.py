from game_screen import gameScreen
import pygame
from player import Player
pygame.init()

# Dimensions de la fenêtre
largeur = 800
hauteur = 600

# Initialisation de la fenêtre

game_screen = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Satisfying game")
player = Player(game_screen, 400, 500)
# Boucle principale du jeu

gameScreen(game_screen, player)
    
if player.loose:
    menu_screen = pygame.display.set_mode((largeur, hauteur))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        menu_screen.fill((0,0,0))
        pygame.display.flip()
        
    


# Fermeture de Pygame
pygame.quit()
