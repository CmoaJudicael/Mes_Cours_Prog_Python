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

def DivisionEuclidienne3Entier():
    print("Valeur a :")
    a=Verif_Nombre()
    print("Valeur b :")
    b=Verif_Nombre()
    print("Valeur c :")
    c=Verif_Nombre()
    PGCD=DivisionEuclidienne(DivisionEuclidienne(a,b),c)

    return f"Le PGCD de {a}, {b} et {c} est de {PGCD}\n"



print(DivisionEuclidienne3Entier())
