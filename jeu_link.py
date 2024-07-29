# Créé par chari, le 19/02/2024 en Python 3.7
from constances import *
import pygame
from pygame.locals import *
pygame.init()

# Initialisation de la musique
pygame.mixer.music.load("musique/main_theme.mp3")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

# Initialisation des class

class Plateau :
    def __init__(self,long,larg,image,sprite,titre):
        self.longueur = long
        self.largeur = larg
        self.fenetre = pygame.display.set_mode((self.longueur, self.largeur))
        self.image = image
        self.taille_sprite = sprite
        self.x = 0
        self.fond_niveau = pygame.image.load(self.image).convert_alpha()
        self.titre = pygame.display.set_caption(titre)


    def creation(self):
        self.fond_niveau = pygame.transform.scale(self.fond_niveau,(1800,self.largeur)) # image de 1500 px
        self.fenetre.blit(self.fond_niveau,(self.x,0))
        pygame.display.flip()


class Personnage:
    def __init__(self,nom,nbr_vie,nbr_piece,dico,x,y):
        self.nom = nom
        self.nbr_vie = nbr_vie
        self.nbr_piece = nbr_piece
        self.images = dico # dico dont clé = postion et valeurs = chargement des images
        self.perso = self.images["droite"][0] # La clé
        self.position = self.perso.get_rect()
        self.position = self.position.move(x,y)
        self.direction = 'stand'
        self.rect = pygame.Rect(self.position[0],self.position[1],taille_sprite,taille_sprite)

    def __str__(self):
        return  self.nom + str(self.nbr_vie) + str(self.nbr_piece) + str(self.images) + str(self.perso) + str(self.position) + str(self.direction) + str(self.rect)

class Objet_Mobs:
    def __init__(self,dico,x,y,point_vie,point_piece):
        self.images = dico
        self.objet = self.images["stand"][0]
        self.position = self.objet.get_rect()
        self.position = self.position.move(x,y)
        self.point_vie = point_vie
        self.point_piece = point_piece
        self.direction = 'stand'
        self.rect = pygame.Rect(self.position[0],self.position[1],taille_sprite,taille_sprite)

    def __str__(self):
        return str(self.point_vie)+ str(self.point_piece) + str(self.images) + str(self.objet) + str(self.position) + str(self.direction) + str(self.rect)


def changement_images(dico) :
    for direction, images in dico.items() :
        for i in range(len(images)):
            dico[direction][i] = pygame.image.load(dico[direction][i])
            dico[direction][i] = pygame.transform.scale(dico[direction][i],(taille_sprite,taille_sprite))
    return dico


# Initialisation du Héros
global taille_sprite
taille_sprite = 50

images_link = {
    'gauche': ["Images/Link/link_gauche ("+str(i)+").png" for i in range(1,5)],
    'droite': ["Images/Link/link_droite ("+str(i)+").png" for i in range(1,5)],
    'haut': ["Images/Link/link_haut ("+str(i)+").png" for i in range(1,5)],
    'bas': ["Images/Link/link_bas ("+str(i)+").png" for i in range(1,5)],
    'stand' : ["Images/Link/link_stand.png"]
}
##nom_link = str(input("Choississez un nom de personnage : "))
images_link = changement_images(images_link)
link = Personnage(nom_link,3,0,images_link,50,410)

# Initialisation du Coeur
image_heart = {'stand': ["Images/Heart.png"]}
image_heart = changement_images(image_heart)
Heart = Objet_Mobs(image_heart,400,350,1,0)

# Initialisation des Pièces
image_piece = {'stand': ["Images/Diamond.png"]}
image_piece = changement_images(image_piece)
Piece = Objet_Mobs(image_piece,800,50,0,1)

image_piece_2 = {'stand': ["Images/Diamond_2.png"]}
image_piece_2 = changement_images(image_piece_2)
Piece_2 = Objet_Mobs(image_piece_2,1300,50,0,2)

image_piece_3 = {'stand': ["Images/Diamond_3.png"]}
image_piece_3 = changement_images(image_piece_3)
Piece_3 = Objet_Mobs(image_piece_3,1700,50,0,3)

# Initialisation du mob
image_hand = {'stand': ["Images/Hand/Hand_move ("+str(i)+").png" for i in range(1,5)]}
image_hand = changement_images(image_hand)
Hand = Objet_Mobs(image_hand,1200,410,1,0)

image_goliath = {'stand':["Images/Goliath/Goliath ("+str(i)+").png" for i in range(1,4)]}
image_goliath = changement_images(image_goliath)
Goliath = Objet_Mobs(image_goliath,1400,410,1,1)

image_flight = {'stand':["Images/Flight/Flight ("+str(i)+").png" for i in range(1,8)]}
image_flight = changement_images(image_flight)
Flight = Objet_Mobs(image_flight,1400,350,2,1)

image_slime = {'stand':["Images/Slime/Slime ("+str(i)+").png" for i in range(1,4)]}
image_slime = changement_images(image_slime)
Slime = Objet_Mobs(image_slime,1600,425,2,2)

