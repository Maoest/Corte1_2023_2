# Calcule los luitros en un recipiente esferico
r=int(input('ingrese el radio en mts: '))

v=(4/3)*(3.1416)*(r**3)
# pasar de mts a litros
v=v*1000

print('Los litros que puede almacenar el recipiente esferico de radio',r,'metro/s es:',round(v,2),'Litros')