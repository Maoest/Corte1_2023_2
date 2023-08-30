def obtener_divisores(numero):
    divisores = []
    for i in range(1, numero):
        if numero % i == 0:
            divisores.append(i)
    return divisores

def es_numero_perfecto(numero):
    divisores = obtener_divisores(numero)
    suma_divisores = sum(divisores)
    return suma_divisores == numero

def main():
    cantidad_solicitada = int(input("Ingrese la cantidad de números perfectos que desea encontrar (máximo 10): "))
    cantidad_encontrada = 0
    numero_actual = 1

    while cantidad_encontrada < cantidad_solicitada:
        if es_numero_perfecto(numero_actual):
            print(f"Número perfecto encontrado: {numero_actual}")
            cantidad_encontrada += 1
        numero_actual += 1

    print("Proceso completado.")

if __name__ == "__main__":
    main()