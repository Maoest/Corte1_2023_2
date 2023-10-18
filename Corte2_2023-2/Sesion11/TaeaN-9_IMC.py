class Persona:
    def __init__(self):
        self._nombre = None
        self._apellido = None
        self._altura = None
        self._peso = None

    def set_nombre(self, value):
        self._nombre = value

    def get_nombre(self):
        return self._nombre

    def set_apellido(self, value):
        self._apellido = value

    def get_apellido(self):
        return self._apellido

    def set_altura(self, value):
        if 0 < value <= 300:
            self._altura = value
        else:
            print("Altura no válida. Debe estar entre 0 y 300 cm.")

    def get_altura(self):
        return self._altura

    def set_peso(self, value):
        if 0 < value <= 500:
            self._peso = value
        else:
            print("Peso no válido. Debe estar entre 0 y 500 kg.")

    def get_peso(self):
        return self._peso

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
        per.set_nombre(input('Nombre: '))
        per.set_apellido(input('Apellido: '))
        per.set_altura(float(input('Altura (en cm): ')))
        per.set_peso(float(input('Peso (en kilogramos): ')))
        personas.append(per)
        opc = input('Desea salir? (y/n): ')
        if opc == 'y':
            break
        else:
            print('Invalido')

    for i in personas:
        print(f'\nNombre: {i.get_nombre()} {i.get_apellido()}\n'
              f'Altura: {i.get_altura()}, Peso: {i.get_peso()}\n'
              f'IMC: {i.imc()}')

if __name__ == "__main__":
    main()