def Verif_MOT():
    Boolean = False
    Nombre = ""
    while (not Boolean):
        result=""
        Nombre = input("veuillez saisir un Mot sans chiffre :\n")
        for ch in Nombre:
            if(ch.isnumeric()):
                Boolean=False
                break
            else:
                result+=ch.capitalize()
                Boolean=True
    return result

Cr=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def CryptageEucli26(mot):
    result=""
    i=0
    j=0
    for j in range(0,len(mot)):
        for i in range(0,26):
            if (mot[j] == Cr[i]):
                result+=Cr[DivEucli26(i)]

    return result
def DeCryptageEucli26(mot):
    result=""
    i=0
    j=0
    for j in range(0,len(mot)):
        for i in range(0,26):
            if (mot[j] == Cr[i]):
                result+=Cr[Decrip(i)]

    return result
def Decrip(a):
    a=5*(a-11)
    while(a<0):
        a+=26
    return a
def DivEucli26(a):
    b=26
    c=0
    a=21*a+11
    while(a>=b):
        c+=1
        a-=b
    return a

stop=True
arret=True

while (stop):
    while (arret):
        mot = input("Voulez vous Crypter [C] ou Décrypter[D] un mot?")
        if(len(mot)!=1):
            print("Veuillez entrez qu'une seule lettre")
            continue
        if(mot.capitalize()=="C"):
            print("Quel mot souhaitez vous crypter?")
            motACrypter=Verif_MOT()
            print(CryptageEucli26(motACrypter))
            break
        elif(mot.capitalize()=="D"):
            print("Quel mot souhaitez vous décrypter?")
            motACrypter=Verif_MOT()
            print(DeCryptageEucli26(motACrypter))
            break
        else:
            print("Je ne comprend pas votre saisie, recommencez")
    while (arret):
        mot = input("Voulez vous Quittez [Q] ou Recommencer[R]?")
        if(len(mot)!=1):
            print("Veuillez entrez qu'une seule lettre")
            print("Voulez vous Quittez [Q] ou Recommencer[R]?")
            continue
        if(mot.capitalize()=="Q"):
            stop=False
            break
        elif(mot.capitalize()=="R"):
            break
        else:
            print("Je ne comprend pas votre saisie, recommencez")






