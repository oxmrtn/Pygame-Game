import pygame

class Button:
    def __init__(self, x, y, largeur, hauteur, couleur_normale, couleur_survol, texte, action):
        self.rect = pygame.Rect(x, y, largeur, hauteur)
        self.couleur_normale = couleur_normale
        self.couleur_survol = couleur_survol
        self.texte = texte
        self.action = action
        self.survole = False

    def draw(self, fenetre):
        couleur = self.couleur_survol if self.survole else self.couleur_normale
        pygame.draw.rect(fenetre, couleur, self.rect)
        police = pygame.font.Font(None, 36)
        texte_surface = police.render(self.texte, True, pygame.Color('black'))
        texte_rect = texte_surface.get_rect(center=self.rect.center)
        fenetre.blit(texte_surface, texte_rect)

    def verifier_clic(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.survole = self.rect.collidepoint(event.pos)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.survole:
            self.action()