def encontrar(a, b, i, r=None):
    if r is None:
        r = []
    i = a.find(b, i)
    if i != -1:
        r.append(i)
        encontrar(a, b, i + 1, r)
    return r

def main():
    a = str(input('ingrese un dato: '))
    b = str(input('ingrese el dato a encontar: '))
    i=0
    posicion = encontrar(a, b, i)
    print("Posiciones:", posicion)

if __name__ == "__main__":
    main()