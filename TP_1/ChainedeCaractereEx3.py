from Ressource.StringSaisie import String_Saisie

def Hash_Mot():
    i = 0
    mot = String_Saisie("veuillez entrez un mot \n")
    nouveau_mot = ""

    for i in range(len(mot)-2):
        nouveau_mot = nouveau_mot+mot[i] + "#"

    nouveau_mot = nouveau_mot + mot[(len(mot)-1)]
    print(nouveau_mot)


Hash_Mot()
