# coding: utf8

import pygame as py
from random import randint
from math import sqrt

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

# dimension de la fenêtre de visualisation 
CARRE = 2

"""
cadrillage utilisé pour les générations
#       (-2,-2),(-2,-1),(-2, 0),(-2, 1),(-2, 2),
#       (-1,-2),(-1,-1),(-1, 0),(-1, 1),(-1, 2),
#       (0, -2),(0, -1),( 0, 0),( 0, 1),( 0, 2),
#       (1, -2),(1, -1),( 1, 0),( 1, 1),( 1, 2),
#       (2, -2),(2, -1),( 2, 0),( 2, 1),( 2, 2),
"""
g1 = [(-1,-1),(0,-1),(1,-1)]
g2 =[
(-2,-2),(-2,-1),
(-1,-2),(-1,-1),
(0,-2),(0,-1),
(1,-2),(1,-1),
(2,-2),(2,-1)]
d1 =[(-1,1),(0,1),(1,1)]
d2 =[
(-2, 1),(-2, 2),
(-1, 1),(-1, 2),
(0, 1),(0, 2),
(1, 1),(1, 2),
(2, 1),(2, 2)]

h2 = [(-2,-2),(-2,-1),(-2, 0),(-2, 1),(-2, 2),
      (-1,-2),(-1,-1),(-1, 0),(-1, 1),(-1, 2)]
      
b2 = [(1,-2),(1,-1),(1, 0),(1, 1),(1, 2),
      (2,-2),(2,-1),(2, 0),(2, 1),(2, 2)]
      
ordre1 =[(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),]
ordre2 =[(-2,-2),(-2,-1),(-2,0),(-2,1),(-2,2),
         (-1,2),(0,2),(1,2),
         (2,2),(2,1),(2,0),(2,-1),
         (2,-2),(1,-2),(0,-2),(-1,-2)]


adjacence = ordre1 + ordre2
#print(adjacence)
adjacence_inv = []
# adjacence_inv associe à  chaque cellule de menace pour un arbre
# sa position relative valide 1 ou invalide 0 par rapport à l'arbre dans l'ordre suivant (d,b,g,h,ordre1,ordre2)
for couple in adjacence :
    position_rel =  [0, 0, 0, 0, 0, 0]
    if couple in adjacence: position_rel[0] = 1
    if couple in g2: position_rel[1] = 1
    if couple in d2: position_rel[2] = 1
    if couple in b2: position_rel[3] = 1
    if couple in h2: position_rel[4] = 1

    adjacence_inv.append((couple, position_rel))

#print(adjacence_inv)
#print("longueur =",len(adjacence_inv))

# Dans l'ordre, Cendres2, Cendres1, Feu1, Feu2 
# Donne le coefficient de risque pour chaque type de menace
#regle_menace = (1,1,1,1)

def def_men_feu_arbres(terre, menaces):
    # menace est la liste des coordonnées des menaces(feu, cendres) 
    # retourne les coordonnées des arbres adjacents menacés
    men_feu_arbres = {}
    # men_feu_arbres = []
    for pos, etat in menaces : # parcours des menaces
            x = pos[0] # abscisse de la menace
            y = pos[1] # ordonnee de la menace
            for pos_adj, position_rel in adjacence_inv : # parcours des cases adjacentes
               xa = pos_adj[0] # abs case adj
               ya = pos_adj[1] # ord case adj
               if terre[x+xa][y+ya] == 3 :
                    cle_men = f'{x+xa}_{y+ya}'
                    #cle_men = [x+xa, y+ya]
                    # print(cle_men)
                    
                    #etat_menace = [p*regle_menace[etat-4] for p in position_rel]   
                    etat_menace =[position_rel[k] for k in range(len(position_rel))]
                    
                    if not (cle_men in men_feu_arbres.keys()) : # si t pas dedans
                        men_feu_arbres[cle_men] = etat_menace
                    else : # si t dedans
                        # actualisation men_feu_arbres[cle_men]
                        etat_menace_n = [0, 0, 0, 0, 0]
                        etat_menace_prel = men_feu_arbres[cle_men]
                        for i in range(len(etat_menace_n)) :
                            etat_menace_n[i] = etat_menace_prel[i] + etat_menace[i] 
                        men_feu_arbres[cle_men] = etat_menace_n
    
    #print(men_feu_arbres)
    return men_feu_arbres

