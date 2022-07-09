# coding: utf8

import pygame as py
from random import randint
from math import sqrt
#import norme as n

py.init()

NOIR        = ( 0 , 0 , 0 )
BLANC       = (255,255,255)
VERT        = ( 0 ,255, 0 )
ROUGE       = (255, 0 ,  0)
ROSE        = (255, 20,147)
GR_RG       = (132, 46, 27)
GRIS        = (122,145,145)
MARRON      = (165, 42, 42)
ARGENT      = (206,206,206)
ORANGE      = (255,192,0  )
JAUNE       = (255,255,0  )

### def des variables :
# def couleur de fonc
C_FOND = BLANC


# nombre de pixels en largueur et longueur : LARGUEUR
# nombre de blocs : NBCARRE
# forêt BP
LARGEUR = 1000
NBCARRE = 1000

# aleat
#LARGEUR = 750
#NBCARRE = 250

# Feu de Martigue
#LARGEUR = 600
#NBCARRE = 600

# temps d'attente en miliseconde
speed = 0
# pourcentage de foret en pourcentage
pforet = 100
#pforet = 80


# si on utilise l'outil de numérisation
IMAGE = "Forêt BP.jpg"
CARRE = LARGEUR // NBCARRE

nvterre = [[0 for j in range(300)] for i in range(329)]

arbre = [0 for i in range (8)]

"""
cadrillage utilisé pour les générations
#       (-2,-2),(-2,-1),(-2, 0),(-2, 1),(-2, 2),
#       (-1,-2),(-1,-1),(-1, 0),(-1, 1),(-1, 2),
#       ( 0,-2),( 0,-1),( 0, 0),( 0, 1),( 0, 2),
#       ( 1,-2),( 1,-1),( 1, 0),( 1, 1),( 1, 2),
#       ( 2,-2),( 2,-1),( 2, 0),( 2, 1),( 2, 2),
"""
g1 = [(-1,-1),(0,-1),(1,-1)]
g2 =[
(-2,-2),(-2,-1),
(-1,-2),(-1,-1),
( 0,-2),( 0,-1),
( 1,-2),( 1,-1),
( 2,-2),( 2,-1)]
d1 =[(-1,1),(0,1),(1,1)]
d2 =[
(-2, 1),(-2, 2),
(-1, 1),(-1, 2),
( 0, 1),( 0, 2),
( 1, 1),( 1, 2),
( 2, 1),( 2, 2)]

b2 = [(-2,-2),(-2,-1),(-2, 0),(-2, 1),(-2, 2),
      (-1,-2),(-1,-1),(-1, 0),(-1, 1),(-1, 2)]
h2 = [( 1,-2),( 1,-1),( 1, 0),( 1, 1),( 1, 2),
      ( 2,-2),( 2,-1),( 2, 0),( 2, 1),( 2, 2)]
ordre1 =[(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),]
ordre2 =[(-2,-2),(-2,-1),(-2,0),(-2,1),(-2,2),
         (-1,2),(0,2),(1,2),
         (2,2),(2,1),(2,0),(2,-1),
         (2,-2),(1,-2),(0,-2),(-1,-2)]

adjacent =[(-1,0),(1,0),(0,-1),(0,1)]

croix = [(0,0),(-1,0),(1,0),(0,-1),(0,1),
         (0, 2),(-2, 0),( 0,-2),( 2, 0)]

hg = [(-2,-2),(-2,-1),(-1,-2),(-1,-1)]
bg = [( 1,-2),( 1,-1),( 2,-2),( 2,-1)]
hd = [(-2, 1),(-2, 2),(-1, 1),(-1, 2)]
bd = [( 1, 1),( 1, 2),( 2, 1),( 2, 2)]
g1  = [[ 0,-2],[ 0,-1]]
d1  = [[ 0, 1],[ 0, 2]]
h1  = [[-2, 0],[-1, 0]]
b1  = [[ 1, 0],[ 2, 0]]

bas = [( 0,-1),        ( 0, 1),
       ( 1,-1),( 1, 0),( 1, 1),
       ( 2,-1),( 2, 0),( 2, 1)]


###

### Fonction d'affichage de la foret pour tous les programmes

