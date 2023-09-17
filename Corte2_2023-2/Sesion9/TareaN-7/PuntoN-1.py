from random import randint as r
def crear_matriz():
    matriz = []
    for i in range(5):
        matriz.append([])
        for j in range(10):
            num = r(1, 100)
            matriz[i].append(num)
    return matriz

def imprimir(matriz):
    for fila in matriz:
        print(fila)

def encontrar_alto_bajo(matriz):
    alto = matriz[0][0]
    bajo = matriz[0][0]
    fila_a = 0
    columna_a = 0
    fila_b = 0
    columna_b = 0

    for fila in range(len(matriz)):
        for columna in range(len(matriz[0])):
            if matriz[fila][columna] > alto:
                alto = matriz[fila][columna]
                fila_a = fila
                columna_a = columna
            if matriz[fila][columna] < bajo:
                bajo = matriz[fila][columna]
                fila_b = fila
                columna_b = columna

    print(f'El número más alto es {alto} y esta en la posición [{fila_a}][{columna_a}]')
    print(f'El número más bajo es {bajo} y esta  en la posición [{fila_b}][{columna_b}]')

def ordenar_matriz(matriz):
    matriz_b = [num for fila in matriz for num in fila]
    matriz_b.sort(reverse=True)
    matriz_ordenada = [[matriz_b.pop(0) for _ in range(10)] for _ in range(5)]
    return matriz_ordenada

def main():
    matriz = crear_matriz()
    imprimir(matriz)
    encontrar_alto_bajo(matriz)
    matriz_ordenada = ordenar_matriz(matriz)
    print("\nMatriz ordenada de mayor a menor:")
    imprimir(matriz_ordenada)

if __name__ == "__main__":
    main()
