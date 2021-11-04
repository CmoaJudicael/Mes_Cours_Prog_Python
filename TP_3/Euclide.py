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
    return f"Le PGCD de {resA} et de {resB} est de {PGCD}\nIl y a eu {count} boucle"


print(DivisionEuclidienne(Verif_Nombre(),Verif_Nombre()))
