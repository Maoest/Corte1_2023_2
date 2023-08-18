n=int(input('ingrese el numero de primos solicitada: '))
con=1;x=2
numero= '1 '

while con <n:
    for i in range(2,x+1):
        primo=x%i
        if primo==0 and x==i:
            numero += str(f'{x} ') # imprmir de lado a lado y no hacoa abajo
            con+=1
        elif primo==0 and x!=i:
            break
    x+=1
print(numero)