import math


def premierPythagore(n):
    resultat = False
    res = f"Le nombre {n} est premier"
    d=1
    f=1
    while d < int(math.sqrt(n)):
        d+=1
        if n%(d) == 0:
            resultat = False
            res = f"Le nombre {n} n'est pas premier, il est divisible par {d}"
            break
        else:
            resultat = True
            res = f"Le nombre {n} est premier\n"
            if n == (4*int(n/4) + 1):
                res+=f"{n} est un nombre premier de pytagore"
            continue
    return res

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

print(premierPythagore(Verif_Nombre()))
