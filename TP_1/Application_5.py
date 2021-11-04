liste_Nombre_Binaire = []

def Conversion():
    Verif_Nombre()
    resultat = ""
    i=0
    j=0
    while  (len(liste_Nombre_Binaire)%4 != 0):
        liste_Nombre_Binaire.append(i)
    liste_Nombre_Binaire.reverse()
    for l in range(0,int((len(liste_Nombre_Binaire)/4))):
        temp = ""
        for li in liste_Nombre_Binaire[i:(i+4)]:
            temp += str(liste_Nombre_Binaire[j])
            j+=1
        if temp == '0000':
            resultat += "0"
        elif temp == '0001':
            resultat += "1"
        elif temp == '0010':
            resultat += "2"
        elif temp == '0011':
            resultat += "3"
        elif temp == '0100':
            resultat += "4"
        elif temp == '0101':
            resultat += "5"
        elif temp == '0110':
            resultat += "6"
        elif temp == '0111':
            resultat += "7"
        elif temp == '1000':
            resultat += "8"
        elif temp == '1001':
            resultat += "9"
        elif temp == '1010':
            resultat += "A"
        elif temp == '1011':
            resultat += "B"
        elif temp == '1100':
            resultat += "C"
        elif temp == '1101':
            resultat += "D"
        elif temp == '1110':
            resultat += "E"
        elif temp == '1111':
            resultat += "F"
        i+=4
        l+=1

    return resultat

def Verif_Nombre():
    verif = "01"
    Boolean = False
    Nombre = ""
    while (not Boolean):
        Nombre = input("veuillez saisir un nombre Binaire\n")
        Boolean = True
        for ch in Nombre:
            if ch in verif:
                liste_Nombre_Binaire.append(int(ch))
                continue
            else:
                print("Ceci n'est pas un nombre binaire, séquence de chiffre 0 ou 1\n")
                Boolean = False
    liste_Nombre_Binaire.reverse()


print("Le résultat en hexadécimal est " + Conversion())
