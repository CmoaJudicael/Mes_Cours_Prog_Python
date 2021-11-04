from Ressource.StringSaisie import String_Saisie
voyelles = "aeiouyAEIOUY"

def isVoyelle(lettre):
    if lettre in voyelles:
        print("c'est une voyelle.")
    else:print("c'est une consonne")

def Envoie_Saisie():
    mot = String_Saisie("Veuillez entrez une lettre seule \n")
    if len(mot) != 1:
        Envoie_Saisie()
    else: return mot

def jeuDeLaLettre():
    isVoyelle(Envoie_Saisie())

jeuDeLaLettre()
