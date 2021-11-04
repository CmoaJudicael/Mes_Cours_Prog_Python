def Conversion(Nombre):
    resultat = 0
    j = len(Nombre)
    print(Nombre)

    i = 0
    while j>0:
        if Nombre[i].isnumeric():
            resultat += int(Nombre[i]) * (16 ** (j-1))
        elif Nombre[i] == "A":
            resultat += 10 * (16 **(j-1))
        elif Nombre[i] == "B":
            resultat += 11 * (16 **(j-1))
        elif Nombre[i] == "C":
            resultat += 12 * (16 **(j-1))
        elif Nombre[i] == "D":
            resultat += 13 * (16 **(j-1))
        elif Nombre[i] == "E":
            resultat += 14 * (16 **(j-1))
        elif Nombre[i] == "F":
            resultat += 15 * (16 **(j-1))
        i+=1
        j-=1
    return resultat

def Verif_Nombre():
    verif = "0123456789ABCDEF"
    Boolean = False
    Nombre = ""
    while (not Boolean):
        Nombre = input("veuillez saisir un nombre hexadécimal\n")
        Boolean = True
        for ch in Nombre:
            if ch in verif:
                continue
            else:
                print("Ceci n'est pas un nombre hexadécimal, chiffre et lettre : 0123456789ABCDEF\n")
                Boolean = False

    return Nombre

print("Le résultat est " + str(Conversion(Verif_Nombre())))
