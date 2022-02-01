from tkinter import *
from time import sleep
import random

fenetre = Tk()


def create_grille( largeur, longueur):
    grille = [[[0 for k in range(3)] for j in range(longueur)] for i in range(largeur)]
    return  grille
def create_check( largeur, longueur):
    checkGrille = [[[0 for n in range(3)] for m in range(longueur)] for l in range(largeur)]
    return checkGrille
def create_item( largeur, longueur):
    itemCanvas=[[0 for p in range(longueur)] for o in range(largeur)]
    return itemCanvas

def selectionAleatoire(largeur, longueur, grille):
    _yPos = 0
    _xPos = 0
    for i in range(largeur):
        _xPos=0
        for j in range(longueur):
            alive = random.randint(0, 1)
            grille[i][j][0] = alive
            grille[i][j][1] = _xPos
            grille[i][j][2] = _yPos
            _xPos += 30
        _yPos += 30
def isAlive(i, j, grille):
    if (grille[i][j][0] == 1):
        return True
    else:
        return False
def countCells(i, j, grille):
    count = 0
    if (i - 1 >= 0):
        if (grille[i - 1][j][0] == 1):
            count += 1
        if (j + 1 < len(grille[i])):
            if (grille[i - 1][j + 1][0] == 1):
                count += 1
        if (j - 1 >= 0):
            if (grille[i - 1][j - 1][0] == 1):
                count += 1
    if (i + 1 < len(grille)):
        if (grille[i + 1][j][0] == 1):
            count += 1
        if (j + 1 < len(grille[i])):
            if (grille[i + 1][j + 1][0] == 1):
                count += 1
            if (grille[i + 1][j - 1][0] == 1):
                count += 1
            if (grille[i][j - 1][0] == 1):
                count += 1
    if (j + 1 < len(grille[i])):
        if (grille[i][j + 1][0] == 1):
            count += 1
    return count
def modifState( largeur, longueur, grille, checkGrille):
    for i in range(largeur):
        for j in range(longueur):
            if ((countCells(i, j, grille) == 3) or (isAlive(i, j, grille) and countCells(i, j, grille) == 2)):
                checkGrille[i][j][0] = 1
            else:
                checkGrille[i][j][0] = 0
    for i in range(largeur):
        for j in range(longueur):
            grille[i][j][0] = checkGrille[i][j][0]
def addRectangle(canvas, color, i, j, grille):
    x2= grille[i][j][1] + 30
    y2=grille[i][j][2] + 30
    canvas.create_rectangle(grille[i][j][1], grille[i][j][2], x2, y2, fill=color)
def changeRectangle(canvas, color, i, j, itemCanvas):
    rect = itemCanvas[i][j]
    canvas.itemconfig(rect, fill=color)
def resetCanvas(cnv):
    cnv.delete('all')
def remplissageCellule(cnv, largeur, longueur, grille):
     for i in range(largeur):
            for j in range(longueur):
                choixColor = grille[i][j][0]
                if (choixColor == 1):
                    addRectangle(cnv, 'black', i, j, grille)
                else:
                    addRectangle(cnv, 'white', i, j, grille)
            cnv.pack()
def buttonStartAleaGame(cnv, nbrEtape, largeur, longueur, typePartie):
    etape=convert_to_int(nbrEtape, cnv)
    larg=convert_to_int(largeur, cnv)
    long=convert_to_int(longueur, cnv)
    if larg>20:
        larg = 20
    if long > 20:
        long = 20
    cnv.delete()
    canvas = Canvas(fenetre, width=1200, height=800, bg="ivory")
    canvas.pack(padx=0, pady=0)
    mainGame(canvas, etape, larg, long, typePartie)
def buttonStartGame():
    print("code")
def convert_to_int(string, cnv):
    try:
        result = int(string)
        return result
    except ValueError:
        if string!="\x08" and string!="":
            resetCanvas(cnv)
            mainPage()

def mainGame(cnv, nbrEtape, largeur, longueur, typePartie):
    count = 0
    grille=create_grille( largeur, longueur)
    checkGrille = create_check( largeur, longueur)
    itemCanvas = create_item( largeur, longueur)
    resetCanvas(cnv)
    if(typePartie=='alea'):
        selectionAleatoire(largeur, longueur, grille)
    remplissageCellule(cnv, largeur, longueur, grille)
    while count < nbrEtape :
        sleep(1)
        resetCanvas(cnv)
        remplissageCellule(cnv, largeur, longueur, grille)
        fenetre.update()
        modifState( largeur, longueur, grille, checkGrille)
        count += 1

def mainPage():
    cnv = Canvas(fenetre, width=1200, height=800, bg="ivory")
    cnv.pack(padx=0, pady=0)
    Label(cnv, text="JEU DE LA VIE", font=('Helvetica bold', 25), fg="black").pack(pady=20)
    largeurTabLabel = Label(cnv, text = "Largeur tableau (max 20 cases)")
    largeurTab= Entry(cnv)
    largeurTab.insert(END, '20')
    longeurTabLabel = Label(cnv, text = "Longeur tableau (max 20 cases)")
    longeurTab= Entry(cnv)
    longeurTab.insert(END, '20')
    nbrEtapeLabel = Label(cnv, text = "nombre d'étape")
    nbrEtape= Entry(cnv)
    nbrEtape.insert(END, '1000')
    buttonAlea = Button(text ="Demarrer avec une configuration aleatoire", command=lambda:buttonStartAleaGame(cnv, nbrEtape.get(), largeurTab.get(), longeurTab.get(), 'alea'))
    buttonAlea.pack()
    button = Button(text="Demarrer avec une partie", command=buttonStartGame)
    button.pack()
    largeurTabLabel.pack()
    largeurTab.pack()
    longeurTabLabel.pack()
    longeurTab.pack()
    nbrEtapeLabel.pack()
    nbrEtape.pack()
mainPage()
fenetre.mainloop()
