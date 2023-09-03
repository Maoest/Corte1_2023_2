f = ['1 de Enero: Año Nuevo',
     '9 de Enero: Día de los Reyes Magos',
     '20 de Marzo: Día de San José',
     '2 de Abril: Domingo de Ramos',
     '6 de Abril: Jueves Santo',
     '7 de Abril: Viernes Santo',
     '9 de Abril: Domingo de Resurrección',
     '1 de Mayo: Día de Trabajo',
     '22 de Mayo: Día de la Ascensión',
     '12 de Junio: Corpus Christi',
     '19 de Junio: Sagrado Corazón',
     '3 de Julio: San Pedro y San Pablo',
     '20 de Julio: Día de la Independencia',
     '7 de Agosto: Batalla de Boyacá',
     '21 de Agosto: La asunción de la Virgen',
     '16 de Octubre: Día de la Raza',
     '6 de Noviembre: Todos los Santos',
     '13 de Noviembre: Independencia de Cartagena',
     '8 de Diciembre: Día de la Inmaculada Concepción',
     '25 de Diciembre: Día de Navidad']

D = ['Enero : 30 días', 'Febrero: 28 días', 'Marzo: 31 días', 'Abril: 30 días', 'Mayo: 31 días', 'Junio: 30 días',
     'Julio: 31 días', 'Agosto: 31 días', 'Septiembre: 30 días', 'Octubre: 31 días', 'Noviembre: 30 días', 'Diciembre: 31 días']


def buscar_festivos(mes):
    i = 0
    festivos = []
    for i in range(len(f)):
        if mes in f[i]:
            festivos.append(f[i],)
        i += 1
    return festivos


def main():
    x=0
    mes = input('Ingrese el mes a indagar: ').capitalize()
    while True: 
        if mes in D[x]:
            festivos = buscar_festivos(mes)
            if len(festivos)!= 0:
                print(f'{D[x]}. Festivos: {", ".join(festivos)}')
                break
            else:
                print(f'{D[x]}. No hay festivos registrados para este mes.')
                break
        else:
            x+=1

if __name__ == "__main__":
    main()





