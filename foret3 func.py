import module_TIPE as m
from random import randint


# à faire pour obtenir une fonction utilisable
# enlever les récupérations de clics du claviers
# enlever l'attente qui permettait de faire un affichage graphique clair
# peut etre meme enlever l'interface graphique tout court ...
def foret3():
    # prend en argument le nombre d'iteration
    #for i in range(nbit)

    # coding: utf8

    ### Iniatilisation choix situation de départ :

    terre = [[0]*m.NBCARRE for i in range(m.NBCARRE)]

    # Variables initialisation
    # pourcentage de foret
    pforet = 75
    terre = random3(terre,pforet)
    a , b = len(terre)//2,len(terre)//2
    terre[a][b] = 7
    for x,y in m.adjacent : terre[a+x][b+y]=7

    ## Générations
    for x in range(10*len(a)**2):
        terre = m.gen3(terre)

    compt=0
    for i in range(len(a)):
        for j in range(len(b)):
            if terre[i][j]==0: compt+=1
    statfinal=100(1-compt/len(terre)**2)

    return(statfinal)


def StatRegle(nbiteration):
    for i in range(nbiteration)
    foret3()

