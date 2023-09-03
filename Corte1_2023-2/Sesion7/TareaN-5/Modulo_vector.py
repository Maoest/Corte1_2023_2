   
def Modulo():
    a = int(input('Ingrese la cordenada x del origen del vector: '))
    b = int(input('Ingrese la cordenada y del origen del vector: '))
    c = int(input('Ingrese la cordenada x del fin del vector: '))
    d = int(input('Ingrese la cordenada y del fin del vector: '))
    x=c-a
    y=d-b
    m=(x**2 + y**2)**0.5
    print('El modulo del vector es: ',m)
    print(f'Las componentes en x y y son:{x,y}')

def main():
    Modulo()

if __name__ == "__main__":
    main()