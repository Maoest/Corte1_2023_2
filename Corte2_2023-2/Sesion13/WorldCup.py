import csv

def lectura():
    with open('c:/Users/203/Documents/Repositorio_2023_2/Corte2/Sesion13/wcm.csv', 'r',encoding="utf8") as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)
    return data

def campeon_mundial(data):
    campeones={}
    for partidos in data:
        if partidos[12]=='Final':
            if (partidos[2]>partidos[4])or(partidos[3]>partidos[5]):
                if partidos[0] not in campeones:
                    campeones[partidos[0]]=[partidos[16]]    
                else:
                    list_year=campeones[partidos[0]]
                    list_year.append(partidos[16])
                    campeones[partidos[0]]=list_year
            else:
                if partidos[1] not in campeones:
                    campeones[partidos[1]]=[partidos[16]]
                    
                else:
                    list_year=campeones[partidos[1]]
                    list_year.append(partidos[16])
                    campeones[partidos[1]]=list_year
    print('\n------------------------LISTADO DE CAMPEONES MUNDIALES-----------------------\n')
    campeones=dict(sorted(campeones.items()))
    for pais, year in campeones.items():
        print(f'{pais}: campeon en {year}')

    pais=input('ingrese un pais: ')
    if pais in campeones:
        year=campeones[pais]
        print(f'{pais} Fue campeon en los años {year}.')
    else:
        print(f'El pais {pais} no ah nsido campeon del mundo.')
    
                    
def subcampeones(data):
    subcampeones={}
    for partidos in data:
        if partidos[12]=='Final':
            if (partidos[2]>partidos[4])or(partidos[3]>partidos[5]):
                if partidos[1] not in subcampeones:
                    subcampeones[partidos[1]]=[partidos[16]]    
                else:
                    list_year=subcampeones[partidos[1]]
                    list_year.append(partidos[16])
                    subcampeones[partidos[1]]=list_year
            else:
                if partidos[0] not in subcampeones:
                    subcampeones[partidos[0]]=[partidos[16]]
                    
                else:
                    list_year=subcampeones[partidos[0]]
                    list_year.append(partidos[16])
                    subcampeones[partidos[0]]=list_year

def main():
    print('Seleccione una de las siguientes opciones: \n'\
      '1, Cantidad de mundiales ganados por un pais. \n'\
        '2, Cantidad de subcampeon en mundiales por un pais ')

    data= lectura()
    
    menu={'1': campeon_mundial,
          '2': subcampeones}
    opcion=input('Ingrese una opcion: ')
    if opcion in menu:
        menu[opcion](data)
    else:
        print('opcion invalida')

if __name__ == '__main__':
    main()