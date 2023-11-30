#decorator

def dec(a,b):
    print(a/b)


#creating the decorator
def newdec(dec): #dec fn accteps aonther fn as parameter
    def inner(a,b):
        if a<b:
            a,b=b,a,b
        return dec(a,b)
    return inner
dec=newdec(dec)
dec(3,1 )