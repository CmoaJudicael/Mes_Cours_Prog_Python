Alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def algo1(lettre):
    rang=-1
    for ch in Alphabet:
        if(lettre==ch):
            rang=0
            while(Alphabet[rang]!=lettre):
                rang+=1
            break
    return rang

def Codage(mot):
    motCoder=""
    for ch in mot:
        rang=algo1(ch)
        if(rang==-1):
            motCoder+=ch
            continue
        rang+=13
        if(rang>25):
            rang=rang-26
        motCoder+=Alphabet[rang]
    return motCoder

def Decodage(motCoder):
    mot=""
    for ch in motCoder:
        rang=algo1(ch)
        if(rang==-1):
            mot+=ch
            continue
        rang-=13
        if(rang<0):
            rang=rang+26
        mot+=Alphabet[rang]
    return mot

def SaisieMessage():
    result= input("veuillez saisir votre message :\n")
    return result

def MessageACoder():
    Boolean = True
    print("Bienvenue dans l'algorithme de codage\n")
    while (Boolean):
        instruction = input("Souhaitez-vous :\n1 - coder un message\n2 - decoder un message\nQ - quittez le programme\n")
        if (instruction=='1'):
            print("1 - Coder un message\n--------------------------\n")
            nbrEssai=10
            mot=""
            testMessage= False
            while(nbrEssai>0):
                mot=SaisieMessage()
                for ch in mot:
                    if(algo1(ch)==-1):
                        testMessage=False
                        break
                    else:
                        testMessage=True
                if (testMessage):
                    print("votre message coder : "+Codage(mot)+"\n")
                    break
                else:
                    nbrEssai-=1
                    print(f"Votre message ne doit contenir que des lettres en majuscules\nEssai restant : {nbrEssai}")

            continue
        elif(instruction=='2'):
            print("2 - Decoder un message\n--------------------------\n")
            nbrEssai=10
            mot=""
            testMessage= False
            while(nbrEssai>0):
                mot=SaisieMessage()
                for ch in mot:
                    if(algo1(ch)==-1):
                        testMessage=False
                        break
                    else:
                        testMessage=True
                if (testMessage):
                    print("votre message decoder : "+ Decodage(mot)+"\n")
                    break
                else:
                    nbrEssai-=1
                    print(f"Votre message ne doit contenir que des lettres en majuscules\nEssai restant : {nbrEssai}")

            continue
        elif(instruction=='Q'):
            break
        else:
            print("desolé je ne comprend pas, choississez '1', '2' ou 'Q'\n")



MessageACoder()
