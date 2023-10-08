import csv

def lectura():
    with open(r'C:\Users\HNNMORAR\PycharmProjects\pythonProject2\wcm.csv', 'r', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)
    return data

def campeon_mundial(data):
    campeones = {}
    for partidos in data:
        if partidos[12] == 'Final':
            if (partidos[2] > partidos[4]) or (partidos[3] > partidos[5]):
                if partidos[0] not in campeones:
                    campeones[partidos[0]] = [partidos[16]]
                else:
                    list_year = campeones[partidos[0]]
                    list_year.append(partidos[16])
                    campeones[partidos[0]] = list_year
            else:
                if partidos[1] not in campeones:
                    campeones[partidos[1]] = [partidos[16]]

                else:
                    list_year = campeones[partidos[1]]
                    list_year.append(partidos[16])
                    campeones[partidos[1]] = list_year
    print('\n------------------------LISTADO DE CAMPEONES MUNDIALES-----------------------\n')
    campeones = dict(sorted(campeones.items()))
    for pais, year in campeones.items():
        print(f'{pais}: campeon en {year}')

    pais = input('ingrese un pais: ')
    if pais in campeones:
        year = campeones[pais]
        print(f'{pais} Fue campeon en los años {year}.')
    else:
        print(f'El pais {pais} no ah sido campeon del mundo.')


def subcampeones(data):
    subcampeones = {}
    for partidos in data:
        if partidos[12] == 'Final':
            if (partidos[2] > partidos[4]) or (partidos[3] > partidos[5]):
                if partidos[1] not in subcampeones:
                    subcampeones[partidos[1]] = [partidos[16]]
                else:
                    list_year = subcampeones[partidos[1]]
                    list_year.append(partidos[16])
                    subcampeones[partidos[1]] = list_year
            else:
                if partidos[0] not in subcampeones:
                    subcampeones[partidos[0]] = [partidos[16]]

                else:
                    list_year = subcampeones[partidos[0]]
                    list_year.append(partidos[16])
                    subcampeones[partidos[0]] = list_year
    print('\n------------------------LISTADO DE SUBCAMPEONES MUNDIALES-----------------------\n')
    subcampeones = dict(sorted(subcampeones.items()))
    for pais, year in subcampeones.items():
        print(f'{pais}: subcampeon en {year}')

    pais = input('ingrese un pais: ')
    if pais in subcampeones:
        year = subcampeones[pais]
        print(f'{pais} Fue subcampeon en los años {year}.')
    else:
        print(f'El pais {pais} no ah sido subcampeon del mundo.')


def copas_mundiales(data):
    copas = []
    for partidos in data:
        if partidos[12] == 'Final':
            copas.append((partidos[16], partidos[15]))
    print('\n------------------------LISTADO DE LAS COPAS DEL MUNDO-----------------------\n')
    copas = sorted(copas, key=lambda x: x[0], reverse=True)
    num=22
    for year, pais in copas:
        print(f'Mundial No{num} ({pais} {year})')
        num -=1


