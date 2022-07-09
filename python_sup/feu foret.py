## Codage graphique propagation
## feu de forets Version générale :
# coding: utf8

# taille fenetre :
from time import sleep
import pygame as py
import module_TIPE as m
from random import randint

# initialisation de pygame
py.init()

# Initialisation de la fenetre graphique avec son nom
py.display.set_caption("Animation feu de forets")

# Vérif des paramètres d'affichage dans le terminal :
#print(py.display.Info())

## CHOIX VERSION
# Il y a trois versions
# Version 0 : prog simple arbre/feu
# Version 1 : prog + evolué avec cendre et feu

# Version 2.1 et 2.2 : ++ evolué
# avec cendreF1/2 et feuF1/2
# regles de propagation modifiables sophistiquées

# Version 3  :
# règles probabilistes
# permet de mettre des règles continues ( descente de gradient )
Version = 3

# choix définit si on initialise
# la foret aléatoirement CHOIX = 0
# en fonction de l'image d'Orsay CHOIX = 1
CHOIX = 1
## Version qui marche
# V0.0 (V0.1)
# V1.0 V1.1
# V2.0 V2.1
# V3.0 V3.1

# toutes les versions sont comptibles avec le CHOIX demandé
a = 0.8
#rule = [a for i in range(6)]
#rule=[0.1, 0.6, 0.6, 1, 0.6, 0.6]

# pour se propager comme dans l'expèrience
rule = [0,0,0,0.8,0,0]
rule = [ 0.403891 , 0.362889 , 0.493857 , 0.326061 , 0.996577 ]


## Initialisation map
# on initialise la foret de départ
terre = [[0]*m.NBCARRE for i in range(m.NBCARRE)]

if CHOIX == 0 :
    # génération aléatoire de la map
    # initialisation fenetre
    terre= m.random3(terre,m.pforet)
    fenetre = py.display.set_mode((m.LARGEUR,m.LARGEUR), py.SHOWN | py.RESIZABLE)

elif CHOIX == 1 :
    # numérisation de la map
    # initialisation fenetre
    terre, m.CARRE, l, h = m.Numerisation(Version, m.IMAGE, m.NBCARRE)
    fenetre = py.display.set_mode((l,h), py.SHOWN | py.RESIZABLE)

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

            # si on appuie sur le bouton du coté de la souris
            if event.button == 6 :
                terre = [[0]*m.NBCARRE for i in range(m.NBCARRE)]

            # si on appuie sur le clic gauche
            # on crée une croix de feu
            elif event.button == 1 :
                b,a = event.pos
                a,b = int(a//m.CARRE) , int(b//m.CARRE)
                # dessin croix de feu
                for x,y in m.croix : terre[a+x][b+y]=7

    m.affichage(fenetre,terre)
    py.display.flip()

FINISH = True
compt = 0
## Générations
while FINISH :
    if not B:
        FINISH = False
    for event in py.event.get() :
        # conditions d'arrets de l'initialisation
        if event.type == py.KEYDOWN and event.key == py.K_p :
            # terre, FINISH = m.gen4(terre,rule)
            # m.affichage(fenetre,terre)
            # py.display.flip()
            sleep(30)
        if event.type == py.QUIT :
            FINISH = Falsep
        if event.type == py.KEYDOWN and event.key == py.K_SPACE:
            FINISH = False
        if event.type == py.KEYDOWN and event.key == py.K_ESCAPE:
            FINISH = False
        elif event.type == py.MOUSEBUTTONDOWN :
            sleep(30)
    if FINISH == False :
        terre, A  = m.gen[Version](terre,rule)
    else :
        terre, FINISH = m.gen[Version](terre,rule)
    m.affichage(fenetre,terre)

    # actualisation fenetre
    py.display.flip()
    py.time.delay(m.speed)


    #affichage numéro génération
    #compt += 1
    #if compt%50 == 0 :
    #    print(compt)
    #    sleep(5)

    # arret au bout d'un certain nombre de génération
    # if compt == len(terre) : A = False


py.quit()