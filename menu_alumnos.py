import os, time
datos=[]
op=1
while True:    #0 < op <9:
    print('1-Ingresar Datos')
    print('2-Mostrar Datos')
    print('3-Ordenar Datos')
    print('4-Sumar Datos')
    print('5-Promediar Datos')
    print('6-Ver edad sobre el promedio')
    print('7-Mostrar edad mayor')
    print('8-Mostrar Diferencia entre cada edad y promedio')
    print('9-Salir')

    op=int(input('Seleccione una opcion: '))
    os.system('cls')
    if op == 1:
        datos.append(int(input('Ingrese la edad del alumno: ')))
    if op == 2:
        print(datos)
    if op == 3:
        datos.sort()
        print(datos)
    if op == 4:
        print(sum(datos))
    if op == 5:
        print(sum(datos)/len(datos))
    if op == 6:
        for i in datos:    
            if i > sum(datos)/len(datos):
                print(i, end=' - ')
    if op == 7:
        print(max(datos))
    if op == 8:
        pass
    if op == 9:
        break
    if op < 1 or op > 9:
        print('Ingrese un número entre 1 y 9')
    print('')