print('1. Programa que pida al usuario un numero, muestre los divisores positivos de ese numero.')
print('2. Programa que muestre el producto entre dos numeros enteros, realizando sumas sucesivas.')
print('3. Programa que muestre en pantalla la cantidad de digitos solicitados por el usuario en serie Fibobnacci.')
N = int(input('Con numeros elige la opcion que quieres ejecutar: 1/2/3 : '))
if N == 1:
    a = int(input('Ingrese un numero: '))
    n=' '
    if a != 0:
        for i in range(1,a+1):
            c=a%i
            if c==0 :
                n += str(f'{i} ')
            i+=1
        print('Los numeros primmos de ese numero son:',n)

    elif a==0:
        print('Ningun numero es divisible entre cero.')

elif N == 2:
    a = int(input('Ingrese un numero: '))
    b = int(input('Ingrese otro numero: '))
    c=0
    if a != 0 and b != 0:
        for i in range(abs(b)):
            c += a
        if (a > 0 and b > 0) or (a < 0 and b < 0):
            print('El producto entre esos dos numeros es:', c)
        else:
            print('El producto entre esos dos numeros es:', -c)
    else:
        print('El producto de cualquier numero con el 0 es 0')


elif N == 3:
    a = int(input('Ingrese el número de términos que quiere: '))
    b = 0
    c = 1
    n = '0 1 '
    for i in range(2, a):
        t = b + c
        n += str(f'{t} ')
        b = c
        c = t
    print(n)


else:
    print('El numero ingresado no es valido.')