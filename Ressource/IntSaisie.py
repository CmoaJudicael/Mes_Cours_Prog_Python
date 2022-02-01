def Int_Saisie(consigne):
    verif = True
    while verif:
        nombre = input(consigne+"\n")
        if (nombre.isnumeric()):
            return int(nombre)
        else:continue
