import math
def nombrepremierinf(n):
    d=2
    resultat = ""
    while d<(n+1):
        if premier(d):
            resultat+=f"{d}, "
        d+=1
    return resultat


def premier(n):
    resultat = False
    for d in range(2,int(math.sqrt(n))+1):
        if n%d == 0:
            resultat = False
            break
        else:
            resultat = True
            continue
    if n == 3:
        resultat = True
    elif n == 2:
        resultat = True

    return resultat

def Verif_Nombre():
    Boolean = False
    Nombre = ""
    while (not Boolean):
        Nombre = input("veuillez saisir un nombre :\n")
        Boolean = True
        for ch in Nombre:
            if ch.isnumeric():
                continue
            else:
                print("Ceci n'est pas un nombre, chiffre : 0123456789\n")
                Boolean = False
                break

    return int(Nombre)

print(nombrepremierinf(Verif_Nombre()))
