import pygame
from player import Player

def gameScreen(screen, user):
    running = True
    while running and not(user.loose):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Logique du jeu
            screen.fill((255,255,255))
            keys = pygame.key.get_pressed()  # Récupère l'état des touches
            if keys[pygame.K_RIGHT]:
                user.movement("droite")
            elif keys[pygame.K_LEFT]:
                user.movement("gauche")

            """
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    user.movement("droite")
                elif event.key == pygame.K_LEFT:
                    user.movement("gauche")"""
            user.draw()
            pygame.display.flip()
            print("ca passe")
