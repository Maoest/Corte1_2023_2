from random import randint as r

def rates():
    comision=[]
    for i in range(5):
        a=r(10,50)
        comision.append(a/100)       # El numero aleatorio  se divide entre 100 y se guarda en la lista comision.
        i+=1
    return comision

def menu(comision):
    while True:                       # bucle infinito para poder ver las tasas de cambio y poder hacer despues la conversion.
        print('1. Conversion de COP a cualquier divisa.')
        print('2. Ver tasas de cambio y la correspondiente comision')
        print('3. Si desea terminar .')
        N=int(input('Con numeros elige la opcion que quieres ejecutar: 1/2/3 : '))
        if N==1:
            print('USD,EUR,CNY,JPY,PEN')
            a=input('A que divisa desea convertir (mayuscula): ')
            b=int(input('Cuantos COP desea cambiar: '))
            if a=='USD':
                c=4108+(4108*comision[0]) # la suma de la tasa de cambio mas el valor de la comision.
                E=b//c                    # la division entre el valor a cambiar y la suma de la comision y la tasa de cambio.
                d=b-(c*E)                 
                print(f'cambio: {E} USD, Devolucion: {round(d,2)} COP')
            elif a=='EUR':
                c=4454+(4454*comision[1])
                E=b//c
                d=b-(c*E)
                print(f'cambio: {E} USD, Devolucion: {round(d,2)} COP')
            elif a=='CNY':
                c=563+(563*comision[2])
                E=b//c
                d=b-(c*E)
                print(f'cambio: {E} USD, Devolucion: {round(d,2)} COP')
            elif a=='JPY':
                c=28+(28*comision[3])
                E=b//c
                d=b-(c*E)
                print(f'cambio: {E} USD, Devolucion: {round(d,2)} COP')
            elif a=='PEN':
                c=1106+(1106*comision[4])
                E=b//c
                d=b-(c*E)
                print(f'cambio: {E} USD, Devolucion: {round(d,2)} COP')
            else:
                print('Divisa no reconocida')
        
        elif N==2:
            print(f'Divisa: USD, Tasa:4108, comision: {comision[0]}.\nDivisa: USD, Tasa:4108, comision: {comision[1]}. \nDivisa: USD, Tasa:4108, comision: {comision[2]}.\nDivisa: USD, Tasa:4108, comision: {comision[3]}.\nDivisa: USD, Tasa:4108, comision: {comision[4]}.\n')

        elif N==3:
            print('saliendo')
            break                                       # Termina el while terminando el bucle infinito.
            
        else:
            print('Seleccion invalida')
    

def main():
    comision=rates()
    menu(comision)
    

if __name__=="__main__":
    main()