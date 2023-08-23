import Fcn_Tupla
def main():
    a=''
    pal=''
    print('para salir escriba "exit"')
    while a!= 'exit':
        pal +=(f' {a}')
        a=input('ingrese un dato: ')
    Fcn_Tupla.app(pal,i=1)


if __name__=="__main__":
    main()
