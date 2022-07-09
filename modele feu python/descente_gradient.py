
"""
numérisation recup des images

def grosse_fonction:
    utilise les images

boucle descente de gradient
appelle la grosse_fonction
"""



## Codage méthode de la descente de gradient
## pour optimiser les règles par rapport à un feu de forêt réel
## feu de forets sans graphisme :
# coding: utf8

# taille fenetre :
import module_TIPE as m
from random import randint

V = 3

## Initialisation carte (forets)  / Création carte brulée
## avec les documents texte des forêts
terre_init = []
terre_brul = []

## Initialisation du feu
coor = (200,200)

A = True
compt=0
## Générations
def foret(terre_i, terre_f, rule) :
    for i in range(1000):
        terre = m.gen[Version](terre,m.rule)
    m.affichage(fenetre,terre)



