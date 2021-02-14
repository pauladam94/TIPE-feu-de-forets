## Codage graphique Conway jeu de la vie :
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

# Variables initialisation
# pourcentage de foret
pforet = 60

A = True
while A :
    for event in py.event.get() :
        # conditions d'arrets de l'initialisation
        if event.type == py.QUIT :
            A = False
        if event.type == py.KEYDOWN and event.key == py.K_SPACE:
            A = False

        elif event.type == py.MOUSEBUTTONDOWN :
            print(event.button)
            if event.button == 3 :
                ### partie qui change entre les simulations
                terre= m.random1(terre,pforet)
            elif event.button == 6 :
                terre = [[0]*m.NBCARRE for i in range(m.NBCARRE)]
            else :

                b,a = event.pos
                a,b = int(a//m.CARRE) , int(b//m.CARRE)
                terre[a][b]=3
                terre[a][b+1]=3
                terre[a+1][b+1]=3
                terre[a+1][b]=3

                """
                for j in range(len(terre)//4,len(terre)-len(terre)//4):
                    terre[len(terre)//2][j] = 2
                """
                """
                if terre[a][b] == 3 :
                    terre[a][b] = 2
                elif terre[a][b] == 2 :
                    terre[a][b] = 1
                elif terre[a][b] == 1 :
                    terre[a][b] = 0
                elif terre[a][b] == 0 :
                    terre[a][b] = 3
                """

            m.affichage1(fenetre,terre)

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
            terre[a][b]=0
            """
            terre[a][b+1]=3
            terre[a+1][b+1]=3
            terre[a+1][b]=3
            """

    ###partie qui change entre les simulations
    terre = m.gen1(terre)
    m.affichage1(fenetre,terre)


    py.display.flip()
    py.time.delay(m.speed)
    compt+=1
    if compt%10 == 0:
        print(compt)

py.quit()











