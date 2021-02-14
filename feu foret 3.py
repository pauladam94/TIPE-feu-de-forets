## Codage graphique propagation
## feu de forets 3 :
# coding: utf8

# taille fenetre :
import pygame as py
import module_TIPE as m
import numpy as np
from random import randint
# initialisation de pygame
py.init()

# Initialisation de la fenetre graphique avec son nom
fenetre = py.display.set_mode((m.LARGUEUR,m.LARGUEUR), py.DOUBLEBUF | py.HWSURFACE | py.RESIZABLE)
py.display.set_caption("JDLV P.A.")

# Vérif des paramètres d'affichage dans le terminal :
print(py.display.Info())

### Iniatilisation choix situation de départ :

fenetre.fill(m.BLANC)
terre = [[0]*m.NBCARRE for i in range(m.NBCARRE)]
py.time.delay(m.speed)
py.display.flip()


## Initialisation Variables :
# pourcentage de foret
pforet = 70

regle=[2,2,2,2,
       1,2,2,2,
        2,2,1,1]

A = True
while A :
    for event in py.event.get() :
        # conditions d'arrets de l'initialisation
        if event.type == py.QUIT :
            A = False
        if event.type == py.KEYDOWN and event.key == py.K_SPACE:
            A = False

        elif event.type == py.MOUSEBUTTONDOWN :
            #print(event.button)
            if event.button == 3 :
                #à changer
                terre= m.random3(terre,pforet)
            elif event.button == 6 :
                terre = [[0]*m.NBCARRE for i in range(m.NBCARRE)]
            else :

                b,a = event.pos
                a,b = int(a//m.CARRE) , int(b//m.CARRE)

                #dessin croix
                #terre[a][b] = 7
                for x,y in m.adjacent : terre[a+x][b+y]=7

            #à changer
            m.affichage3(fenetre,terre)

    py.display.flip()


## Sauvegarde pour récupérer les données
# sauv =[[terre[i][j] for j in range(len(terre))] for i in range(len(terre))]

A = True
compt=0
## Générations
while A :
    for event in py.event.get() :
        # conditions d'arrets de l'initialisation
        if event.type == py.QUIT :
            A = False
        if event.type == py.KEYDOWN and event.key == py.K_SPACE:
            A = False
        elif event.type == py.MOUSEBUTTONDOWN :
            b,a = event.pos
            a,b = int(a//m.CARRE) , int(b//m.CARRE)
            #dessin croix
            #terre[a][b] = 7
            for x,y in m.adjacent : terre[a+x][b+y]=7

    # à changer
    terre = m.gen3(terre,regle)
    m.affichage3(fenetre,terre)


    py.display.flip()
    py.time.delay(m.speed)
    compt+=1
    if compt%10 == 0:
        print(compt)

py.quit()