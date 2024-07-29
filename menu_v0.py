from constances import *
import pygame
from pygame.locals import *
pygame.init()

pygame.mixer.music.load("musique/menu.mp3")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

def creation_fenetre(largeur,hauteur):
    """ création d'une fenêtre de taille largeur x hauteur"""
    global fenetre

    fenetre = pygame.display.set_mode((largeur, hauteur))
    pygame.display.set_caption("Link's Adventure Run")
    fond_niveau = pygame.image.load(fond).convert()
    pygame.transform.scale(fond_niveau, (largeur,hauteur))
    fenetre.blit(fond_niveau, (0,0))
    pygame.display.flip()


    running = True  #Variable pour contrôler la boucle principale
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False  #Quitter la boucle principale si l'utilisateur ferme la fenêtre
            if event.type == MOUSEBUTTONDOWN and event.button == 1:  #Vérifier le clic de souris
                #Récupérer les coordonnées du clic
                x, y = event.pos
                x2, y2 = event.pos
                x3, y3 = event.pos
                x4, y4 = event.pos
                #Vérifier si le clic est dans la zone du texte "Exit"
                if (largeur // 15.5 <= x <= largeur // 15.5 + 70) and (hauteur // 1.4 <= y <= hauteur // 1.4 + 50):
                    running = False
                    pygame.mixer.music.stop()
                #Vérifier si le clic est dans la zone du texte "Play"
                if (largeur // 15.5 <= x2 <= largeur // 15.5 + 70) and (hauteur // 1.8 <= y2 <= hauteur // 1.8 + 50):
                    running = False
                    pygame.mixer.music.stop()
                    import jeu_link




creation_fenetre(largeur,hauteur)
pygame.quit()