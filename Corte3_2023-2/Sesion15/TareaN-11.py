class Ciudadano:
    def __init__(self, nombre: str, cedula: int, edad: int ):
        self.__nombre = nombre
        self.__cedula = cedula
        self.__edad = edad

    def set_nombre(self, nombre: str):
        self.__nombre = nombre
    def get_nombre(self):
        return self.__nombre

    def set_cedula(self, cedula: int):
        self.__cedula = cedula
    def get_cedula(self):
        while len(str(self.__cedula)) != 8:
            self.__cedula = int(input('La cédula debe tener 8 dígitos: '))
        return self.__cedula

    def set_edad(self, edad: int):
        self.__edad = edad
    def get_edad(self):
        return self.__edad

    def mostrar(self):
        return f'Nombre:{self.get_nombre()}-Edad:{self.get_edad()}-CC:{self.get_cedula()}'

    def esMayorDeEdad(self):
        if self.__edad >= 18:
            return f'Usted es mayor de edad'
        else:
            return f'usted es menor de edad'

    def infoDeLaPersona(self):
        return f'{self.get_nombre()} de {self.get_edad()} años, su cedula es {self.get_cedula()}'


class Profesor(Ciudadano):
    def __init__(self, nombre: str, cedula: int, edad: int, materia: str, titulo: str):
        super().__init__(nombre, cedula, edad)
        self.materia = materia
        self.titulo = titulo

    def setMateria(self, materia: str):
        self.materia = materia
    def getMateria(self):
        return self.materia

    def setTitulo(self, titulo: str):
        self.titulo = titulo
    def getTitulo(self):
        return self.titulo

    def darTarea(self):
        return f'el profespor {self.get_nombre()} dejo 3 tareas y un proyecto en la materia de {self.getMateria()}.'

    def infoDeLaPersona(self):
        return f'El profesor {self.get_nombre()} de {self.get_edad()} años, tiene el titulo de {self.getTitulo()} da clases de {self.getMateria()}'

class Entrenador(Ciudadano):
    def __init__(self, nombre: str, cedula: int, edad: int , deporte: str, equipo: str):
        super().__init__(nombre, cedula, edad)
        self.deporte = deporte
        self.equipo = equipo

    def setDeporte(self, deporte: str):
        self.deporte = deporte
    def getDeporte(self):
        return self.deporte

    def setEquipo(self, equipo: str):
        self.equipo= equipo
    def getEquipo(self):
        return self.equipo

    def ganarPartido(self):
        return f'el entrenador {self.get_nombre()} ganó otro partido.'

    def infoDeLaPersona(self):
        return f'El entrenador {self.get_nombre()} de {self.get_edad()}, es entrenador de {self.getDeporte()} del equipo de {self.getEquipo()}'

class Actor(Ciudadano):
    def __init__(self, nombre: str, cedula: int, edad: int, categoria: str, peliculas : int):
        super().__init__(nombre, cedula, edad)
        self.categoria = categoria
        self.peliculas = peliculas

    def setCategoria(self, categoria: str):
        self.categoria = categoria
    def getCategoria(self):
        return self.categoria

    def setPeliculas(self, peliculas: str):
        self.sexo = peliculas
    def getPeliculas(self):
        return self.peliculas

    def actuar(self):
        return f'"ser o no ser, esa es la cuestion"'

    def infoDeLaPersona(self):
        return f'El/La actor/actriz {self.get_nombre()} de {self.get_edad()}, es actor de {self.getCategoria()} que ah hecho {self.getPeliculas()} peliculas'

def main():
    ciudadano = Ciudadano('Nicolás', 12345678, 28)
    actor = Actor('Gomez', 12345678, 35, 'Drama', 23)
    profesor = Profesor('Elmer', 12345678, 43, 'Estatica', 'Ingeniero')
    entrenador = Entrenador('Jose', 12345678, 38, 'Bloncesto', 'los Raptors')
    print(ciudadano.mostrar())
    print(ciudadano.infoDeLaPersona())
    print(actor.infoDeLaPersona())
    print(profesor.infoDeLaPersona())
    print(entrenador.infoDeLaPersona())
if __name__ == "__main__":
    main()