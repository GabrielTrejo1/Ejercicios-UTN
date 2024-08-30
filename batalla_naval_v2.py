import os,time

def limpiar_pantalla():
    os.system('cls')

def mostrar_matriz(n,mat):
    print(f'Turno del jugador {n}')
    cont=0
    coordendas=['A','B','C','D','E']
    print('\t1\t2\t3\t4\t5')
    print()
    for lista in mat:
        print(coordendas[cont], end='\t')
        for j in lista:
            print(j, end='\t')
        print('\n')
        cont+=1

trad_coords={'A':0,'B':1,'C':2,'D':3,'E':4}
def agregar_barco(n,matriz):
    limpiar_pantalla()
    for i in range(5):              #lo mismo pero con diccionarios
        mostrar_matriz(n,matriz)
        while True:
            coord_barco=input('Ingrese la coordenada donde desea poner su barco, Ej. A1: ').upper()
            if 1<len(coord_barco)<3:
                if coord_barco[0] in trad_coords and 0<int(coord_barco[1])<6 and matriz[trad_coords[coord_barco[0]]][int(coord_barco[1])-1]!='B':
                    matriz[trad_coords[coord_barco[0]]][int(coord_barco[1])-1]='B'
                    break
                else:
                    print('Coordenada no valida, vuelva a intentar')
            else:
                print('Coordenada no valida, vuelva a intentar')
        limpiar_pantalla()
        mostrar_matriz(n,matriz)
        time.sleep(1)
        limpiar_pantalla()
        
def disparar(n,matriz,matriz_de_juego,contador):
    mostrar_matriz(n,matriz_de_juego)
    while True:
        disparo=input('Ingrese la coordenada donde desea disparar, EJ. E5: ').upper()
        if 1<len(disparo)<3:
            if disparo[0] in trad_coords and 0<int(disparo[1])<6 and (matriz_de_juego[trad_coords[disparo[0]]][int(disparo[1])-1]=='*' or matriz_de_juego[trad_coords[disparo[0]]][int(disparo[1])-1]=='B'):
                if matriz[trad_coords[disparo[0]]][int(disparo[1])-1]=='B':
                    matriz_de_juego[trad_coords[disparo[0]]][int(disparo[1])-1]='H'
                    contador+=1
                else:
                    matriz_de_juego[trad_coords[disparo[0]]][int(disparo[1])-1]='A'
                break
            else:
                print('Coordenada no valida, vuelva a intentar')
        else:
            print('Coordenada no valida, vuelva a intentar')
    limpiar_pantalla()
    mostrar_matriz(n,matriz_de_juego)
    time.sleep(2)
    limpiar_pantalla()
    return contador

reset = ''
while reset !='X':
    mat_player_one=[['*' for _ in range(5)] for _ in range(5)]
    mat_player_two=[['*' for _ in range(5)] for _ in range(5)]
    mat_player_one_play=[['*' for _ in range(5)] for _ in range(5)]
    mat_player_two_play=[['*' for _ in range(5)] for _ in range(5)]
    cont_p1=0
    cont_p2=0

    agregar_barco(1,mat_player_one)
    agregar_barco(2,mat_player_two)
            
    while cont_p1 != 5 and cont_p2 != 5:
        cont_p1 = disparar(1, mat_player_two, mat_player_one_play, cont_p1)
        cont_p2 = disparar(2, mat_player_one, mat_player_two_play, cont_p2)
        
    if cont_p1 == 5 and cont_p2 == 5:
        print("Empate")
    elif cont_p2 == 5:
        print('El ganador es el Jugador 2')
    elif cont_p1 == 5:
        print('El ganador es el Jugador 1')
        
    reset = input('Si desea volver a jugar pulse cualquier tecla,\ncaso contrario pulse X: ').upper()
print('FIN.')