class Deportista:
    def __init__(self,nombre:str,documento:str,edad:int):
        self.__nombre= nombre
        self.__documento= documento
        self.__edad= edad

    def setNombre(self,nombre:str):
        self.__nombre =nombre
    def getNombre(self):
        return self.__nombre

    def setDocumento(self,documento:str):
        self.__documento=documento
    def getDocumento(self):
        return self.__documento
    
    def setEdad(self,edad:int):
        self.__edad=edad
    def getEdad(self):
        return self.__edad
    
    def jugador(self):
        return f'EL jugador {self.getNombre()} Es un gran ajedrecista'
    
class Futbolista(Deportista):
    def __init__(self,nombre:str,documento:str,edad:int,goles:int,nombreEquipo:str):
        super().__init__(nombre,edad,documento)
        self.nombreEquipo= nombreEquipo
        self.goles= goles

    def setGoles(self,goles:int):
        self.goles =goles
    def getGoles(self):
        return self.goles

    def setNombreEquipo(self,nombreEquipo:str):
        self.nombreEquipo=nombreEquipo
    def getNombreEquipo(self):
        return self.nombreEquipo
    
    def patear(self):
        return f'el jugador {self.getNombre()} acaba de anotar un gol'
    
    def jugador(self):
        return f'EL jugador {self.getNombre()} es un gran goleador'
    
class Basquetbolista(Deportista):
    def __init__(self,nombre:str,documento:str,edad:int,cestas:int,nombreEquipo:str):
        super().__init__(nombre,edad,documento)
        self.cestas = cestas
        self.nombreEquipo = nombreEquipo

    def setCestas(self,cestas:int):
        self.cestas =cestas
    def getGoles(self):
        return self.cestas

    def setNombreEquipo(self,nombreEquipo:str):
        self.nombreEquipo=nombreEquipo
    def getNombreEquipo(self):
        return self.nombreEquipo
    
    def anotar(self):
        return f'El jugador {self.getNombre()} acaba de hacer un triple'

    def jugador(self):
        return f'EL jugador {self.getNombre()} es un gran anotador'

class DeportistaTenis(Deportista):
    def __init__(self,nombre:str,documento:str,edad:int,sets_ganados:int,ace:int):
        super().__init__(nombre,edad,documento)
        self.ace= ace
        self.sets_ganados= sets_ganados

    def setAce(self,ace:int):
        self.ace =ace
    def getGoles(self):
        return self.ace

    def setSets_ganados(self,sets_ganados:int):
        self.sets_ganados=sets_ganados
    def getNombreEquipo(self):
        return self.sets_ganados
    
    def Ace(self):
        return f'El jugador {self.getNombre()} acaba de hacer un punto'
    
    def jugador(self):
        return f'El jugador {self.getNombre()} es un gran ajedrecista'
    
def main():
    jugador1=Futbolista('Radamel Falcao Garcia',35,'23334553262','Colombia',34)
    jugador2=DeportistaTenis('Roger Federer',42,'2425235252',6,12)
    jugador3=Deportista('Magnus carlsen',32,'32,2141414')
    jugador4=Basquetbolista('Lebron James',38,'1241441414',11620,'Lakers')


    print(jugador4.anotar())
    print(jugador2.Ace())
    print(jugador1.patear())
    print(jugador3.jugador())


if __name__=="__main__":
    main()