def affichage(window,terre):
    for i in range(len(terre)):
        for j in range(len(terre[0])):

            ## Feu force 2
            if terre[i][j] == 7 :
                py.draw.rect(window, ROUGE, [CARRE*j,CARRE*i, CARRE,CARRE])

            ## Feu force 1
            if terre[i][j] == 6 :
                py.draw.rect(window, ROUGE, [CARRE*j,CARRE*i, CARRE,CARRE])

            ## Cendre force 2
            if terre[i][j] == 5 :
                py.draw.rect(window, ORANGE, [CARRE*j,CARRE*i, CARRE,CARRE])

            ## Cendre force 1
            if terre[i][j] == 4 :
                py.draw.rect(window, JAUNE, [CARRE*j,CARRE*i, CARRE,CARRE])

            ## Arbres
            elif terre[i][j] == 3 :
                py.draw.rect(window, VERT, [CARRE*j,CARRE*i, CARRE,CARRE])

            ## Murs
            elif    terre[i][j] == 1 :
                py.draw.rect(window, GRIS, [CARRE*j,CARRE*i, CARRE,CARRE])

            ## Sol Neutre
            elif  terre[i][j] == 0 :
                py.draw.rect(window, BLANC, [CARRE*j,CARRE*i, CARRE,CARRE])


###

###

### feu foret 0

# la regle n'a pas d'utilité ici
def gen0(terre,rule) :
    nvterre = [[terre[i][j] for j in range(len(terre[0]))] for i in range(len(terre))]

    for i in range(len(terre)) :
        for j in range(len(terre[0])) :

            ### arbre => feu

            if terre[i][j] == 3 :
                # si feu adjacent
                compt = 0
                for a,b in adjacent :
                    if terre[i+a][j+b] == 7 : compt +=1
                if compt >= 1 : nvterre[i][j] = 7

                # si + de 2 feux dans le voisinnage d'ordre 1
                compt = 0
                for a,b in ordre1 :
                    if terre[i+a][j+b] == 7 : compt +=1

                if compt >= 2 : nvterre[i][j] = 7

            ### feu => sol
            elif terre[i][j] == 7 :
                nvterre[i][j] = 1
    return(nvterre,True)


###

###

### feu foret 1

# la regle n'a pas d'utilité ici
def gen1(terre,rule):
    nvterre=[[terre[i][j] for j in range(len(terre[0]))] for i in range(len(terre))]

    for i in range(len(terre)):
        for j in range(len(terre[0])):

            ### arbre => feu
            if terre[i][j] == 3 :
                # si 1 feu adjacent
                compt = 0
                for a,b in adjacent :
                    if terre[i+a][j+b] == 7 : compt+=1

                if compt>=1 : nvterre[i][j] = 7

                # si + de 4 cendre voisinnage d'ordre 1
                compt = 0
                for a,b in ordre1 :
                    if terre[i+a][j+b] == 4 : compt +=1
                # avant f.nvterre[i][j]
                if compt >= 4 : nvterre[i][j] = 3

            ### feu => sol
            elif terre[i][j] == 7 :
                nvterre[i][j] = 1

    return(nvterre,True)


###

###
## Version SANS aléatoire mais avec règles sophistiquées
## Ordre 1
### feu foret 2
def gen2_1(terre,rule):
    nvterre=[[terre[i][j] for j in range(len(terre[0]))] for i in range(len(terre))]

    for i in range(len(terre)):
        for j in range(len(terre[0])):

            ### arbre => feu force 2/1 // cendres forces 1/2
            if terre[i][j] == 3 :
                # ordre 1
                arbre = [0 for i in range(8)]
                for a,b in ordre1 : arbre[terre[i+a][j+b]] += 1

                if arbre[4] + arbre[5] + arbre[6] >= rule[0] : nvterre[i][j] = 6
                if arbre[5] + arbre[6] + arbre[7] >= rule[1] : nvterre[i][j] = 7

            ### feu force 2 => feu force 1
            elif terre[i][j] == 7 : nvterre[i][j] = 6
            ### feu force 1 => cendres force 2
            elif terre[i][j] == 6 : nvterre[i][j] = 5
            ### cendre force 2 => cendre force 1
            elif terre[i][j] == 5 : nvterre[i][j] = 4
            ### cendre force 1 => sol
            elif terre[i][j] == 4 : nvterre[i][j] = 1

    return(nvterre,True)

