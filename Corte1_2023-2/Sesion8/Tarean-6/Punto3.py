def org_min_may():
    L=[]
    a=0
    while a>=0:
        a=int(input('ingrese un numero: '))
        if a>=0:
            L.append(a)
    return L

def eliminacion_duplicados(L):
    m = max(L)
    i = 0
    while i < m:
        if L.count(i) >= 2:
            L.remove(i)
            m = max(L)
        else:
            i += 1
    print(L)

def main():
    L=org_min_may()
    print(L)
    eliminacion_duplicados(L)

    

if __name__ == "__main__":
    main()
