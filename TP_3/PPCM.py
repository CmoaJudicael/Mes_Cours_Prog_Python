import math
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


def DivisionEuclidienne(a,b):
    resA=a
    resB=b
    if a<b:
        c=a
        a=b
        b=c
    count=0
    while (True):
        count+=1
        r=a%b
        if r==0:
            PGCD=b
            break
        else:
            a=b
            b=r
    return PGCD

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

def CalculPPCM():
    print("Valeur a :")
    a=Verif_Nombre()
    print("Valeur b :")
    b=Verif_Nombre()
    PPCM= ((a*b)/DivisionEuclidienne(a,b))
    return f"PPCM({a},{b}) = {PPCM}\n"


print(CalculPPCM())

