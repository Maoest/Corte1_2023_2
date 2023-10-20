def crear_inventario(lista):
    inventario={}
    for elementos in lista:
        if elementos not in inventario:
            inventario[elementos]=1
        else:
            inventario[elementos]+=1
    return inventario

def agregar_elemtos(inv,lista):
    nuevos=crear_inventario(lista)
    for elementos in lista:
        if elementos not in inv:
            inv[elementos]=nuevos[elementos]
        else:
            inv[elementos]+=nuevos[elementos]
    return inv

def reducir_inventarios(inv,lista):
    nuevos=crear_inventario(lista)
    for elementos in lista:
        if elementos not in inv:
            inv[elementos]=nuevos[elementos]
        else:
            if (inv[elementos]-nuevos[elementos])<0:
                inv[elementos]=0
            else:
                inv[elementos]-=nuevos[elementos]
    return inv

def borrado_inventario(inv,item):
    if item in inv:
        del inv[item]  # o tambien inv.pop(item)
    else:
        print('el  item no esta en el inventario')
    return inv


def main():
    crear_inventario(['carbon','madera','madera','diamante','diamante','diamante'])
    agregar_elemtos({'madera':1},['madera','hierro','carbon','madera'])
    reducir_inventarios({'carbon':2,'hierro':3,'diamante':0},['diamante','carbon','hierro','hierro'])
    borrado_inventario({'carbon':2,'madera':1,'diamante':2},'carbon')
if __name__=="__main__":
    main()