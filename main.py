import pygame
pygame.init()

# Dimensions de la fenêtre
largeur = 800
hauteur = 600

# Initialisation de la fenêtre
ecran = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Satisfying game")

# Boucle principale du jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Logique du jeu
    ecran.fill((0,0,255))

    # Mise à jour de l'affichage
    pygame.display.flip()

# Fermeture de Pygame
pygame.quit()
