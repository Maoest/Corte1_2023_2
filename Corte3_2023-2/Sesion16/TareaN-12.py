class Articulos:
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio

    def setNombre(self, nombre: str):
        self.nombre = nombre
    def getNombre(self):
        return self.nombre

    def setPrecio(self, precio: float):
        self.precio = precio
    def getPrecio(self):
        return self.precio

    def iva(self):
        return 0

    def precioBruto(self):
        return self.precio - self.iva()

class SinIva(Articulos):
    def __init__(self, nombre: str, precio: float):
        super().__init__(nombre, precio)

    def iva(self):
        return 0

class Iva5(Articulos):
    def __init__(self, nombre: str, precio: float):
        super().__init__(nombre, precio)

    def iva(self):
        return self.precio * 0.05

class Iva19(Articulos):
    def __init__(self, nombre: str, precio: float):
        super().__init__(nombre, precio)

    def iva(self):
        return self.precio * 0.19

def main():
    manzanas = SinIva('Manzanas', 1000)
    leche = Iva5('Leche', 1500)
    carne = Iva19('Carne', 5000)
    productos = [manzanas, leche, carne]

    for producto in productos:
        precio_bruto = producto.precioBruto()
        iva = producto.iva()
        precio_completo = producto.precio
        print(f'Producto: {producto.getNombre()}, Precio Bruto: {precio_bruto}, IVA: {iva}, Precio Completo: {precio_completo}')

if __name__ == "__main__":
    main()