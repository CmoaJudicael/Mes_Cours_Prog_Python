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
    Boolean = False
    Nombre = ""
    while (not Boolean):
        result= input("veuillez saisir votre message :\n")
        for ch in result:
            if(ch==ch.capitalize()):
                Boolean=True
            else:
                Boolean=False
                break
    print(""+result)
    return result

motcoder=Codage(SaisieMessage())
print("votre message coder : "+ motcoder)


print("votre message decoder : "+ Decodage(motcoder))
