class Persona:
    def __init__(self):
        self.nombre = None
        self.apellido = None
        self.altura = None
        self.peso = None

    def imc(self):
        return float(self.peso) / (float(self.altura) ** 2)

def main():
    personas = []
    opc = 'n'
    while True:
        per = Persona()
        per.nombre = input('Nombre: ')
        per.apellido = input('Apellido: ')
        per.altura = float(input('Altura (en metros): '))
        per.peso = float(input('Peso (en kilogramos): '))
        personas.append(per)
        opc = input('Desea salir? (y/n): ')
        if opc == 'y':
            break
        else:
            print('Invalido')

    for i in personas:
        print(f'Nombre: {i.nombre} {i.apellido}\n\
              Altura: {i.altura}, Peso: {i.peso}\n IMC: {i.imc()}')

if __name__ == "__main__":
    main()