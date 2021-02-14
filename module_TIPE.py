
# coding: utf8

import pygame as py
from random import randint
#from C:/Users/marin/Documents/Perso/Python/GENERAL/Couleur import *
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
LARGUEUR = 600
# nombre de carré : max 200 sans lag
NBCARRE = 150
# en miliseconde
speed = 10

CARRE = LARGUEUR/NBCARRE

ordre1 =[(-1,-1),
         (0,-1),
         (1,-1),
         (-1,1),
         (0,1),
         (1,1),
         (-1,0),
         (1,0)]

adjacent =[(-1,0),
         (1,0),
         (0,-1),
         (0,1)]
###

###

### feu foret 1

def affichage1(window,terre):
    for i in range(len(terre)):
        for j in range(len(terre)):

            ## Feu
            if    terre[i][j] == 3 :
                py.draw.rect(window, ROUGE, [CARRE*j,CARRE*i, CARRE,CARRE])

            ## Murs
            elif    terre[i][j] == 2 :
                py.draw.rect(window, GRIS, [CARRE*j,CARRE*i, CARRE,CARRE])

            ## Arbres
            elif  terre[i][j] == 1 :
                py.draw.rect(window, VERT, [CARRE*j,CARRE*i, CARRE,CARRE])

            ## Sol Neutre
            elif  terre[i][j] == 0 :
                py.draw.rect(window, BLANC, [CARRE*j,CARRE*i, CARRE,CARRE])
            ## TEST
            ## Cendres finales fixes
            elif terre[i][j] == -1 :
                py.draw.rect(window, ARGENT, [CARRE*j,CARRE*i, CARRE,CARRE])


def gen1(terre):
    nvterre=[[terre[i][j] for j in range(len(terre))] for i in range(len(terre))]

    for i in range(len(terre)):
        for j in range(len(terre)):

            ### arbre => feu

            if terre[i][j] == 1 :
                # si feu adjacent
                compt = 0
                for a,b in adjacent :
                    if terre[i+a][j+b] == 3 : compt+=1
                if compt>=1 : nvterre[i][j] = 3

                # si + de 2 feux dans le voisinnage d'ordre 1
                compt = 0
                for a,b in ordre1 :
                    if terre[i+a][j+b] == 3 : compt +=1
                if compt >= 2 : nvterre[i][j] = 3

            ### feu => sol
            elif terre[i][j] == 3 :
                nvterre[i][j] = 0

    return(nvterre)

def random1(terre,pforet):
    for i in range(len(terre)):
        for j in range(len(terre)):
            a = randint(1,100)
            if a <= pforet :
                terre[i][j]=1
            else :
                terre[i][j]=0
            # si on est au bord
            if i==0 or j==0 or i==len(terre)-1 or j==len(terre)-1:
                terre[i][j]=2
    return(terre)



###

###

### feu foret 2

def affichage2(window,terre):
    for i in range(len(terre)):
        for j in range(len(terre)):
            ## Feu
            if    terre[i][j] == 5 :
                py.draw.rect(window, ROUGE, [CARRE*j,CARRE*i, CARRE,CARRE])

            ## Cendre
            if    terre[i][j] == 4 :
                py.draw.rect(window, GR_RG, [CARRE*j,CARRE*i, CARRE,CARRE])

            ## Arbres
            elif  terre[i][j] == 3 :
                py.draw.rect(window, VERT, [CARRE*j,CARRE*i, CARRE,CARRE])

            ## Arbres mort
            elif  terre[i][j] == 2 :
                py.draw.rect(window, MARRON, [CARRE*j,CARRE*i, CARRE,CARRE])

            ## Murs
            elif    terre[i][j] == 1 :
                py.draw.rect(window, GRIS, [CARRE*j,CARRE*i, CARRE,CARRE])

            ## Sol Neutre
            elif  terre[i][j] == 0 :
                py.draw.rect(window, BLANC, [CARRE*j,CARRE*i, CARRE,CARRE])


