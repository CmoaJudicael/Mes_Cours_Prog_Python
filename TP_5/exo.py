import random


def nombre_aleatoire():
    return random.randint(3,18)

def creer_tableau(a):
    tableau=[]
    for i in range (int(a)):
        tableau.append(nombre_aleatoire())
    return tableau
def tri_croissant_tableau(tableau):
    check = True
    while check:
        for i in range(len(tableau)):
            if (i+1) < len(tableau):
                if tableau[i] < tableau[i+1]:
                    temp = tableau[i]
                    tableau[i] = tableau[i+1]
                    tableau[i+1] = temp
                    check = True
                    break
                else:
                    check=False
    return tableau

def tri_decroissant_tableau(tableau):
    check = True
    while check:
        for i in range(len(tableau)):
            if (i+1) < len(tableau):
                if tableau[i] > tableau[i+1]:
                    temp = tableau[i]
                    tableau[i] = tableau[i+1]
                    tableau[i+1] = temp
                    check = True
                    break
                else:
                    check=False
    return tableau
def moyenne_tableau(tableau):
    moyenne=0
    for i in range(len(tableau)):
        moyenne+=tableau[i]
    moyenne= moyenne/len(tableau)
    return moyenne
def mediane_tableau(tableau):
    if len(tableau)%2==0:
        mediane = (tableau[int(len(tableau)/2)-1]+tableau[int((len(tableau)/2))])/2
    else:
        mediane = tableau[int((len(tableau))/2)]
    return mediane

mon_tableau = creer_tableau(input('longueur du tableau :'))

print(mon_tableau)

mon_tableau = tri_croissant_tableau(mon_tableau)
print(mon_tableau)

mon_tableau = tri_decroissant_tableau(mon_tableau)
print(mon_tableau)

print('moyenne : '+str(moyenne_tableau(mon_tableau)))

print('mediane : '+str(mediane_tableau(mon_tableau)))
