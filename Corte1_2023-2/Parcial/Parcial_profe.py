from random import uniform as u

def rates():
    comision=[]
    for i in range(5):
        comision.append(round(u(0.1,0.5),2))      
    return comision

def ver_tasas(r,d,c):
    for i in range(5):
        print(f'Divisa: {d[i]}, Tasa: {c[i]}, comision: {r[i]}')

def conversion(r,d,c):
    divisa=input('a que divisa desea hacer el cambio: ').upper()
    if divisa in d:
        idx=d.index(divisa)
        divisa=d[idx]
        tasa=int(c[idx])
        comision=r[idx]
        precio_venta=tasa+(tasa*comision)
        cambio=int(input('que valor desea cambiar: '))
        total= cambio//precio_venta
        vueltas=round(cambio-(precio_venta*total),2)
        print(f'Cambio: {total} {divisa}, Devolucion: {vueltas} cop')
        return 1
    print('Ingrese una opcion valida \n')

def menu():
    comision=rates()
    divisas=['USB','EUR','CNY','JPY','PEN']
    cambios=['4108','4454','563 ','28  ','1106']   
    print(' 1. Cambio de divisas\n','2. Ver tasas de cambio,\n','3. Salir')
    opc=input('Seleciones la opcion deseada: ')

    while opc!='Salir':
        if opc=='1':
            conversion(comision,divisas,cambios)
        elif opc=='2':
            ver_tasas(comision,divisas,cambios)
        elif opc=='salir' or '3':
            break
        else:
            print('Selecion invalida')
        print(' 1. Cambio de divisas\n','2. Ver tasas de cambio,\n','3. Salir')
        opc=input('Seleciones la opcion deseada: ')

def main():
    menu()

if __name__=="__main__":
    main()