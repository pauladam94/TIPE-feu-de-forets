
# coding: utf8

import pygame as py
from random import randint

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

### def des variables :
# def couleur de fonc
C_FOND = BLANC

# variable à définir en fonction du choix
LARGEUR = 600
# nombre de blocs en largeur : max 200 sans lag
NBCARRE = 200
# temps d'attente en miliseconde
speed = 0
# pourcentage de foret en pourcentage
pforet = 75

# si on utilise l'outil de numérisation
IMAGE = "Forêt BP.jpg"

# définition de la regle à utiliser
# uniquement utile pour Version 2 et +
# bonne regle pour V3
#rule = [3, 2, 3, 1]
# bonne regle pour V4

#rule = [3, 2, 2, 1]

#rule = [2, 3, 3, 1]

# autre regle possible
rule=[ 0.4, 0.4, 0.15, 0.15 ]

droite =[(1,-1),
         (1,1),
         (1,0)]

ordre1 =[(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),]
ordre2 = [(-2,-2),(-2,-1),(-2,0),(-2,1),(-2,2),
           (-1,2),(0,2),(1,2),(2,2),(2,1),(2,0),(2,-1),(2,-2),
           (1,-2),(0,-2),(-1,-2)]
adjacent =[(-1,0),
           (1,0),
           (0,-1),
           (0,1)]

CARRE = LARGEUR // NBCARRE

x=-1

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
                py.draw.rect(window, ROSE, [CARRE*j,CARRE*i, CARRE,CARRE])

            ## Cendre force 2
            if terre[i][j] == 5 :
                py.draw.rect(window, GR_RG, [CARRE*j,CARRE*i, CARRE,CARRE])

            ## Cendre force 1
            if terre[i][j] == 4 :
                py.draw.rect(window, GRIS, [CARRE*j,CARRE*i, CARRE,CARRE])

            ## Arbres
            elif terre[i][j] == 3 :
                py.draw.rect(window, VERT, [CARRE*j,CARRE*i, CARRE,CARRE])

            ## Arbres mort
            elif terre[i][j] == 2 :
                py.draw.rect(window, MARRON, [CARRE*j,CARRE*i, CARRE,CARRE])

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
def gen0(terre,rule):
    nvterre=[[terre[i][j] for j in range(len(terre[0]))] for i in range(len(terre))]

    for i in range(len(terre)):
        for j in range(len(terre[0])):

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
                nvterre[i][j] = 0
    return(nvterre)

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

                if compt >= 4 : nvterre[i][j] = 3

            ### arbre mort => feu
            elif terre[i][j] == 2 :
                # si 1 (feu voisinnage d'ordre 1) adjacent
                compt = 0
                for a,b in adjacent :
                    if terre[i+a][j+b] == 7 : compt+=1
                if compt>=1 : nvterre[i][j] = 7

                # si + de 3 cendres dans le voisinnage d'ordre 1
                compt = 0
                for a,b in ordre1 :
                    if terre[i+a][j+b] == 4 : compt +=1

                if compt >= 3 :
                    nvterre[i][j] = 4

            ### feu => cendres
            elif terre[i][j] == 7 :
                nvterre[i][j] = 4

            ### cendre => sol
            elif terre[i][j] == 4 :
                nvterre[i][j] = 0
    return(nvterre)


###

###

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

            ### arbre mort => feu force 2/1 // cendres forces 1/2
            elif terre[i][j] == 2 :
                # ordre 1
                arbre = [0 for i in range(8)]
                for a,b in ordre1 : arbre[terre[i+a][j+b]] += 1

                if arbre[4] + arbre[5] + arbre[6] >= rule[2] : nvterre[i][j] = 6
                if arbre[5] + arbre[6] + arbre[7] >= rule[3] : nvterre[i][j] = 7

            ### feu force 2 => feu force 1
            elif terre[i][j] == 7 : nvterre[i][j] = 6
            ### feu force 1 => cendres force 2
            elif terre[i][j] == 6 : nvterre[i][j] = 5
            ### cendre force 2 => cendre force 1
            elif terre[i][j] == 5 : nvterre[i][j] = 4
            ### cendre force 1 => sol
            elif terre[i][j] == 4 : nvterre[i][j] = 0

    return(nvterre)

def gen2_2(terre,rule):
    nvterre=[[terre[i][j] for j in range(len(terre[0]))] for i in range(len(terre))]

    for i in range(len(terre)):
        for j in range(len(terre[0])):

            ### arbre => feu force 2/1 // cendres forces 1/2
            if terre[i][j] == 3 :
                # ordre 1
                arbre = [0 for i in range(8)]
                for a,b in ordre1 : arbre[terre[i+a][j+b]]+=1

                if arbre[4] + arbre[5] >= rule[0] : nvterre[i][j] = 5
                if arbre[6] + arbre[7] >= rule[1] : nvterre[i][j] = 7

            ### arbre mort => feu force 2/1 // cendres forces 1/2
            elif terre[i][j] == 2 :
                # ordre 1
                arbre = [0 for i in range(8)]
                for a,b in ordre1 : arbre[terre[i+b][j+a]]+=1

                if arbre[4] + arbre[5] >= rule[2] : nvterre[i][j] = 5
                if arbre[6] + arbre[7] >= rule[3] : nvterre[i][j] = 7

            ### feu force 2 => feu force 1
            elif terre[i][j] == 7 : nvterre[i][j] = 6
            ### feu force 1 => cendres force 2
            elif terre[i][j] == 6 : nvterre[i][j] = 5
            ### cendre force 2 => cendre force 1
            elif terre[i][j] == 5 : nvterre[i][j] = 4
            ### cendre force 1 => sol
            elif terre[i][j] == 4 : nvterre[i][j] = 0

    return(nvterre)






