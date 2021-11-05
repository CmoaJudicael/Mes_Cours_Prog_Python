ALPHABET=" ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def DecodeLettre(a):
    h=(23*a)%78
    ck=[45,22,13,4,2]
    list=[]
    for i in range(0,len(ck)):
        if((h-ck[i])>= 0):
            list.append(1)
            h-=ck[i]
        else:
            list.append(0)
    result=list[0]*2**4+list[1]*2**3+list[2]*2**2+list[3]*2**1+list[4]
    return  ALPHABET[result]
def DecodeMot(liste):
    result=[]
    for i in range(0,len(liste)):
        result.append(DecodeLettre(liste[i]))
    return result


print("Decoder numero 96 :"+str(DecodeLettre(96)))
print("Decoder liste 131,133,34 : "+str(DecodeMot([131,133,34])))