def searcharound(i,j,terre,arbre) :

    # remise à zero de arbre
    for k in range(8) : arbre[k]=0

    # haut gauche
    for a,b in hg :
        if terre[i+a][j+b] > 3 : arbre[0] += 1

    # haut droit
    for a,b in hd :
        if terre[i+a][j+b] > 3 : arbre[2] += 1
    # bas gauche
    for a,b in bg :
        if terre[i+a][j+b] > 3 : arbre[6] += 1

    # bas droit
    for a,b in bd :
        if terre[i+a][j+b] > 3 : arbre[4] += 1

    # droit
    if terre[i][j+1] > 3 : arbre[3] += 1
    if terre[i][j+2] > 3 : arbre[3] += 1

    # gauche
    if terre[i][j-2] > 3 : arbre[7] += 1
    if terre[i][j-1] > 3 : arbre[7] += 1

    # haut
    if terre[i-2][j] > 3 : arbre[1] += 1
    if terre[i-1][j] > 3 : arbre[1] += 1

    # bas
    if terre[i+1][j] > 3 : arbre[5] += 1
    if terre[i+2][j] > 3 : arbre[5] += 1


# génération avec probabilité
# de propagation du feu
def gen3 (terre,rule):
    FINISH = True

    # creation de la copie de terre
    nvterre=[[terre[i][j] for j in range(len(terre[0]))] for i in range(len(terre))]

    prec = 10**4
    # à modifier 5-6-7
    nbfeu = 5 # 5  -  6  - 7   (pour avoir la même proportion entre
    decalage = 7   # 7  - 8.4 - 9.8  ord1+ord2 et g2,b2,h2 et d2)

    for i in range(len(terre)) :
        for j in range(len(terre[0])) :

            ### arbre => feu force 2/1 // cendres forces 1/2
            if terre[i][j] == 3 :

                searcharound(i,j,terre,arbre)
                ### Version sans l'expèrience

                #rule = [ 0.403891 , 0.362889 , 0.493857 , 0.326061 , 0.996577 ]
                # ordre 1 + 2
                if arbre[0]+arbre[1]+arbre[2]+arbre[3]+arbre[4]+arbre[5]+arbre[6]+arbre[7] >= nbfeu+decalage and randint(1,prec)/prec < rule[0] :
                    nvterre[i][j] = 7
                # gauche
                elif arbre[0]+arbre[6]+arbre[7] >= nbfeu and randint(1,prec)/prec < rule[1] :
                    nvterre[i][j] = 7
                # droite
                elif arbre[2]+arbre[3]+arbre[4] >= nbfeu and randint(1,prec)/prec < rule[2] :
                    nvterre[i][j] = 7
                # bas
                elif arbre[4]+arbre[5]+arbre[6] >= nbfeu and randint(1,prec)/prec < rule[3] :
                    nvterre[i][j] = 7
                # haut
                elif arbre[0]+arbre[1]+arbre[2] >= nbfeu and randint(1,prec)/prec < rule[4] :
                    nvterre[i][j] = 7

                """
                ### Version pour l'expèrience
                search = 0
                for a,b in bas :
                    if terre[i+a][j+b] > 3 : search += 1
                if search >= 2 and randint(1,prec)/prec < rule[3] :
                    nvterre[i][j] = 7
                """

            ### feu force 2 => feu force 1
            elif terre[i][j] == 7 : nvterre[i][j] = 6
            ### feu force 1 => cendres force 2
            elif terre[i][j] == 6 : nvterre[i][j] = 5
            ### cendre force 2 => cendre force 1
            elif terre[i][j] == 5 : nvterre[i][j] = 4
            ### cendre force 1 => mur
            elif terre[i][j] == 4 : nvterre[i][j] = 1

    if terre == nvterre :
        FINISH = False

    return(nvterre,FINISH)

def gen4 (terre,rule):
    FINISH = True

    # creation de la copie de terre
    nvterre=[[terre[i][j] for j in range(len(terre[0]))] for i in range(len(terre))]

    for i in range(len(terre)) :
        for j in range(len(terre[0])) :
            ### feu force 2 => feu force 1
            if terre[i][j] == 7 : nvterre[i][j] = 1
            ### feu force 1 => cendres force 2
            elif terre[i][j] == 6 : nvterre[i][j] = 1
            ### cendre force 2 => cendre force 1
            elif terre[i][j] == 5 : nvterre[i][j] = 1
            ### cendre force 1 => mur
            elif terre[i][j] == 4 : nvterre[i][j] = 1

    if terre == nvterre :
        FINISH = False

    return(nvterre,False)

