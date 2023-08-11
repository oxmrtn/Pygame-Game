import pygame

def menuScreen(screen,event, playButton, quitButton):
        screen.fill((0,0,0))
        playButton.verifier_clic(event)
        quitButton.verifier_clic(event)
        playButton.draw(screen)
        quitButton.draw(screen)
        pygame.display.flip()