def gen2(terre):
    nvterre=[[terre[i][j] for j in range(len(terre))] for i in range(len(terre))]

    for i in range(len(terre)):
        for j in range(len(terre)):

            ### arbre => feu
            if terre[i][j] == 3 :
                # si 1 feu adjacent
                compt = 0
                for a,b in adjacent :
                    if terre[i+a][j+b] == 5 : compt+=1
                if compt>=1 : nvterre[i][j] = 5

                # si + de 4 cendre voisinnage d'ordre 1
                compt = 0
                for a,b in ordre1 :
                    if terre[i+a][j+b] == 4 : compt +=1
                if compt >= 4 :
                    nvterre[i][j] = 3

            ### arbre mort => feu
            elif terre[i][j] == 2 :
                # si 1 (feu voisinnage d'ordre 1) adjacent
                compt = 0
                for a,b in adjacent :
                    if terre[i+a][j+b] == 5 : compt+=1
                if compt>=1 : nvterre[i][j] = 5

                # si + de 3 cendres dans le voisinnage d'ordre 1
                compt = 0
                for a,b in ordre1 :
                    if terre[i+a][j+b] == 4 : compt +=1

                if compt >= 3 :
                    nvterre[i][j] = 3

            ### feu => cendres
            elif terre[i][j] == 5 :
                nvterre[i][j] = 4

            ### cendre => sol
            elif terre[i][j] == 4 :
                nvterre[i][j] = 0

    return(nvterre)

# on prendra 30% d'abre mort
def random2(terre,pforet):
    for i in range(len(terre)):
        for j in range(len(terre)):
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



###

###

### feu foret 3

def affichage3(window,terre):
    for i in range(len(terre)):
        for j in range(len(terre)):

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


def gen3(terre,regle):
    nvterre=[[terre[i][j] for j in range(len(terre))] for i in range(len(terre))]

    for i in range(len(terre)):
        for j in range(len(terre)):

            ### arbre => feu force 2/1
            if terre[i][j] == 3 :
                # ordre 1
                arbre = [0 for i in range(8)]
                for a,b in ordre1 :
                    arbre[terre[i+a][j+b]]+=1

                if arbre[5]+arbre[6]+arbre[7]>=2 : nvterre[i][j]=7
                if arbre[4]+arbre[5]+arbre[6]>=3 : nvterre[i][j]=6
                #if arbre[5]+arbre[6]>=2 : nvterre[i][j]=6
                #if arbre[4]+arbre[5]>=2 : nvterre[i][j]=5

                if arbre[7]>=regle[0] : nvterre[i][j] = 7
                if arbre[6]>=regle[1] : nvterre[i][j] = 6
                if arbre[5]>=regle[2] : nvterre[i][j] = 5
                if arbre[4]>=regle[3] : nvterre[i][j] = 4
                """
                # adjacent
                arbre = [0 for i in range(8)]
                for a,b in adjacent :
                    arbre[terre[i+a][j+b]]+=1

                if arbre[6]>=regle[4] : nvterre[i][j] = 6
                if arbre[7]>=regle[5] : nvterre[i][j] = 7
                """
            ### arbre mort => feu force 2/1 // cendres forces 1/2
            elif terre[i][j] == 2 :
                # ordre 1
                arbre = [0 for i in range(8)]
                for a,b in ordre1 :
                    arbre[terre[i+a][j+b]]+=1

                if arbre[5]+arbre[6]+arbre[7]>=2 : nvterre[i][j]=7
                if arbre[4]+arbre[5]+arbre[6]>=2 : nvterre[i][j]=6
                #if arbre[5]+arbre[6]>=2 : nvterre[i][j]=6
                #if arbre[4]+arbre[5]>=2 : nvterre[i][j]=5

                if arbre[7]>=regle[4] : nvterre[i][j] = 7
                if arbre[6]>=regle[5] : nvterre[i][j] = 6
                if arbre[5]>=regle[6] : nvterre[i][j] = 5
                if arbre[4]>=regle[7] : nvterre[i][j] = 4
                """
                # adjacent
                arbre = [0 for i in range(8)]
                for a,b in adjacent :
                    arbre[terre[i+a][j+b]]+=1

                if arbre[6]>=regle[10] : nvterre[i][j] = 6
                if arbre[7]>=regle[11] : nvterre[i][j] = 7
                """

            ### feu force 2 => feu force 1
            elif terre[i][j] == 7 : nvterre[i][j] = 6
            ### feu force 1 => cendres force 2
            elif terre[i][j] == 6 : nvterre[i][j] = 5
            ### cendre force 2 => cendre force 1
            elif terre[i][j] == 5 : nvterre[i][j] = 4
            ### cendre force 1 => sol
            elif terre[i][j] == 4 : nvterre[i][j] = 1

    return(nvterre)

# on prendra 30% d'abre mort
def random3(terre,pforet):
    for i in range(len(terre)):
        for j in range(len(terre)):
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