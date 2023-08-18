n=int(input('ingrese el numero de primos solicitada: '))
con=1;x=2
numero= print('1')

while con<=n:
    for i in range(2,x):
        primo=x%i
        if primo==0 and x==i:
            print(x)
            con+=1
    x+=1