### Fonction d'affichage de la foret 
def affichage(window,terre):
    for i in range(len(terre)):
        for j in range(len(terre[0])):
            ## Feu force 2
            if terre[i][j] == 7:
                py.draw.rect(window, ROUGE, [CARRE*j,CARRE*i, CARRE,CARRE])
            ## Feu force 1
            elif terre[i][j] == 6:
                py.draw.rect(window, ROSE, [CARRE*j,CARRE*i, CARRE,CARRE])
            ## Cendre force 2
            elif terre[i][j] == 5 :
                py.draw.rect(window, GR_RG, [CARRE*j,CARRE*i, CARRE,CARRE])
            ## Cendre force 1
            elif terre[i][j] == 4 :
                py.draw.rect(window, GRIS, [CARRE*j,CARRE*i, CARRE,CARRE])
            ## Arbres
            elif terre[i][j] == 3 :
                py.draw.rect(window, VERT, [CARRE*j,CARRE*i, CARRE,CARRE])
            ## Arbres mort
            elif terre[i][j] == 2 :
                py.draw.rect(window, MARRON, [CARRE*j,CARRE*i, CARRE,CARRE])
            ## Murs (cadre de deux lignes et colonnes de 1 entourant la forêt puis arbres brulés) 
            elif    terre[i][j] == 1 :
                py.draw.rect(window, GRIS, [CARRE*j,CARRE*i, CARRE,CARRE])
            ## Sol Neutre
            elif  terre[i][j] == 0 :
                py.draw.rect(window, BLANC, [CARRE*j,CARRE*i, CARRE,CARRE])

nbfeu = 5
decalage = 7
prec = 10**4

def gen(terre, rule, menaces):

    # nvterre = copy.deepcopy(terre)
    
    
    # DEFINITION men_feu_arbres
    men_feu_arbres = def_men_feu_arbres(terre, menaces)
    
    #print(men_feu_arbres)
    menaces_n = []
    for cle_pos, etat_menace in men_feu_arbres.items():
        arbre_feu = False
        pos_arbre_men = [0,0]
        pos_arbre_men = cle_pos.split('_')
        x_m = int(pos_arbre_men[0])
        y_m = int(pos_arbre_men[1])
        
        if etat_menace[0] >= nbfeu :
            if randint(1,prec)/prec < rule[2] :
                arbre_feu = True
        if etat_menace[1] >= nbfeu :
            if randint(1,prec)/prec < rule[3] :
                arbre_feu = True
        if etat_menace[2] >= nbfeu :
            if randint(1,prec)/prec < rule[1] :
                arbre_feu = True
        if etat_menace[3] >= nbfeu : 
            if randint(1,prec)/prec < rule[4] :
                arbre_feu = True
        if etat_menace[4] >= nbfeu + decalage :
            if randint(1,prec)/prec < rule[0]:                           
                arbre_feu = True

        if arbre_feu:
            terre[x_m][y_m] = 7
            menaces_n.append(((x_m,y_m),7))
    for pos, etat in menaces:  
        i = pos[0]
        j = pos[1]  
        ### feu force 2 => feu force 1
        if etat == 7: 
            terre[i][j] = 6
            menaces_n.append(((i,j),6))
        ### feu force 1 => cendres force 2
        elif etat == 6 : 
            terre[i][j] = 5
            menaces_n.append(((i,j),5))
        ### cendre force 2 => cendre force 1
        elif etat == 5 : 
            terre[i][j] = 4
            menaces_n.append(((i,j),4))
        ### cendre force 1 => mur
        elif etat == 4 : terre[i][j] = 1
    return terre, menaces_n



""" truc on sait pas ce que c'est 
            etat_foret['arbres_brules'] = etat_foret['murs'] - cloture
            etat_foret['total_arbres'] =  etat_foret['arbres_brules'] + etat_foret['arbres_sains'] + etat_foret['feu_force_2'] +  etat_foret['feu_force_1'] \
            + etat_foret['cendre_force_2'] + etat_foret['cendre_force_1']  
            print(f"{'':>10}Feu force2: {etat_foret['feu_force_2']} -- Feu force1: {etat_foret['feu_force_1']} -- Cendres force2: {etat_foret['cendre_force_2']}-- Arbres brulés:  {etat_foret['arbres_brules']}")
"""










