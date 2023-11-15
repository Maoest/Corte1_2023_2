class Producto:
    def __init__(self, nombre: str, precio: float, cantidad_disp: int=0 ):
        self.nombre = nombre
        self.precio = precio
        self.cantidad_d
        isp = cantidad_disp

    def setNombre(self, nombre: str):
        self.nombre = nombre
    def getNombre(self):
        return self.nombre

    def setPrecio(self, precio: float):
        self.precio = precio
    def getPrecio(self):
        return self.precio

    def setCantidad_disp(self, cantidad_disp: int):
        self.cantidad_disp = cantidad_disp
    def getCantidad_disp(self):
        return self.cantidad_disp

    def obtener_info(self):
        return f'Producto: {self.getNombre()}, Precio: ${self.getPrecio()}, Disponibles: {self.getCantidad_disp()} unidades'

    def restar_cantidad(self):
        if self.getCantidad_disp() > 0:
            self.setCantidad_disp(self.getCantidad_disp() - 1)
            return True
        else:
            return False

    def verificar_disponibilidad(self):
        return f'Hay {self.getCantidad_disp()} unidades disponibles de {self.getNombre()}'

class Snack(Producto):
    def __init__(self, nombre: str, precio: float, tipo: str, cantidad_disp: int = 0):
        super().__init__(nombre, precio, cantidad_disp)
        self.tipo = tipo

    def setTipo(self, tipo: str):
        self.tipo = tipo

    def getTipo(self):
        return self.tipo

    def obtener_info(self):
        return f'Snack: {self.getNombre()}, Precio: ${self.getPrecio()}, Disponibles: {self.getCantidad_disp()} unidades, Tipo: {self.getTipo()}'

class Bebida(Producto):
    def __init__(self, nombre: str, precio: float, tamaño: str, cantidad_disp: int = 0):
        super().__init__(nombre, precio, cantidad_disp)
        self.tamaño = tamaño

    def setTamaño(self, tamaño: str):
        self.tamaño = tamaño

    def getTamaño(self):
        return self.tamaño

    def obtener_info(self):
        return f'Bebida: {self.getNombre()}, Precio: ${self.getPrecio()}, Disponibles: {self.getCantidad_disp()} unidades, Tamaño: {self.getTamaño()}'

class MaquinaDispensadora:
    def __init__(self, productos: list, total_ventas: float, cantidad_disp: int = 0):
        self._productos = productos
        self._total_ventas = total_ventas

    def setProductos(self, productos):
        self._productos = productos
    def getProductos(self):
        return self._productos

    def setTotal_ventas(self, total_ventas):
        self._total_ventas = total_ventas
    def getTotal_ventas(self):
        return self._total_ventas

    def agregar_producto(self, producto):
        self._productos.append(producto)

    def realizar_venta(self, nombre_producto):
        for producto in self._productos:
            if producto.getNombre() == nombre_producto and producto.getCantidad_disp() > 0:
                producto.setCantidad_disp(producto.getCantidad_disp() - 1)
                self._total_ventas += producto.getPrecio()
                print(f'Venta realizada: {producto.obtener_info()}')
                return True
        print(f'Error: Producto "{nombre_producto}" no disponible.')
        return False

    def total_ventas(self):
        return f'Total de ventas: ${self._total_ventas}'

def main():
    papas = Snack('Papas de Limón', 2500, 'paquete', 10)
    print(papas.obtener_info())
    print(papas.verificar_disponibilidad())

    soda = Bebida('Pepsi', 1500, 'grande', 20)
    print(soda.obtener_info())
    print(soda.verificar_disponibilidad())

    maquina = MaquinaDispensadora([], 0)
    maquina.agregar_producto(papas)
    maquina.agregar_producto(soda)

    maquina.realizar_venta('Papas de Limón')
    maquina.realizar_venta('Pepsi')

    print(maquina.total_ventas())

if __name__ == "__main__":
    main()