class ConversorNumerico:
    def __init__(self, numero: int):
        self.numero = numero

    def setNumero(self,numero):
        self.__numero =numero
    def getNumero(self):
        return self.__numero


class Decimal(ConversorNumerico):
    def __init__(self, numero: int):
        super().__init__(numero)

    def deciBi(self):
        a = self.numero
        b = 2
        d = []
        while a >= b:
            c = a // b
            d.append(a - (c * b))
            a = a // b
        else:
            d.append(c)
        return d

    def decoHexa(self):
        a = int(self.numero)
        b = 16
        d = []
        while a >= b:
            c = a // b
            e = a - (c * b)
            if e == 10:
                d.append('A')
            elif e == 11:
                d.append('B')
            elif e == 12:
                d.append('C')
            elif e == 13:
                d.append('D')
            elif e == 14:
                d.append('E')
            elif e == 15:
                d.append('F')
            else:
                d.append(e)
            a = a // b
        else:
            d.append(c)
        return d

class Binario(ConversorNumerico):
    def __init__(self, numero):
        super().__init__(numero)

    def binDeci(self):
        c = len(str(self.numero))
        a = []
        for i in str(self.numero):
            if i != '0':
                d = int(i) * 2 ** (c - 1)
                a.append(d)
            c -= 1
        return sum(a)

class Hexadecimal(ConversorNumerico):
    def __init__(self, numero):
        super().__init__(numero)

    def hexaDeci(self):
        c = len(str(self.numero))
        a = []
        for i in str(self.numero):
            if i != '0':
                if i == 'A':
                    d = 10 * 16 ** (c - 1)
                    a.append(d)
                elif i == 'B':
                    d = 11 * 16 ** (c - 1)
                    a.append(d)
                elif i == 'C':
                    d = 12 * 16 ** (c - 1)
                    a.append(d)
                elif i == 'D':
                    d = 13 * 16 ** (c - 1)
                    a.append(d)
                elif i == 'E':
                    d = 14 * 16 ** (c - 1)
                    a.append(d)
                elif i == 'F':
                    d = 15 * 16 ** (c - 1)
                    a.append(d)
                else:
                    if i != '0':
                        d = int(i) * 16 ** (c - 1)
                        a.append(d)
            c -= 1
        return sum(a)

def main():
    m = input('Que conversión desea realizar:\n a. Decimal a Binario\n b. Decimal a Hexadecimal\n c. Binario a Decimal\n d. Hexadecimal a Decimal\n')
    n = input('Ingrese un número: ')
    
    if m == 'a':
        decimal_instance = Decimal(n)
        result = decimal_instance.deciBi()
        print("Resultado:", result)
    elif m == 'b':
        decimal_instance = Decimal(n)
        result = decimal_instance.decoHexa()
        print("Resultado:", result)
    elif m == 'c':
        binary_instance = Binario(n)
        result = binary_instance.binDeci()
        print("Resultado:", result)
    elif m == 'd':
        hexadecimal_instance = Hexadecimal(n)
        result = hexadecimal_instance.hexaDeci()
        print("Resultado:", result)
    else:
        print('Opción inválida')

if __name__ == "__main__":
    main()

