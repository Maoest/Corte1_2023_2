class Persona:
    def __init__(self):
        self.nombre = None
        self.apellido = None
        self.altura = None
        self.peso = None

    def imc(self):
        a = round(float(self.peso) / (float(self.altura) ** 2), 1)
        if a <= 18.5:
            categoria = 'Bajo'
        elif a <= 24.9:
            categoria = 'Saludable'
        elif a <= 29.9:
            categoria = 'Sobrepeso'
        elif a <= 34.9:
            categoria = 'Obesidad I'
        elif a <= 39.9:
            categoria = 'Obesidad II'
        else:
            categoria = 'Obesidad III'
        
        return f'IMC: {categoria}, {a}'

        

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
        print(f'\nNombre: {i.nombre} {i.apellido}\n'\
              f'Altura: {i.altura}, Peso: {i.peso}\n'\
                 f'IMC: {i.imc()}')

if __name__ == "__main__":
    main()