def enfrentamientos(data):
    a = input('Digite el primer equipo: ')
    b = input('Digite el segundo equipo: ')
    enfrentamientos = {a: {'victorias': 0, 'empates': 0, 'derrotas': 0},
                       b: {'victorias': 0, 'empates': 0, 'derrotas': 0}}
    cantidad_partidos = 0

    for partido in data[1:]:
        equipo_local = partido[0]
        equipo_visitante = partido[1]
        goles_local = int(partido[2])
        goles_visitante = int(partido[4])

        if equipo_local == a and equipo_visitante == b:
            if goles_local > goles_visitante:
                enfrentamientos[a]['victorias'] += 1
                enfrentamientos[b]['derrotas'] += 1
            elif goles_local < goles_visitante:
                enfrentamientos[b]['victorias'] += 1
                enfrentamientos[a]['derrotas'] += 1
            else:
                enfrentamientos[a]['empates'] += 1
                enfrentamientos[b]['empates'] += 1
            cantidad_partidos += 1
        elif equipo_local == b and equipo_visitante == a:
            if goles_local > goles_visitante:
                enfrentamientos[b]['victorias'] += 1
                enfrentamientos[a]['derrotas'] += 1
            elif goles_local < goles_visitante:
                enfrentamientos[a]['victorias'] += 1
                enfrentamientos[b]['derrotas'] += 1
            else:
                enfrentamientos[a]['empates'] += 1
                enfrentamientos[b]['empates'] += 1
            cantidad_partidos += 1

    print(f'Cantidad de partidos: {cantidad_partidos}')
    print(f'Historial de enfrentamientos entre {a} y {b}:')
    print(
        f'{a}: Victorias = {enfrentamientos[a]["victorias"]}, Empates = {enfrentamientos[a]["empates"]}, Derrotas = {enfrentamientos[a]["derrotas"]}')
    print(
        f'{b}: Victorias = {enfrentamientos[b]["victorias"]}, Empates = {enfrentamientos[b]["empates"]}, Derrotas = {enfrentamientos[b]["derrotas"]}')

    for partido in data[1:]:
        equipo_local = partido[0]
        equipo_visitante = partido[1]
        goles_local = int(partido[2])
        goles_visitante = int(partido[4])
        pais = partido[15]
        fase = partido[12]
        year = int(partido[16])

        if equipo_local == a and equipo_visitante == b:
            print('\n----------------------------------------------------')
            print(f'                       -({pais}-{year})-                      ')
            print(f'{a} {goles_local} vs {goles_visitante} {b} - Ronda: {fase}')
        elif equipo_local == b and equipo_visitante == a:
            print('\n----------------------------------------------------')
            print(f'                       -({pais}-{year})-                      ')
            print(f'{b} {goles_local} vs {goles_visitante} {a} - Ronda: {fase}')



def mayor_goles_por_mundial(data):
    print('Seleccione una de las siguientes opciones: \n'\
          '1. Ver lista completa de goles por mundial \n'\
          '2. Búsqueda por mundial')
    opcion = input('Ingrese una opción: ')
    goles = {}
    if opcion == '1':
        for partido in data[1:]:
            home_score = int(partido[2])
            away_score = int(partido[4])
            year = int(partido[16])
            if year not in goles:
                goles[year] = home_score + away_score
            else:
                goles[year] += home_score + away_score
        print('\n------------------------LISTADO DE CANTIDAD DE GOLES POR MUNDIAL-----------------------\n')
        goles = sorted(goles.items(), key=lambda x: x[1], reverse=True)
        for year, num in goles:
            print(f'En el Mundial de {year} se hicieron un total de {num} goles')

    if opcion == '2':
        goles_por_fase = {
            'Final': 0,
            'Third-place match':0,
            'Semi-finals': 0,
            'Quarter-finals': 0,
            'Round of 16': 0,
            'Group stage': 0
        }
        print('\n------------------------CANTIDAD DE GOLES POR MUNDIAL-----------------------')
        year_busqueda = int(input('Escriba el año del mundial que desea consultar: '))
        for partido in data[1:]:
            home_score = int(partido[2])
            away_score = int(partido[4])
            year = int(partido[16])
            fase = partido[12]
            if year == year_busqueda:
                if fase in goles_por_fase:
                    goles_por_fase[fase] += home_score + away_score
        total_goles = sum(goles_por_fase.values())

        print(f'-------------------Mundial: {year_busqueda}_____________________ ')
        for fase, num_goles in goles_por_fase.items():
            print(f'fase {fase}: {num_goles} goles')
        print(f'-------------------Total Goles {total_goles}_____________________\n')


def main():
    print('Seleccione una de las siguientes opciones: \n'\
          '1, Cantidad de mundiales ganados por un pais. \n'\
          '2, Cantidad de subcampeonatos en mundiales por un pais. \n'\
          '3, Conocer cuál es el mundial con mayor número de goles. (1.5 pts) \n'\
          '4, Conocer cuantas veces se han enfrentado 2 equipos en los mundiales. (5 pts) \n'\
          '5, Cantidad de goles de las copas del mundo. (4 pts)')

    data = lectura()

    menu = {'1': campeon_mundial,
            '2': subcampeones,
            '3': copas_mundiales,
            '4': enfrentamientos,
            '5': mayor_goles_por_mundial}
    opcion = input('Ingrese una opcion: ')
    if opcion in menu:
        menu[opcion](data)
    else:
        print('opcion invalida')

if __name__ == '__main__':
    main()