import pygame
from player import Player
from game_screen import gameScreen
from menu_screen import menuScreen
from bridge import Bridge
from button import Button
pygame.init()

# Dimensions de la fenêtre
largeur = 800
hauteur = 600


# Initialisation de la fenêtre
menu_screen = pygame.display.set_mode((largeur, hauteur))
game_screen = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Satisfying game")
player = Player(game_screen, 400, 500)
bridge = Bridge(game_screen)

def stop_running():
    global running
    running = False
def test():
    global player
    player.loose = False
    pygame.event.pump()

play_button = Button(200,200,100,50,(0,0,255), (0,255,0), "Jouer", test)
quit_button = Button(200,400,100,50,(0,0,255), (0,255,0), "Quitter", stop_running)
# Boucle principale du jeu

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if player.loose:
        menuScreen(game_screen,event, play_button,quit_button)
    else:
        gameScreen(game_screen, player, event,bridge)
    
    


# Fermeture de Pygame
pygame.quit()
