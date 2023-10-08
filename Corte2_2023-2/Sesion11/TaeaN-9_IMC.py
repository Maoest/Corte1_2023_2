class Persona:
    def __init__(self):
        self._nombre = None
        self._apellido = None
        self._altura = None
        self._peso = None

    def nombre(self):
        return self._nombre
    def nombre(self, value):
        self._nombre = value

    def apellido(self):
        return self._apellido
    def apellido(self, value):
        self._apellido = value

    def altura(self):
        return self._altura
    def altura(self, value):
        self._altura = value

    def peso(self):
        return self._peso
    def peso(self, value):
        self._peso = value

    def imc(self):
        if self._altura is not None and self._peso is not None:
            a = round((self._peso / (self._altura / 100) ** 2), 1)
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
        else:
            return 'IMC no calculable'

def main():
    personas = []
    opc = 'n'
    while True:
        per = Persona()
        per.nombre = input('Nombre: ')
        per.apellido = input('Apellido: ')
        per.altura = float(input('Altura (en cm): '))
        per.peso = float(input('Peso (en kilogramos): '))
        personas.append(per)
        opc = input('Desea salir? (y/n): ')
        if opc == 'y':
            break
        else:
            print('Invalido')

    for i in personas:
        print(f'\nNombre: {i.nombre} {i.apellido}\n' \
              f'Altura: {i.altura}, Peso: {i.peso}\n' \
              f'IMC: {i.imc()}')

if __name__ == "__main__":
    main()
