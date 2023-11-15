b='C92A'
c=len(b)
a=[]
f=[]
for i in range(c):
    if b[i]!='0':
        if b[i]=='A':
            d=(10*16**(c-1))
            a.append(d)
        elif b[i]=='B':
            d=(11*16**(c-1))
            a.append(d)
        elif b[i]=='C':
            d=(12*16**(c-1))
            a.append(d)
        elif b[i]=='D':
            d=(13*16**(c-1))
            a.append(d)
        elif b[i]=='E':
            d=(14*16**(c-1))
            a.append(d)
        elif b[i]=='F':
            d=(15*16**(c-1))
            a.append(d)
        else:
            if b[i]!='0':
                d=int(b[i])*16**(c-1)
                a.append(d)
    c-=1
print(sum(a))