from TP_1.Application_2 import Print_Upper

def TraitementTitre(Donnee):
    if Donnee == "1":
        return "Madame"
    elif Donnee == "2":
        return "Monsieur"
def TraitementTitre2(Donnee):
    if Donnee == "1":
        return "Elle"
    elif Donnee == "0":
        return "Il"

def TraitementDomaine(Donnee):
    if Donnee == "0":
        return "direction"
    elif Donnee == "1":
        return "secretariat"
    elif Donnee == "2":
        return "gestion"
    elif Donnee == "3":
        return "informatique"
    elif Donnee == "4":
        return "communication"
    elif Donnee == "5":
        return "entretien"
    elif Donnee == "6":
        return "fabrication"
def Code_Annee_Embauche(Annee):
    if Annee>"56":
        return "19"+Annee
    elif Annee<="21":
        return "20"+Annee

def Code_Entreprise():
    Nom=input("Notez le Nom \n")
    Prenom=input("Notez le prenom \n")
    Code=input("Notez le code \n")
    if not Code.isnumeric():
        Code_Entreprise()
    if len(Code) != 8:
        print("Désolé, les coordonnées sont érronné")
    if Code[:3] > "21":
        if Code[:3] < "56":
            print("désolé, date d'embauche impossible après 2021")
            Code_Entreprise()
    resultat = TraitementTitre(Code[6]) + " " + Prenom + " " + Print_Upper(Nom)+ " travaile au service " + TraitementDomaine(Code[7]) + ". " + TraitementTitre2(Code[6]) + " travaille dans l'entreprise depuis " + Code_Annee_Embauche(Code[:2]) + " et son numéro d'embauche est le " + Code[2:6]

    return resultat

print(Code_Entreprise())
