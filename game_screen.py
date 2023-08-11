import pygame
from player import Player

def gameScreen(screen, user,event,bridge ):
        # Logique du jeu
        screen.fill((255,255,255))
        bridge.draw()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                user.movement("droite")
            elif event.key == pygame.K_LEFT:
                user.movement("gauche")
            user.draw()
            pygame.display.flip()
            pygame.time.delay(10)