def random0(terre,pforet):
    for i in range(len(terre)):
        for j in range(len(terre[0])):
            a = randint(1,100)
            if a <= pforet :
                terre[i][j] = 3
            else :
                terre[i][j] = 0
            # si on est au bord
            if i==0 or j==0 or i==len(terre)-1 or j==len(terre)-1:
                terre[i][j] = 1
    return(terre)

## Fonction de génération aléatoire des forets
# Compatible VERSION 1 et 2

def random3(terre,pforet):
    for i in range(len(terre)):
        for j in range(len(terre[0])):
            a = randint(1,100)
            if a <= pforet :
                terre[i][j] = 3
            else : terre[i][j] = 0
            # si on est au bord
            if i==0 or i==1 or j==0 or j==1 or i==len(terre)-1 or j==len(terre[0])-1 or i==len(terre)-2 or j==len(terre[0])-2:
                terre[i][j] = 1
    return(terre)

### Définition des fonctions à utiliser
## la version i utilise les fonctions [i] des listes suivantes
gen = [gen0, gen1, gen2_1, gen3]


###

### Numérisation

# fonction qui attribue, pour une couleur de pixel (R,G,B,m),
# l'un des quatre "blocs" de notre programme
def code (A) :

    #choix des diférentes règles de sélection (critère pour détecter la couleur d'un arbre)
    #if A[0] <= 25 and A[1] >= 220 and A[2] <= 25 :
    #if A[0] <= 200 and A[2] <= 200 and A[1] >= A[0] and A[1] >= A[2] :
    #if A[1] >= A[0] and A[1] >= A[2] :
    # Réglage qui marche bien avec Google Earth :
    if A[0] <= 50 and A[1] <= 50 and A[2] <= 50 and A[1] >= A[0] and A[1] >= A[2] :

        return(3)
    else : return(0)


def Numerisation(Version , NomFich,l):

    # Equivalent de NBCARRE du module
    # => variable modifiable et tt marche
    LARGEUR_SORTIE = l

    foret  = py.image.load(NomFich)
    taille = foret.get_size()


    ## Partie dégradation:
    a,b = taille
    # Pour éviter les problèmes de dépassement
    if a < LARGEUR_SORTIE : LARGEUR_SORTIE = a

    # On définit la HAUTEUR_SORTIE par une règle de trois
    # pour garder les proportions de l'image
    HAUTEUR_SORTIE = (b*LARGEUR_SORTIE)//a

    # Les intervalles entre chaque "prise de pixel" (en nombre de pixels)
    pas_largeur = a / LARGEUR_SORTIE
    pas_hauteur = b / HAUTEUR_SORTIE

    CARRE = a // LARGEUR_SORTIE

    terre = [[0 for j in range (LARGEUR_SORTIE)] for i in range (HAUTEUR_SORTIE)]

    for i in range (HAUTEUR_SORTIE) :
        for j in range (LARGEUR_SORTIE) :
            # pl et ph sont les coordonnées du relevé de pixel le plus
            # en haut à gauche (en nombre de pixels)
            pl = pas_largeur // 2
            ph = pas_hauteur // 2

    # La commande foret.get.at((x,y)) récupère le code (R,G,B,m)
    # du pixel aux coordonnées (x,y)
            terre[i][j]=code(foret.get_at((int(pl+(j*pas_largeur)),int(ph+(i*pas_hauteur)))))

    if Version > 3 :
        # On met des murs sur les bords
        for k in range (len(terre)):
            terre[k][0]  = 1
            terre[k][-1] = 1

        for k in range (len(terre[0])):
            terre[0][k]  = 1
            terre[-1][k] = 1

    # Doubles couches de murs !!! pour Version  3
    if Version == 3 or Version == 1 or Version == 2 :
        # On met des murs sur les bords
        for k in range (len(terre)):
            terre[k][1]  = 1
            terre[k][0]  = 1
            terre[k][-1] = 1
            terre[k][-2] = 1

        for k in range (len(terre[0])):
            terre[1][k] = 1
            terre[0][k]  = 1
            terre[-1][k] = 1
            terre[-2][k] = 1


    ## Dimension fenêtre
    # Comme les images ne sont plus carrées => redimensionner la fenetre
    # l_f et h_f sont la taille finale de la fenêtre
    l_f = CARRE*LARGEUR_SORTIE
    h_f = CARRE*HAUTEUR_SORTIE

    return(terre, CARRE, l_f, h_f)