image_boss = {'stand':["Images/Boss/Boss ("+str(i)+").png" for i in range(1,5)]}
image_boss = changement_images(image_boss)
Boss = Objet_Mobs(image_boss,1700,410,3,2)

# Initialisation du Chateau

image_chateau = {'stand' : ["Images/castle.png"]}
image_chateau = changement_images(image_chateau)
Chateau = Objet_Mobs(image_chateau,1900,410,0,0)


# Initialisation du Plateau
niveau = Plateau(1000,500,"Images/fond.png",10,"Link Run")
niveau.creation()

game_over = Plateau(1000,500,"Images/game_over.png",10,"Perdu !")

win = Plateau(1000,500,"Images/Win.png",10,"Win !")

def jeu() :
    # Initialisation du jeu
    clock = pygame.time.Clock()
    gagner = False
    continuer = True

    Heart_present = True
    Piece_present = True
    Piece_2_present = True
    Piece_3_present = True
    Hand_present = True
    Goliath_present = True
    Slime_present = True
    Flight_present = True
    Boss_present = True
    Chateau_present =  True
    x = 0  # pour déplacer le fond
    Heart_collision = False
    Piece_collision = False
    Piece_2_collision = False
    Piece_3_collision = False
    Hand_collision = False
    Goliath_collision = False
    Slime_collision = False
    Flight_collision = False
    Boss_collision = False
    Chateau_collision = False
    debut = pygame.time.get_ticks()


    while continuer:
        # Début du chrono
        duree = pygame.time.get_ticks()-debut
        duree = duree//1000
        clock.tick(60) # Nbr de FPS pour animation

        # Initialisation du texte
        color=(246, 255, 122)
        font = pygame.font.SysFont('Comic Sans MS,Arial',25)
        texte_vie = font.render('Vies : '+str(link.nbr_vie),True,color)
        texte_slogan = font.render("Go go "+link.nom+" !",True,color)
        texte_piece = font.render('Pièces : '+str(link.nbr_piece),True,color)
        texte_chrono = font.render("Chronomètre : "+str(duree)+" secondes",True,color)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False

        # Touche de déplacement de Link
        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_DOWN]:
            link.position = link.position.move(0, 15)
            link.rect.y += 15
            link.direction = 'bas'
        elif key_pressed[K_UP]:
            link.position = link.position.move(0, -15)
            link.rect.y -= 15
            link.direction = 'haut'
        elif key_pressed[K_RIGHT]:
            link.position = link.position.move(15, 0)
            link.rect.x += 15
            link.direction = 'droite'
        elif key_pressed[K_LEFT]:
            link.position = link.position.move(-15, 0)
            link.rect.x -= 15
            link.direction = 'gauche'
        else :
            link.direction = 'stand'

        # Limites du plateau
        if link.position[0] < -5 :
            link.position = link.position.move(15,0)
            link.rect.x+=15
        if link.position[0] > 950 :
            link.position = link.position.move(-15,0)
            link.rect.x-=15
        if link.position[1] > 415 :
            link.position = link.position.move(0,-15)
            link.rect.y-=15
        if link.position[1] < 350 :
            link.position = link.position.move(0,15)
            link.rect.y+=15
        if Piece.position[1]> 415:
            Piece_collision = True
        if Piece_2.position[1]> 415:
            Piece_2_collision = True
        if Piece_3.position[1]> 415:
            Piece_3_collision = True

        # Animation des sprites
        link.images[link.direction].append(link.images[link.direction].pop(0))
        Hand.images[Hand.direction].append(Hand.images[Hand.direction].pop(0))
        Slime.images[Slime.direction].append(Slime.images[Slime.direction].pop(0))
        Flight.images[Flight.direction].append(Flight.images[Flight.direction].pop(0))
        Goliath.images[Goliath.direction].append(Goliath.images[Goliath.direction].pop(0))
        Boss.images[Boss.direction].append(Boss.images[Boss.direction].pop(0))

        # collision entre 2 sprites
        if Heart_present and not Heart_collision and link.rect.colliderect(Heart.rect) :
            link.nbr_vie += Heart.point_vie
            Heart_collision = True

        if Piece_present and not Piece_collision and link.rect.colliderect(Piece.rect) :
            link.nbr_piece += Piece.point_piece
            Piece_collision = True

        if Piece_2_present and not Piece_2_collision and link.rect.colliderect(Piece_2.rect) :
            link.nbr_piece += Piece_2.point_piece
            Piece_2_collision = True

        if Piece_3_present and not Piece_3_collision and link.rect.colliderect(Piece_3.rect) :
            link.nbr_piece += Piece_3.point_piece
            Piece_3_collision = True

        if Hand_present and not Hand_collision and link.rect.colliderect(Hand.rect):
            link.nbr_vie -= Hand.point_vie
            Hand_collision = True

        if Goliath_present and not Goliath_collision and link.rect.colliderect(Goliath.rect):
            link.nbr_vie -= Goliath.point_vie
            link.nbr_piece -= Goliath.point_piece
            Goliath_collision = True

        if Slime_present and not Slime_collision and link.rect.colliderect(Slime.rect):
            link.nbr_vie -= Slime.point_vie
            link.nbr_piece -= Slime.point_piece
            Slime_collision = True

        if Flight_present and not Flight_collision and link.rect.colliderect(Flight.rect):
            link.nbr_vie -= Flight.point_vie
            link.nbr_piece -= Flight.point_piece
            Flight_collision = True

        if Boss_present and not Boss_collision and link.rect.colliderect(Boss.rect):
            link.nbr_vie -= Boss.point_vie
            link.nbr_piece -= Boss.point_piece
            Boss_collision = True

        if Chateau_present and not Chateau_collision and link.rect.colliderect(Chateau.rect):
            link.nbr_vie -= Chateau.point_vie
            link.nbr_piece -= Chateau.point_piece
            Chateau_collision = True

        # Gestion de la victoire/défaite
        if link.nbr_piece < 0:
            link.nbr_piece = 0
            print(link.nbr_piece)
        if link.nbr_vie <=0:
            print("Perdu !")
            continuer = False
        if duree >= 75:
            print("Perdu")
            continuer = False
        if Chateau_present and Chateau_collision :
            gagner = True
            continuer = False
            print('gagné ! ')

        # Déplacement des objets/mobs au rythme du fond
        Heart.position = Heart.position.move(-1,0)
        Heart.rect.x -= 1
        Piece.position = Piece.position.move(-1,3)
        Piece.rect.x -= 1
        Piece.rect.y += 3
        Piece_2.position = Piece_2.position.move(-2,1)
        Piece_2.rect.x -= 2
        Piece_2.rect.y += 1
        Piece_3.position = Piece_3.position.move(-3,1)
        Piece_3.rect.x -= 3
        Piece_3.rect.y += 1
        Hand.position = Hand.position.move(-5,0)
        Hand.rect.x -= 5
        Goliath.position = Goliath.position.move(-3,0)
        Goliath.rect.x -= 3
        Slime.position = Slime.position.move(-5,0)
        Slime.rect.x -= 5
        Flight.position = Flight.position.move(-2,0)
        Flight.rect.x -=2
        Boss.position = Boss.position.move(-2,0)
        Boss.rect.x -= 2
        Chateau.position = Chateau.position.move(-2,0)
        Chateau.rect.x -= 2

        # Re-collage
        x-=1
    ##    print(link.rect)
    ##    print(Heart.rect)
    ##    print(Piece.rect)
    ##    print(Hand.rect)
    ##    print(Goliath.rect)
    ##    print(Boss.rect)
        niveau.fenetre.blit(niveau.fond_niveau,(x,0))
        niveau.fenetre.blit(texte_vie,(10,40))
        niveau.fenetre.blit(texte_piece,(110,40))
        niveau.fenetre.blit(texte_slogan,(x+50,10))
        niveau.fenetre.blit(texte_chrono,(650,10))
        if Heart_present and not Heart_collision:
            niveau.fenetre.blit(Heart.images[Heart.direction][0],Heart.position)
        if Piece_present and not Piece_collision :
            niveau.fenetre.blit(Piece.images[Piece.direction][0],Piece.position)
        if Piece_2_present and not Piece_2_collision :
            niveau.fenetre.blit(Piece_2.images[Piece_2.direction][0],Piece_2.position)
        if Piece_3_present and not Piece_3_collision :
            niveau.fenetre.blit(Piece_3.images[Piece_3.direction][0],Piece_3.position)
        if Hand_present and not Hand_collision :
            niveau.fenetre.blit(Hand.images[Hand.direction][0],Hand.position)
        if Goliath_present and not Goliath_collision :
            niveau.fenetre.blit(Goliath.images[Goliath.direction][0],Goliath.position)
        if Slime_present and not Slime_collision :
            niveau.fenetre.blit(Slime.images[Slime.direction][0],Slime.position)
        if Flight_present and not Flight_collision :
            niveau.fenetre.blit(Flight.images[Flight.direction][0],Flight.position)
        if Boss_present and not Boss_collision :
            niveau.fenetre.blit(Boss.images[Boss.direction][0],Boss.position)

        niveau.fenetre.blit(Chateau.images[Chateau.direction][0],Chateau.position)
        niveau.fenetre.blit(link.images[link.direction][0], link.position)

        #Rafraichissement
        clock.tick(10) #Nbr de FPS
        pygame.display.flip()

    if not gagner and not continuer:
##            fond_GameOver = pygame.image.load("Images/game_over.png").convert_alpha()
##            fond_GameOver = pygame.transform.scale(fond_GameOver,(1000,500))
            niveau.fenetre.blit(game_over.fond_niveau,(0,0))
            pygame.display.flip()

    else :
            niveau.fenetre.blit(win.fond_niveau,(0,0))
            pygame.display.flip()

    # fermeture fenêtre
    pygame.time.wait(2000)
    pygame.mixer.music.stop()
    pygame.quit()
jeu()