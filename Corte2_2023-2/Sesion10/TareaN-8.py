def buscar_alimento(data, nombre):
    for fila in data:
        elementos = fila.strip().split(",")
        if len(elementos) >= 2 and elementos[1].lower() == nombre.lower():
            return elementos
    return None

def calcular_valor_neto(valor_ne, iva):
    if iva > 0:
        valor_sin_iva = valor_ne / (1 + iva)
        valor_iva = valor_sin_iva * iva
        valor_total = valor_ne
        return valor_sin_iva, valor_iva, valor_total
    else:
        return valor_ne

def main():
    with open("C:/Users/Haydin/Documents/Alimentos.txt", "r") as archivo:
        reader = archivo.readlines()
        data = list(reader)

    while True:
        var = input('Ingrese el nombre del alimento, si desea salir escriba "salir": ')
        if var.lower() == 'salir':
            break

        elementos = buscar_alimento(data, var)

        if elementos:
            nombre = elementos[1]
            valor_ne = float(input('Ingrese el valor neto del producto: '))
            iva = float(elementos[2])

            if iva > 0:
                print(f'El IVA es de: {iva*100:.0f}%')
                valor_sin_iva, valor_iva, valor_total = calcular_valor_neto(valor_ne, iva)
                print(f'El valor sin IVA es: {round(valor_sin_iva, 2)}')
                print(f'El valor del IVA es: {round(valor_iva, 2)}')
                print(f'El valor neto del producto es: {round(valor_total, 2)}')
            else:
                print(f'El producto no tiene IVA, el Valor a pagar es {valor_ne}')
        else:
            print('El alimento no se encuentra en la base de datos.')

if __name__ == "__main__":
    main()