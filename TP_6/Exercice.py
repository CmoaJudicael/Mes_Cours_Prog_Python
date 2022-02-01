from random import *


def Int_Saisie(consigne): #fonction qui n'a rien à voir avec l'exercice
    verif = True
    while verif:
        nombre = input(consigne+"\n")
        if (nombre.isnumeric()):
            return int(nombre)
        else:
            continue


# Exercice1
##########################


def remplissageAleaMatrice(ligne, colonne):
    matrice=[]
    for i in range(0,ligne):
        _liste=[]
        for j in range(0,colonne):
            _liste.append(randint(0,100))
        matrice.append(_liste)
    return matrice


# Exercice2
##########################


def SaisieCoefficients(ligne, colonne):
    matrice=[]
    for i in range(0,ligne):
        _liste=[]
        print("Coefficients de la ligne "+str(i+1))
        for j in range(0,colonne):
            _liste.append(int(input("Colonne "+str(j+1)+"\n")))
        matrice.append(_liste)
    return matrice


def affichezMatrice(matrice):#Exercice2
    print("Nombre de ligne : "+str(len(matrice))+"\n")
    print("Nombre de colonne : "+str(len(matrice[0]))+"\n")
    for i in range(0,len(matrice)):
        print("Coefficients de la ligne "+str(i+1))
        for j in range(0,len(matrice[i])):
            print("coefficients "+str(j)+" : "+str(matrice[i][j])+"\n")
    print(matrice)
    print("\n")


# Exercice3
##########################


def affiche_matrice(matrice):
    for i in range(0,len(matrice)):
        print(matrice[i])
    print("\n")


# Exercice4
##########################


def soustractionMatrice(matriceA, matriceB):
    matriceSoustraction=[]
    if(len(matriceA)==len(matriceB)):
        if (len(matriceA[0])==len(matriceB[0])):
            for i in range(0, len(matriceB)):
                _list=[]
                for j in range(0, len(matriceB[i])):
                    _list.append((matriceA[i][j] - matriceB[i][j]))
                matriceSoustraction.append(_list)
            return matriceSoustraction


def additionMatrice(matriceA, matriceB):
    matriceAddition = []
    if len(matriceA) == len(matriceB):
        if len(matriceA[0]) == len(matriceB[0]):
            for i in range(0, len(matriceB)):
                _liste = []
                for j in range(0, len(matriceB[i])):
                    _liste.append((matriceA[i][j] + matriceB[i][j]))
                matriceAddition.append(_liste)
            return matriceAddition


# Exercice5
##########################


def produitScalaireMatrice(matriceA, coefficientk_k):
    matriceScalaire = []
    for i in range(0, len(matriceA)):
        _liste = []
        for j in range(0, len(matriceA[i])):
            _liste.append((matriceA[i][j] * coefficientk_k))
        matriceScalaire.append(_liste)
    return matriceScalaire


# Exercice6
##########################


def Matrice_Negative(matrice):
    matriceNegative = []
    for i in range(0, len(matriceA)):
        _liste = []
        for j in range(0, len(matrice[i])):
            if matrice[i][j] == 1:
                _liste.append(0)
            else:_liste.append(1)
        matriceNegative.append(_liste)
    return matriceNegative


# Exercice7
##########################


def Matrice_Symetrique(matrice):
    matriceSymetrique = []
    for i in range(0, len(matriceA)):
        _liste = []
        for j in range((len(matrice[i])-1), -1, -1):
            _liste.append(matrice[i][j])
        matriceSymetrique.append(_liste)
    return matriceSymetrique


# Exercice8 -1
##########################


def produits_matrice( matriceA, matriceB):
    matrice_soustraction = []
    if len(matriceA[0]) == len(matriceB):
        for i in range(0, len(matriceA)):
            _list = []
            for j in range(0, len(matriceB[i])):
                coefficient = 0
                for k in range(0, len(matriceB)):
                    coefficient += matriceA[i][k] * matriceB[k][j]
                _list.append(coefficient)
            matrice_soustraction.append(_list)
    return matrice_soustraction


# Exercice8 -2
##########################


def puissance_matrice(matrice, n):
    if len(matrice) == len(matrice[0]):
        matrice_puissance = produits_matrice(matrice, matrice)
        for i in range(1, n-1):
            matrice_puissance = produits_matrice(matrice_puissance, matrice)
        return matrice_puissance


# Exercice8 -3
##########################


def Nombre_CheminsLongueurN(matrice, n):
    if len(matrice) == len(matrice[0]):
        matriceTemp = puissance_matrice(matrice, n)
        print("matrice M de puissance N :")
        affiche_matrice(matriceTemp)
        nombre_total_longeur=0
        for i in range(0, len(matriceTemp)):
            for j in range(0, len(matriceTemp[i])):
                nombre_total_longeur += matriceTemp[i][j]
                if matriceTemp[i][j] > 0 :
                    print("nombre de chemins de longueurs n du sommet "+str(i) + "/"+str(j) + " : "+ str(matriceTemp[i][j]) )
        print("nombre total de chemins de longueurs n : " + str(nombre_total_longeur))
    else:
        print("Désolé, mais la matrice n'est pas carré\n")


# Lancement des fonctions pour les tester
#
matriceA = [[1, 2, 0, -2], [3, 1, -2, -1], [1, 0, -2, 1]]
matriceB = [[0, 3, -1, -3], [5, 1, 1, 0], [-1, -3, 0, 1]]
affiche_matrice(soustractionMatrice(matriceA, matriceB))
affiche_matrice(additionMatrice(matriceA, matriceB))
print("matrice D :\n")
matriceD = produitScalaireMatrice(matriceA, (-1/2))
affiche_matrice(matriceD)

matriceE = soustractionMatrice(produitScalaireMatrice(matriceA,3),produitScalaireMatrice(matriceB,2))
print("matrice E :\n")
affiche_matrice(matriceE)

matriceM = [[0, 0, 1, 0], [0, 1, 1, 1], [0, 0, 0, 1]]
print("matrice M :\n")
affiche_matrice(matriceM)

matriceN = Matrice_Negative(matriceM)
print("matrice N :\n")
affiche_matrice(matriceN)

matriceP = Matrice_Symetrique(matriceM)
print("matrice P :\n")
affiche_matrice(matriceP)


matriceX = [[1, 2, 0, -2], [3, 1, -2, -1], [1, 0, -2, 1]]

matriceY = [[0, 3, -1], [5, 1, 1], [-1, -3, 0], [0, 6, 5]]

matriceZ = produits_matrice(matriceX, matriceY)
print("matrice Z :\n")
affiche_matrice(matriceZ)

matriceP = [[2, 0, 2, 0], [0, 1, 0, 1], [2, 0, 2, 0], [0, 1, 0, 1]]
matriceQ = puissance_matrice(matriceP, 15)
print("matrice Q :\n")
affiche_matrice(matriceQ)


print("nombre de chemins de longueurs de la MatriceA :\n")
Nombre_CheminsLongueurN(matriceA, 22)

print("nombre de chemins de longueurs de la MatriceP :\n")
Nombre_CheminsLongueurN(matriceP, 5)
