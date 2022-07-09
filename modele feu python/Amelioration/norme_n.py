# coding: utf8
# Norme

# taille fenetre :
import numpy as np
import pygame as py
import module_TIPE_n as m
from random import randint
import time

# Paramètres de diffusion du feu
# rule =[1, 1, 1, 1, 1, 1]
# rule =[1, 1, 1, 1, 1, 0]
# rule = [0.25 for k in range(5)]
rule = [ 1 , 0 , 0 , 0 , 0 ]
#pb dans les rules 3 et 5 (j'ai vérifié)


croix = [(0,0),(-1,0),(1,0),(0,-1),(0,1),
         (0, 2),(-2, 0),(0,-2),(2, 0)]
         
# initialisation de pygame
py.init()

# Initialisation de la fenetre graphique avec son nom
py.display.set_caption("Animation feu de forets")

    
# création de la list
def creatlist(nom,e):
    fich = open(nom,"r")
    list = []
    j = 0
    for lgn in fich:
        s = lgn.strip()
        l = []
        for i in range(len(s)):
            val = int(s[i])
            l.append(val)   
        list.append(l)
        j+=1
    fich.close
    return(list)

terre = creatlist("foretavant.txt",'Avant')
terrebrul = creatlist("foretbrulee.txt",'Apres')

l = len(terre)
h = len(terre[0])

fenetre = py.display.set_mode((m.CARRE*h,m.CARRE*l), py.SHOWN )

#print(f"Nombre d'éléments de forêt modélisés: {l*h}")
print(f'Paramètres de diffusion du feu: {rule}')

# Bilan initial :

## Boucle d'initialisation du feu
A = True
B = True
menaces = []# Initialisation menaces
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
                ### Affichage à Enlever
                #print("a=",a," b=",b)
                a=111
                b=150

                # zone initiale de déclenchement d'un feu (croix)
                for x,y in croix:                
                    if  terre[a+x][b+y] == 3:
                        terre[a+x][b+y] = 7 
                        # menaces contient les cases en feu
                        menaces.append(((a+x,b+y),7))                    
                
    m.affichage(fenetre,terre)
    py.display.flip()

FINISH = True
compt = 0
## Générations
while FINISH :
    if not B :
        FINISH = False
    
    #men_feu_nouv = []
    for event in py.event.get() :
        # conditions d'arrets de l'initialisation
        if event.type == py.QUIT :
            FINISH = False
        if event.type == py.KEYDOWN and event.key == py.K_SPACE :
            FINISH = False
        if event.type == py.KEYDOWN and event.key == py.K_ESCAPE:
            FINISH = False
        elif event.type == py.MOUSEBUTTONDOWN :
            b,a = event.pos
            a,b = int(a//m.CARRE) , int(b//m.CARRE)

            # zone de déclenchement nouveau feu (croix)
            cpt = 0
            for x,y in croix :
                if  terre[a+x][b+y] == 3:
                    terre[a+x][b+y] = 7  
                    menaces.append(((a+x,b+y),7))
                    
    terre, menaces = m.gen(terre, rule, menaces) 
    #print(menaces)  
    
    if menaces != [] :
        # affichage numéro génération
        compt += 1
        if compt == 1 : debut_traitement = time.time()
        if compt%20 == 0 :
            if compt == 20 :
                t_20pas = time.time()-debut_traitement
            else:
                  t_20pas = time.time()-fin_20pasprel
            fin_20pasprel = time.time()
            print(f'NOMBRE DE PAS DE CALCUL: {compt} les 20 pas précédents ont été effectués en {t_20pas}')
            
    else: #executer à la fin quand il n'y a plus de menaces !
        duree_traitement = time.time()-debut_traitement
        minutes = duree_traitement // 60
        secondes = round(duree_traitement - minutes*60,3)
        print(f"Simulation réalisée en {minutes}mn {secondes}s")
        FINISH = False
    
    m.affichage(fenetre,terre)
    py.display.flip()
py.quit()


N1 = np.array(terre)
N2 = np.array(terrebrul)
NORME = np.linalg.norm(N2-N1)

print(NORME)