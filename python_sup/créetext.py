import pygame as py
from random import randint
import module_TIPE as m
py.init()

#imageavant = "martigues-bavfin2.jpg"

imageavant = "foretavant-martigues.jpg"
imageapres = "finsurdébut.jpg"
NBCARRE = 300
ROUGE = (255,0,0)

def code (version,A) :
    if version == 2 and A[0] == 255 and A[1] == 0 and A[2] == 0 :
        return(1)

    else:
        if A[0] <= 80 and A[1] <= 80 and A[2] <= 80 and A[1] >= A[0] and A[1] >= A[2] :
            return(3)
        else : return(0)


def Selection(NomFich,l, foretavant):
    LARGEUR_SORTIE = l

    foret  = py.image.load(NomFich)
    taille = foret.get_size()
    a,b = taille

    #taille choisie de 600 pour simplifier, mais réglable à terme
    b2 = 600*b // a

    #foret  = py.transform.scale(foret,(600,b2))
    fenetre = py.display.set_mode((600,b2), py.SHOWN)
    m.affichage(fenetre,foretavant)

    #fenetre.blit(foret,(0,0))

    py.display.flip()

    A=True
    py.key.set_repeat(10,0)
    while A :
        for event in py.event.get() :
            if event.type == py.QUIT :
                A = False
            if event.type == py.KEYDOWN and event.key == py.K_ESCAPE:
                A = False
            if event.type == py.KEYDOWN and event.key == py.K_SPACE:
                A = False
            if  event.type == py.KEYDOWN and event.key == py.K_a:
                x,y=py.mouse.get_pos()
                couleur=foret.get_at((x,y))
                py.draw.circle(fenetre,ROUGE,[x,y],10)
                py.display.flip()
            if event.type == py.MOUSEBUTTONDOWN :
                if event.button == 1 :
                    x,y=event.pos
                    couleur=foret.get_at((x,y))
                    py.draw.circle(fenetre,ROUGE,[x,y],35)
                    py.display.flip()

    if a < LARGEUR_SORTIE : LARGEUR_SORTIE = a
    HAUTEUR_SORTIE = (b*LARGEUR_SORTIE)//a

    pas_largeur = a / LARGEUR_SORTIE
    pas_hauteur = b / HAUTEUR_SORTIE

    CARRE = a // LARGEUR_SORTIE

    terre = [[0 for j in range (LARGEUR_SORTIE)] for i in range (HAUTEUR_SORTIE)]

    pl = pas_largeur // 2
    ph = pas_hauteur // 2

    for i in range (HAUTEUR_SORTIE) :
        for j in range (LARGEUR_SORTIE) :
            terre[i][j]=code(2,fenetre.get_at((int((pl+(j*pas_largeur))/a *600),int((ph+(i*pas_hauteur))/b *b2))))


    for k in range (len(terre)):
        terre[k][0]  = 1
        terre[k][1]  = 1
        terre[k][-1] = 1
        terre[k][-2] = 1

    for k in range (len(terre[0])):
        terre[0][k]  = 1
        terre[1][k]  = 1
        terre[-1][k] = 1
        terre[-2][k] = 1

    return(terre)



def Numerisation(NomFich,l):
    LARGEUR_SORTIE = l

    foret  = py.image.load(NomFich)
    taille = foret.get_size()

    a,b = taille
    if a < LARGEUR_SORTIE : LARGEUR_SORTIE = a

    HAUTEUR_SORTIE = (b*LARGEUR_SORTIE)//a

    pas_largeur = a / LARGEUR_SORTIE
    pas_hauteur = b / HAUTEUR_SORTIE

    CARRE = a // LARGEUR_SORTIE

    terre = [[0 for j in range (LARGEUR_SORTIE)] for i in range (HAUTEUR_SORTIE)]

    for i in range (HAUTEUR_SORTIE) :
        for j in range (LARGEUR_SORTIE) :
            pl = pas_largeur // 2
            ph = pas_hauteur // 2

            terre[i][j]=code(1,foret.get_at((int(pl+(j*pas_largeur)),int(ph+(i*pas_hauteur)))))

    for k in range (len(terre)):
        terre[k][0]  = 1
        terre[k][1]  = 1
        terre[k][-1] = 1
        terre[k][-2] = 1


    for k in range (len(terre[0])):
        terre[0][k]  = 1
        terre[1][k]  = 1
        terre[-1][k] = 1
        terre[-2][k] = 1

    l_f = CARRE*LARGEUR_SORTIE
    h_f = CARRE*HAUTEUR_SORTIE

    return(terre, CARRE, l_f, h_f)

def sauverCSV (NomFich,T):
    f = open(NomFich,"w")
    for lgn in range(len(T)) :
        for k in range (len(T[lgn])):
            f.write(str(T[lgn][k]))
            if k == len(T[lgn])-1:
                if lgn != len(T)-1 :
                    f.write("\n")
    f.close


AV = Numerisation(imageavant, NBCARRE)[0]


AP = Selection(imageapres, NBCARRE, AV)






## création terre_brulee final
terrebrul =[ [0 for j in range(300) ]  for i in range(329) ]


for i in range(329):
    for j in range(300):
        if AP[i][j] == 1 :
            if AV[i][j]!=0 :
                terrebrul[i][j] = 1
        else :
            terrebrul[i][j] = AV[i][j]


sauverCSV("foretavant.txt",AV)

A= input("ENREGISTRER ? ( True or False )")
if A :
    sauverCSV("foretbrulee.txt",terrebrul)

py.quit()

