# coding: utf8
# Programme de test des regles de propagation
# on enlève l'interface graphique
# on garde que le calcul des generations

import module_TIPE as m
from random import randint

# on se place à la version 3
# pour pouvoir tester des regles
Version = 3

## à faire pour obtenir une fonction utilisable
# enlever les récupérations de clics du claviers
# enlever l'attente qui permettait de faire un affichage graphique clair
# peut etre meme enlever l'interface graphique tout court ...
def foret(pforet,rule):
    # prend en argument le nombre d'iteration
    #for i in range(nbit)

    ### Iniatilisation choix situation de départ :

    terre = [[0]*m.NBCARRE for i in range(m.NBCARRE)]

    # Variables initialisation
    # pourcentage de foret
    terre = m.random[Version](terre,pforet)
    a , b = len(terre)//2,len(terre)//2
    terre[a][b] = 7
    for x,y in m.adjacent : terre[a+x][b+y]=7

    ## Générations
    # boucle la plus longue
    for x in range(3*len(terre)):
        terre = m.gen[Version](terre,rule)

    compt=0
    for i in range(len(terre)):
        for j in range(len(terre)):
            if terre[i][j]==0: compt+=1
    statfinal = (compt / (len(terre)**2 -len(terre)*4-4 )) * 100
    return(statfinal)

## stat_rule
# rq : plus nbiteration plus la qualité du pourcentage est bon
# calcul le premier pourcentage de foret
# tel que "prctge" pourcent de foret à brulé
# en moyenne pour "nbiteration" programme foret3()
# avec la rule "rule"
def stat_rule(nbiteration, rule, prctge) :
    for i in range(26) :
        sum = 0
        for j in range(nbiteration) :
            sum += foret(i*2 + 50,rule)
        if sum/nbiteration >= prctge :
            return(i*2 + 50,rule)
    return("+100", rule)

# fonction très lourde qui prend du temps a être exécuté
def save_result(ens_rule,prctge):
    fichier = open("rule.txt", "a")
    compt = 0
    print(len(ens_rule),"regles à tester")
    fichier.write("\n")
    fichier.write("TEST règles V = "+str(Version)+" :"+"\n")
    for rule in ens_rule :
        result = stat_rule(5,rule,prctge)
        print(result)
        fichier.write(str(result))
        fichier.write("\n")

        # affichage de l'avancé du programme
        compt += 1
        print("regle : ",compt," => effectué")
    fichier.close()

# 0eme 1er regle  => arbres
# 2eme 3eme regle => arbres morts
# dans 1er et 3eme regle il y a les feu forces 2
# choix de l'ensemble des règles à tester
ens_rule = [
# echantillon témoin
# tjrs à +100
[4, 4, 4, 4 ],
# tjrs à 100
[3, 3, 3, 3 ],
# tjrs à env 75
[2, 2, 2, 2 ],
# tjrs à 50
[1, 1, 1, 1 ],

# celle avec des 4
[4, 3, 3, 2 ], [4, 3, 2, 1 ],

# que 1 / 2
[2, 2, 1, 1 ], [2, 2, 2, 1 ],

# vrai essai plausible
[3, 2, 2, 1 ],[3, 2, 1, 1 ],[3, 1, 3, 1 ],[3 ,2 ,3 ,2 ],[3 ,2 ,3 ,1 ]]

#save_result(ens_rule,95)
#save_result([[3,2,3,1]] ,95)

def f(pforet,rule):
    terre = [[0]*m.NBCARRE for i in range(m.NBCARRE)]
    terre = m.random[Version](terre,pforet)
    a , b = len(terre)//2,len(terre)//2
    terre[a][b] = 7
    for x,y in m.adjacent : terre[a+x][b+y]=7

    for x in range(3*len(terre)):
        terre = m.gen[Version](terre,rule)