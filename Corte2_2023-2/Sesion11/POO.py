class Estudiante:
    def __init__(self):
        self.nombre= None
        self.apellido= None
        self.edad= None
        self.nacionalidad = 'colombia'
        
        self.estudiar = None

    def entender(self):                 # Metodo
        return 'Si, Aprendi mucho hoy :)'

def main():
    est1 = Estudiante()                 # como crear objetos
    est1.nombre = 'Juan'
    est1.apellido = 'Picon'
    est1.edad = 17

    est2 = Estudiante()
    est2.nombre = 'Roger'
    est2.apellido = 'Piñeros'
    est2.edad = 17

    print(f'el estudainte {est1.nombre} {est1.apellido} de edad de {est1.edad} años y nacionalidad {est1.nacionalidad}')
    input('entendio?')
    print(est2.entender())

if __name__=="__main__":
    main()