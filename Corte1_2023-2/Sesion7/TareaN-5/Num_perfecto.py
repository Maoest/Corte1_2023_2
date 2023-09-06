def obtener_divisores(numero):
    divisores = []
    for i in range(1, numero):
        if numero % i == 0:
            divisores.append(i)
    return divisores

def numero_perfecto(numero):
    divisores = obtener_divisores(numero)
    suma = sum(divisores)
    return suma == numero

def main():
    s = int(input("Ingrese la cantidad de números perfectos que desea encontrar (máximo 10): "))
    cantidad = 0
    numero = 1

    while cantidad < s:
        if numero_perfecto(numero):
            print(f"Número perfecto encontrado: {numero}")
            cantidad += 1
        numero += 1

    print("Proceso completado.")

if __name__ == "__main__":
    main()