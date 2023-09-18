from random import randint as r
def crear_lista(x):
    lista = []
    for i in range(x):
        num = r(1, 100)
        lista.append(num)
    return lista

def buscar_mayor_menor(lista, i, mayor, menor):
    if i == len(lista):
        return mayor, menor
    if lista[i] > mayor:
        mayor = lista[i]
    if lista[i] < menor:
        menor = lista[i]
    return buscar_mayor_menor(lista, i + 1, mayor, menor)

def main():
    x=int(input('ingrese la longitud de la lista deseada: '))
    lista = crear_lista(x)
    i = 0
    inicio = lista[0]
    mayor, menor = buscar_mayor_menor(lista, i, inicio, inicio)
    print(lista)
    print('numero mayor:',mayor)
    print('numero menor:', menor)

if __name__ == "__main__":
    main()