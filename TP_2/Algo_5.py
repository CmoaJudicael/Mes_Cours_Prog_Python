import math
def Goldbach(n):
    for x in range(2,n):
        if premier(x):
            for y in range(2,n):
                if premier(y):
                    if n==(y+x):
                        print(f"{n}={x} + {y}")





def premier(n):
    resultat = False
    for d in range(2,int(math.sqrt(n))+1):
        if n%d == 0:
            resultat = False
            break
        else:
            resultat = True
            continue
    if n==3:
        resultat = True
    elif n==2:
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

Goldbach(Verif_Nombre())
