def CodeBase2(a):
    for i in range (0,2):
        for j in range (0,2):
            for k in range (0,2):
                for l in range (0,2):
                    for m in range (0,2):
                        ck=i*2**4+j*2**3+k*2**2+l*2**1+m
                        if(a==ck):
                            l = [i, j, k, l, m]
                            return l

def CodeLettre(lettre):
    clef=[63,62,65,68,34]
    ALPHABET=" ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(0,(len(ALPHABET)-1)):
        if(lettre.capitalize() ==ALPHABET[i]):
            code=CodeBase2(i)
            result=clef[0]*code[0]+clef[1]*code[1]+clef[2]*code[2]+clef[3]*code[3]+clef[4]*code[4]
            return result
def CodeMot(mot):
    list=[]
    for ch in mot:
        list.append(CodeLettre(ch))
    return list

L=CodeBase2(9)
print(str(L))
print("codage lettre I :"+ str(CodeLettre("I")))
print("codage Mot :" + str(CodeMot("BTS")))
