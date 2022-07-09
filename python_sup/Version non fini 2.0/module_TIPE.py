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

### def des variables :
# def couleur de fonc
C_FOND = BLANC

# variable à définir en fonction du choix
LARGEUR = 600
# nombre de blocs en largeur : max 200 sans lag
NBCARRE = 300
# temps d'attente en miliseconde
speed = 0
# pourcentage de foret en pourcentage
pforet = 70

# si on utilise l'outil de numérisation
IMAGE = "Forêt BP.jpg"
CARRE = LARGEUR // NBCARRE

# définition de la regle à utiliser
# uniquement utile pour Version 2 et +
# bonne regle pour V3
#rule = [3, 2, 3, 1]
#rule = [3, 2, 2, 1]
#rule = [2, 3, 3, 1]

nvterre = [[0 for j in range(300)] for i in range(329)]


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
ordre2 =[(-2,-2), (-2,-1), (-2,0), (-2,1), (-2,2),
         (-1,2), (0,2), (1,2),
         (2,2), (2,1), (2,0), (2,-1),
         (2,-2), (1,-2), (0,-2), (-1,-2)]

adjacent =[(-1,0),(1,0),(0,-1),(0,1)]

croix = [(0,0),(-1,0),(1,0),(0,-1),(0,1),
         (0, 2),(-2, 0),( 0,-2),( 2, 0)]

Feu = 1
Arbre = 0
Mur = -1
Sol = 2

###
### Fonction d'affichage de la foret

def affichage(window,terre):
    for i in range(len(terre)):
        for j in range(len(terre[0])):

            ## Feu
            if terre[i][j] == Feu :
                py.draw.rect(window, ROUGE, [CARRE*j,CARRE*i, CARRE,CARRE])

            ## Arbres
            elif terre[i][j] == Arbre :
                py.draw.rect(window, VERT, [CARRE*j,CARRE*i, CARRE,CARRE])

            ## Murs
            elif    terre[i][j] == Mur :
                py.draw.rect(window, GRIS, [CARRE*j,CARRE*i, CARRE,CARRE])

            ## Sol Neutre
            elif  terre[i][j] == Sol :
                py.draw.rect(window, BLANC, [CARRE*j,CARRE*i, CARRE,CARRE])

#fin = [True]
# génération avec probabilité
# de propagation du feu
def gen (terre, rule):
    FINISH = True
    nvterre=[[terre[i][j] for j in range(len(terre[0]))] for i in range(len(terre))]
    prec = 10**4
    # à modifier 5 -  6  - 7
    nbfeu = 5 # 5  -  6  - 7   (pour avoir la même proportion entre
    dec = 7   # 7  - 8.4 - 9.8  ord1 + ord2 et g2, b2, h2 et d2)

    for i in range(len(terre)) :
        for j in range(len(terre[0])) :
            ### arbre => feu force 2/1 // cendres forces 1/2
            if terre[i][j] == 3 :

                # ordre 1
                #arbre = [0 for i in range(8)]
                #for a,b in ordre1 : arbre[terre[i+a][j+b]] += 1
                #if arbre[4] + arbre[5] + arbre[6] + arbre[7] >= 2 :
                #    if randint(1,prec)/prec < rule[0] :
                #        nvterre[i][j] = 7

                A = True
                # ordre 1 + 2
                arbre = [0 for i in range(8)]
                for a,b in ordre1 : arbre[terre[i+a][j+b]] += 1
                for a,b in ordre2 : arbre[terre[i+a][j+b]] += 1
                if arbre[4] + arbre[5] + arbre[6] + arbre[7] >= nbfeu + dec:
                    if randint(1,prec)/prec < rule[0] :
                        nvterre[i][j] = 7
                        A = False

                # gauche
                if A :
                    arbre = [0 for i in range(8)]
                    for a,b in g2 : arbre[terre[i+a][j+b]]+=1
                    if arbre[4] + arbre[5] + arbre[6] + arbre[7] >= nbfeu :
                        if randint(1,prec)/prec < rule[1] :
                            nvterre[i][j] = 7
                            A = False

                # droite
                if A :
                    arbre = [0 for i in range(8)]
                    for a,b in d2 : arbre[terre[i+a][j+b]] += 1
                    if arbre[4] + arbre[5] + arbre[6] + arbre[7] >= nbfeu :
                        if randint(1,prec)/prec < rule[2] :
                            nvterre[i][j] = 7
                            A = False

                # bas
                if A:
                    arbre = [0 for i in range(8)]
                    for a,b in b2 : arbre[terre[i+a][j+b]] += 1
                    if arbre[4] + arbre[5] + arbre[6] + arbre[7] >= nbfeu :
                        if randint(1,prec)/prec < rule[3] :
                            nvterre[i][j] = 7
                            A = False
                # haut
                if A:
                    arbre = [0 for i in range(8)]
                    for a,b in h2 : arbre[terre[i+a][j+b]] += 1
                    if arbre[4] + arbre[5] + arbre[6] + arbre[7] >= nbfeu :
                        if randint(1,prec)/prec < rule[4] :
                            nvterre[i][j] = 7
                            A = False

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


# Différence euclidienne entre deux matrices 2D
def diff_eucl(l1,l2):
    if len(l1)!=len(l2) or len(l1[0])!=len(l2[0]) : return(-1)
    s=0
    for i in range(len(l1)):
        for j in range(len(l1[0])):
            s+=(l1[i][j]-l2[i][j])**2
    return(sqrt(s))