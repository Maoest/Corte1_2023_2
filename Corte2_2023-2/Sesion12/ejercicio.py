a=[1,2,3,4]
b=['uno','dos','tres','cuatro']
x=zip(a,b)         # une las dos listas, tuplas, diciconarios
m=list(x)


for idx, valor in enumerate(m):   # primt dato por dato con el idx
    print(idx)
    print(valor)