def main(filas,columnas):
    matriz= []
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            num=int(input(f'ingrese el valor de la posicion [{i},{j}]: '))
            matriz[i].append(num)
    return matriz

if __name__=="__main__":
    filas=int(input('Ingrese las filas deseadas: '))
    columnas=int(input('Ingrese las columnas deseadas: '))
    print(main(filas,columnas))