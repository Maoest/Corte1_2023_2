b='110101'
c=len(b)
a=[]
f=[]
for i in range(c):
    if b[i]!='0':
        d=(b[i]*2**(c-1))
        a.append(len(d))
    c-=1
print(sum(a))