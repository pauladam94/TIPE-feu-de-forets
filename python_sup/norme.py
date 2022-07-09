# coding: utf8
# Norme

# taille fenetre :
import pygame as py
import module_TIPE as m
from random import randint
import numpy as np
from time import sleep


# initialisation de pygame
py.init()

# Initialisation de la fenetre graphique avec son nom
py.display.set_caption("Animation feu de forets")

# toutes les versions sont comptibles avec le CHOIX demandé
a = 1
#rule = [a for i in range(6)]
#rule=[0.8, 0.8, 0.8, 1, 0.8,0.8]
#rule = [ 0.315705 , 0.397217 , 0.506582 , 0.999761 , 0.294215]
# rule = [0.705790 , 0.413583 , 0.698237 , 0.299002 , 0.768593]
# rule = [0.740623 , 0.41319 , 0.753198 , 0.273529 , 0.942581]
# rule = [0.258332 , 0.474413 , 0.7209 , 0.254891 , 0.710462]
# rule = [0.406718 , 0.451291 , 0.580995 , 0.305784 , 0.757176]

### GOOD ONE
rule = [ 0.403891 , 0.362889 , 0.493857 , 0.326061 , 0.996577 ]

### Merdique test
#rule = [ 1 , 0.3 , 0.4 , 0.3 , 0.4 ]

#0.406718 / 0.451291 / 0.580995 / 0.305784 / 0.757176

## Regles runner en C++
# une bonne valeur de norme se trouve dans les alentour de 124


# création de la list
def creatlist(nom):
    fich = open(nom,"r")
    list = []
    for lgn in fich:
        s = lgn.strip()
        #print(s)
        l = []
        for i in range(len(s)):
            l.append( int(s[i]) )
        list.append(l)
    fich.close
    return(list)


terrebrul = creatlist("foretbrulee.txt")
terre = creatlist("foretavant.txt")

#terre = creatlist("test.txt")

l = len(terre)
h = len(terre[0])

fenetre = py.display.set_mode((m.CARRE*h,m.CARRE*l), py.SHOWN )

print(len(terre))
print(len(terre[0]))

## Boucle d'initialisation du feu
A = True
B = True
while A :
    for event in py.event.get() :
        # conditions d'arrets de l'initialisation
        if event.type == py.QUIT :
            A = False
            B = False
        if event.type == py.KEYDOWN and event.key == py.K_ESCAPE:
            A = False
            B = False
        if event.type == py.KEYDOWN and event.key == py.K_SPACE :
            A = False

        elif event.type == py.MOUSEBUTTONDOWN :
            # print(event.button)
            # si on appuie sur le clic gauche
            if event.button == 3 : print("rien programmé")

            # si on appuie sur le bouton du coté de la souris
            elif event.button == 6 : print("rien programmé")

            # si on appuie sur le clic gauche
            # on crée une croix de feu
            elif event.button == 1 :
                b,a = event.pos
                a,b = int(a//m.CARRE),int(b//m.CARRE)
                ###AFFICHAGE à enlever
                print("a=",a," b=",b)

                ### FORCE A DEMARRER COMME EN C++
                a=111
                b=150
                # dessin croix de feu
                for x,y in m.croix : terre[a+x][b+y] = 7

    ### POUR AFFICHER FORETBRUL
    m.affichage(fenetre,terre)
    py.display.flip()


FINISH = True
compt = 0
## Générations
while FINISH :
    if not B :
        FINISH = False
    for event in py.event.get() :
        # conditions d'arrets de l'initialisation
        if event.type == py.KEYDOWN and event.key == py.K_p :
            sleep(10)
        if event.type == py.QUIT :
            FINISH = False
        if event.type == py.KEYDOWN and event.key == py.K_SPACE :
            FINISH = False
        if event.type == py.KEYDOWN and event.key == py.K_ESCAPE:
            FINISH = False
        elif event.type == py.MOUSEBUTTONDOWN :
            b,a = event.pos

            a,b = int(a//m.CARRE) , int(b//m.CARRE)

            # dessin croix de feu
            for x,y in m.croix : terre[a+x][b+y]=7

    terre,FINISH = m.gen[3](terre,rule)
    m.affichage(fenetre,terre)

    # actualisation fenetre
    py.display.flip()
    # py.time.delay(m.speed)


    # affichage numéro génération
    compt += 1
    if compt%10 == 0:
        print(compt)

    # arret au bout d'un certain nombre de génération
    # if compt == len(terre) : A = False
sleep(20)
py.quit()

N1 = np.array(terre)
N2 = np.array(terrebrul)

NORME = np.linalg.norm(N2-N1)

print(NORME)