# génération avec probabilité
# de propagation
def gen3 (terre,rule):
    nvterre=[[terre[i][j] for j in range(len(terre[0]))] for i in range(len(terre))]
    prec = 10**4
    for i in range(len(terre)):
        for j in range(len(terre[0])):
            ### arbre => feu force 2/1 // cendres forces 1/2
            if terre[i][j] == 3 :
                # ordre 1
                arbre = [0 for i in range(8)]
                for a,b in ordre1 : arbre[terre[i+a][j+b]]+=1

                if arbre[4] + arbre[5] >= 2 :
                    a=randint(1,prec)/prec
                    if a < rule[0] :
                        nvterre[i][j] = 5

                if arbre[6] + arbre[7] >= 2 :
                    a=randint(1,prec)/prec
                    if a < rule[1] :
                        nvterre[i][j] = 7

                # ordre 2
                for a,b in ordre2 : arbre[terre[i+b][j+a]]+=1

                if arbre[4] + arbre[5] >= 4 :
                    a=randint(1,prec)/prec
                    if a < rule[2] :
                        nvterre[i][j] = 5

                if arbre[6] + arbre[7] >= 4 :
                    a=randint(1,prec)/prec
                    if a < rule[3] :
                        nvterre[i][j] = 7





            ### feu force 2 => feu force 1
            elif terre[i][j] == 7 : nvterre[i][j] = 6
            ### feu force 1 => cendres force 2
            elif terre[i][j] == 6 : nvterre[i][j] = 5
            ### cendre force 2 => cendre force 1
            elif terre[i][j] == 5 : nvterre[i][j] = 4
            ### cendre force 1 => mur
            elif terre[i][j] == 4 : nvterre[i][j] = 1
    return(nvterre)







## Fonction de génération aléatoire des forets
# Compatible VERSION 1 et 2

# on prendra 30% d'abre mort
def random12(terre,pforet):
    for i in range(len(terre)):
        for j in range(len(terre[0])):
            a = randint(1,100)
            if a <= pforet :
                # foret
                b= randint(1,100)
                if b<= 30 : terre[i][j] = 2
                else : terre[i][j]= 3

            else : terre[i][j] = 0
            # si on est au bord
            if i==0 or j==0 or i==len(terre)-1 or j==len(terre)-1:
                terre[i][j]=1
    return(terre)

def random3(terre,pforet):
    for i in range(len(terre)):
        for j in range(len(terre[0])):
            a = randint(1,100)
            if a <= pforet :
                terre[i][j]= 3
            else : terre[i][j] = 0
            # si on est au bord
            if i==0 or i==1 or j==0 or j==1 or i==len(terre)-1 or j==len(terre[0])-1 or i==len(terre)-2 or j==len(terre[0])-2:
                terre[i][j]=1
    return(terre)

### Définition des fonctions à utiliser
# la version i utilise les fonctions [i] des listes suivantes

gen = [gen0, gen1, gen2_1, gen3]
random = [random0, random12, random12, random3]





























###

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

        # On prendra 30% d'arbres morts parmi les arbres identifiés.
        proba = randint(1,100)
        if proba <= 30 :
            return(2)
        else : return(3)
    else : return(0)


def Numerisation(NomFich,l):

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

    # On met des murs sur les bords
    for k in range (len(terre)):
        terre[k][0]  = 1
        terre[k][-1] = 1

    for k in range (len(terre[0])):
        terre[0][k]  = 1
        terre[-1][k] = 1

    ## Dimension fenêtre
    # Comme les images ne sont plus carrées => redimensionner la fenetre
    # l_f et h_f sont la taille finale de la fenêtre
    l_f = CARRE*LARGEUR_SORTIE
    h_f = CARRE*HAUTEUR_SORTIE

    return(terre, CARRE, l_f, h_f)

# norme de la différence entre
# deux matrices 2D d'entiers
def diff_eucl(l1,l2):
    if len(l1)!=len(l2) or len(l1[0])!=len(l2[0]) : return(-1)
    s=0
    for i in range(len(l1)):
        for j in range(len(l1[0])):
            s+=(l1[i][j]-l2[i][j])**2
    return(sqrt(s))















# affichage d'un mur de pierre
"""
for j in range(len(terre)//6,len(terre)-len(terre)//6):
    terre[len(terre)//2][j] = 0
"""

## Sauvegarde pour récupérer les données
# sauv =[[terre[i][j] for j in range(len(terre))] for i in range(len(terre))]
