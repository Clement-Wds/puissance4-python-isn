from tkinter import*
from math import*
import random


fen = Tk()
fen.title("Puissance 4")
fen.geometry("800x800")


dessin = Canvas(fen,height=800,width=800,bg="white")
dessin.grid()


i = 1
while i <= 7 :
    dessin.create_line(100,i*100,700,i*100,fill="blue")
    dessin.create_line(i*100,100,i*100,700,fill="blue")
    i = i + 1


T = 6 * [0]
for i in range(6):
  T[i] = 6 * [0]


def pos_colone(a) :
    if (a>=0 and a<100) or (a>=700 and a<800) :   ## evt.x correspond à l'abscisse du clic de la souris en pixel)
            return -1
    else:
        for i in range(6) :
            if a>=(100*(5-i)+100) :
                return 5-i


def ligne(a) :
     if a != -1 :                                   ## -1 corespond a un clic dans les marges
        for j in range(6) :
            if T[j][a] != 0 :                       ## j : colone du tableau et a : ligne du tableau
                return j - 1
        return 5


def jouer(evt) :
    global cpt
    abspion = pos_colone(evt.x)  ##numéro colone pion
    ordpion = ligne(abspion)  ##numéro ligne pion
    abspixel = (pos_colone(evt.x) * 100 ) +150    ## evt.x correspond à l'abscisse du clic de la souris en pixel -> ici on centralise sur la colone l'abcsisse en pixel
    ordpixel = (ordpion * 100 ) +150         ## evt.y correspond à l'ordonné du clic de la souris en pixel -> ici on cetralise sur la ligne l'ordonnée en pixel
    r = 100/2-20
    if (abspion >= 0 and abspion <= 5) and (ordpion >= 0 and ordpion <= 5):  ## si la position du clic est comprise dans le tableau de jeu alors jouer -> palcer le pion et executer la fonction gagner
        cpt = cpt + 1
        if cpt % 2 :
            dessin.create_oval(abspixel-r,ordpixel-r,abspixel+r,ordpixel+r,outline="yellow",fill="yellow")
            T[ordpion][abspion] = 20
        else :
            dessin.create_oval(abspixel-r,ordpixel-r,abspixel+r,ordpixel+r,outline="red",fill="red")
            T[ordpion][abspion] = 1
        for i in range(6) :
            print(T[i],"\n")
        gagner()


def gagner():
    cptd1 = 1
    cptd2 = 1
    cptd3 = 1
    cptd4 = 1
    cptd5 = 1
    cptd6 = 1
    cptd7 = 1
    cptd8 = 1
    cptd9 = 1
    cptd10 = 1
    cptd11 = 1
    for i in range(6):
        cptl = 1
        cptc = 1
        for j in range(6):
            cptl = cptl + T[i][j]
            cptc = cptc + T[j][i]
        if cptl == 81 or cptc == 81 :
            print("Le joueur 1 a gagné")

        elif cptl == 5 or cptc == 5 :
            print("Le joueur 2 a gagné")
        cptd1 = cptd1 + T[i][i]   ## de 6.1 à 1    colonne.ligne
        cptd2 = cptd2 + T[i][1-i] ## de 3 à 6
        cptd3 = cptd3 + T[i][5-i] ## de 1.1 à 6
        cptd4 = cptd4 + T[i][4-i] ## de 1.2 à 6
        cptd5 = cptd5 + T[i][3-i] ## de 1.3 à 6
        cptd6 = cptd6 + T[i][i-1] ## de 5 à 1
        cptd7 = cptd7 + T[i][i-2] ## de 4 à 1
        cptd8 = cptd8 + T[i][i-4] ## de 6.3 à 1
        cptd9 = cptd9 + T[i][i-5] ## de 6.2 à 1
        cptd10 = cptd10 + T[i][0-i] ## de 2 à 5

    if cptd1 == 81 or cptd2 == 81 or cptd3 == 81 or cptd4 == 81 or cptd5 == 81 or cptd6 == 81 or cptd7 == 81 or cptd8 == 81 or cptd9 == 81 or cptd10 == 81:
        print("Le joueur 1 a gagné")
    elif cptd1 == 5 or cptd2 == 5 or cptd3 == 5 or cptd4 == 5 or cptd5 == 5 or cptd6 == 5 or cptd7 == 5 or cptd8 == 5 or cptd9 == 5 or cptd10 == 5:
        print("Le joueur 2 a gagné")




dessin.bind("<Button-1>",jouer)
cpt = 0

fen.mainloop()