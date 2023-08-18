print('1. Programa que pida al usuario una letra del abecedario,verifique si el caracter es vocal o consonante.')
print('2. Programa que calcule el cobro de un estacionamiento.')
print('3. Programa que solicite tres longitudes y determine si se puede hacer o no un triangulo.')
N=int(input('Con numeros elige la opcion que quieres ejecutar: 1/2/3 '))
if N==1:
    I=[]
    n=int(input('ingrese un número entero positivo que desee: '))
    if n>0:
        i=1
        while i<=n:
            r=i%2
            if r==1:
                I.append(i)
            i+=1
        print('Los numeros inpares hasta ',n,' son: ',I)
    else:
        print('el numero ingresado es invalido')

elif N==2:
    n = int(input('ingrese un numero: '))
    fa=1
    while n>1:
        fa*=n
        n-=1
    print(fa)
elif N==3:
    n=int(input('ingrese un numero:'))
    D=2
    while D<n:
        if n%D==0:
            print('El numero no es primo')
            break
        else:
            print('El es un numero primo')
            break
    print('los numero primos hasta ',n,'son: ')
    if n>0:
        for i in range(1,n):
            B=2
            sp=True
            while (sp) and B<i:
                if i%B==0:
                    sp=False
                else:
                    B+=1
            if sp:
                print(i)

else:
  print('El numero ingresado no es valido.')