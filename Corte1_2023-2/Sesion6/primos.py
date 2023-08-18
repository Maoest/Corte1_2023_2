n=int(input('ingrese un numero: '))
print('Los numeros primos de',n,'son:')
for i in range(1,n+1):
    if n%i==0:
        print(i)