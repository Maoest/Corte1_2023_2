print('1.calcular el area de un circulo')
print('2.calcular el area de un rectangulo')
print('3.calcular el area de un triangulo')
a=int(input('ingrese un numero '))
if a==1:
    r=float(input('ingrese el radio'))
    a_c=3.14*r**2
    print('el area del circulo es de',a_c)
elif a==2:
    l=float(input('ingrese valor de un lado'))
    a_cu=l*l
    print('el area del cuadrado es de',a_cu)
elif a==3:
    b=float(input('ingrese la base del triangulo'))
    h=float(input('ingrese la altura del triangulo'))
    a_t=(b*h)/2
    print('el area del triangulo es de',a_t)
else:
    print('seleccione una figura valida')