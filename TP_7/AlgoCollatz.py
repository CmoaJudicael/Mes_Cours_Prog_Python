def suivant(n):
    if n == 1 :
        return 1
    else:
        if n%2 == 0 :
            return int(n/2)
        else:
            return int(n*3 + 1)


def collatz(n):
    c = 0
    while(n!=1):
        c+=1
        n = suivant(n)
    return c


def Max(n):
    max = n
    while suivant(n) != 1:
        n = suivant(n)
        if n > max :
            max = n
    return max
def Liste(n):
    L = [n]
    while suivant(n)!= 1:
        n = suivant(n)
        L.append(n)
    L.append(suivant(n))
    return L

def Algo():
    print("***Algorithme lancé***")
    n = int(input("entrer n :\n"))
    print("nombre d'étape :\n "+str(collatz(n)))
    print("La plus grande valeur est :\n"+str(Max(n)))
    L = Liste(n)
    print("La liste des nombres rencontrés est :")
    for i in L :
        print(str(i)+" ", end="")
    print("\n***L'algorithme est terminé***")
def AlgoFlash():
    print("***Algorithme lancé***")
    nbrEtape = int(input("Nombre d'étape souhaité :\n"))
    print("Nombre d'étape : "+str(nbrEtape))
    n = 2
    while collatz(n) != nbrEtape :
        n += 1
    print("N = "+str(n))
    print("La plus grand nombre rencontré : "+str(Max(n)))
    print("\n***L'algorithme est terminé***")




Algo()
AlgoFlash()
