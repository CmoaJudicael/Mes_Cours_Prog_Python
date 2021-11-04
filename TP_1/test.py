n = input("Entrez votre code personel: ")
name = input("entrer votre Nom svp:")
def info(name,n,annee, num_embauche,genre,domaine,end=""):
    profession = {0: "direction", 1: "secretariat", 2: "gestion", 3: "informatique", 4: "communication",
                  5: "l'entretien",
                  6: "fabrication"}
    if int(genre) == 1:
        print("Madame:  " + name + " Elle travaille")
    elif int(genre) == 2:
        print("Monsieur: " + name + "Il travaille")
    # else:
    # print("Le numéro que vous avvez rentré est érronée")
    if int(domaine) in profession.keys():
        print(profession.get(int(domaine)))

    if int(annee) <= 2021:  # and int(annee) > 51:
        print(" dans l'entreprise depuis 20" + annee + " Et son numero d'embauche est " + num_embauche)

info(name, n, annee=n[0:2], num_embauche=n[2:6], genre=n[6], domaine=n[7], end="")
