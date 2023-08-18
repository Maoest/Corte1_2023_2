print('1. Programa que pida al usuario una letra del abecedario,verifique si el caracter es vocal o consonante.')
print('2. Programa que calcule el cobro de un estacionamiento.')
print('3. Programa que solicite tres longitudes y determine si se puede hacer o no un triangulo.')
N=int(input('Con numeros elige la opcion que quieres ejecutar: 1/2/3 : '))
if N==1:
    a=input('Ingrese un aletra del abecedario: ')
    if a.upper() == 'A' or a.upper() == 'E' or a.upper() == 'I' or a.upper() == 'O' or a.upper() == 'U' :
        print('La letras es una vocal.')
    else:
        print('La letras es unas consonate.')

elif N==2:
    m = int(input('Ingrese los minutos que estuvo el carro en el estacionamiento: '))
    v_t = m * 139
    v_r = round((v_t - v_t * 0.19) / 50) * 50
    print('El valor a pagar sin IVA es de:', v_r)
    
elif N==3:
    a = int(input('Ingrese la longitud del primer lado: '))
    b = int(input('Ingrese la longitud del segundo lado: '))
    c = int(input('Ingrese la longitud del tercer lado: '))
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            print('El triángulo es Equilátero.')
        elif a == b or a == c or b == c:
            print('El triángulo es Isósceles.')
        else:
            print('El triángulo es Escaleno.')
    else:
        print('No se puede formar un triángulo.')


else:
  print('El numero ingresado no es valido.')