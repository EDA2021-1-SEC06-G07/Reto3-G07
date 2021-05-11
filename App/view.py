"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """
import time
import datetime
import tracemalloc
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar crear catálogo")
    print("2- Cargar información en el catálogo")
    print("3- R1: Caracterizar las reproducciones")
    print("4- R2: Encontrar música para festejar")
    print("5- R3: Encontrar música para estudiar")
    print("6- R4: Estudiar los géneros musicales")
    print("7- R5: Indicar el género musical más escuchado en el tiempo")

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        analyzer = controller.init()

    elif int(inputs[0]) == 2:
        print("\nCargando información de eventos ....")
        tracemalloc.start()
        delta_time = -1.0
    
        start_time= float(time.perf_counter()*1000)
        
        controller.loadData(analyzer)
    
    
        stop_time = float(time.perf_counter()*1000)
        tracemalloc.stop()
        delta_time = stop_time - start_time
        
    
        print(delta_time)
        print()
        print('Eventos cargados: ' + str(controller.listSize(analyzer['eventos'])))
        print('Artistas únicos: ' + str(controller.keysSize(analyzer['artistas_u'])))
        print('Pistas únicas de audio: ' + str(controller.keysSize(analyzer['tracks_u'])))
        print()
        primeros = controller.subList(analyzer['eventos'],1,5)
        print('--- Primeros cinco eventos cargados---')
        n = 1
        for evento in lt.iterator(primeros): 
            print(f'evento {n}:')
            print(evento)
            n+=1
        print()
        pos = controller.listSize(analyzer['eventos'])
        ultimos = controller.subList(analyzer['eventos'],pos-5,5)
        print('--- Ultimos cinco eventos cargados---' )
        n = 1
        for evento in lt.iterator(primeros): 
            print(f'evento {n}:')
            print(evento)
            n+=1
        print()
        print(controller.hola(analyzer))

    elif int(inputs[0]) == 3:
        feature = str(input('feature: '))
        featureL = feature.lower()
        minF = float(input('minF: '))
        maxF = float(input('maxF: '))
        totalR,totalA = (controller.requerimiento_1(analyzer,featureL,minF,maxF))
        print('\n')
        print('***** Req No. 1 resultados *****')
        print()
        print(f'{feature} entre {minF} & {maxF}')
        print(f'Total de reproducciones: {totalR} || Total de artistas únicos: {totalA}')
        print()

    elif int(inputs[0]) == 4:
        minE = float(input('Mínimo valor energy: '))
        maxE = float(input('Máximo valor energy: '))
        minD = float(input('Mínimo valor danceability: '))
        maxD = float(input('Máximo valor danceability: '))
        size,cinco = (controller.requerimiento_2(analyzer,minE,maxE,minD,maxD))
        print('\n')
        print('***** Req No. 2 resultados *****')
        print()
        print(f'Energy entre {minE} - {maxE}')
        print(f'Danceability entre {minD} - {maxD}')
        print(f'Total de tracks únicos en eventos: {size}')
        print()
        print('--- Tracks únicos ---')
        n = 1
        for evento in lt.iterator(cinco): 
            track_id = evento['track_id']
            energy = evento['energy']
            dance = evento['danceability']
            print(f'track {n}: {track_id} con energy de {energy} & danceability de {dance}')
            n+=1
        print()
        


    elif int(inputs[0]) == 5:
        minI = float(input('Mínimo valor isntrumentalness: '))
        maxI = float(input('Máximo valor isntrumentalness: '))
        minT = float(input('Mínimo valor tempo: '))
        maxT = float(input('Máximo valor tempo: '))
        size,cinco = (controller.requerimiento_3(analyzer,minI,maxI,minT,maxT))
        print('\n')
        print('***** Req No. 3 resultados *****')
        print()
        print(f'Instrumentalness entre {minI} - {maxI}')
        print(f'Tempo entre {minT} - {maxT}')
        print(f'Total de tracks únicos en eventos: {size}')
        print()
        print('--- Tracks únicos ---')
        n = 1
        for evento in lt.iterator(cinco): 
            track_id = evento['track_id']
            instr= evento['instrumentalness']
            tempo = evento['tempo']
            print(f'track {n}: {track_id} con instrumentalness de {instr} & tempo de {tempo}')
            n+=1
        print()

    elif int(inputs[0]) == 6:
        newGen = None 
        min1 = 0
        max1 = 0
        generos = str(input('Generos separados por (\",\") y sin espacios: '))
        deseo = str(input('¿Desea añadir un nuevo genero? (si o no): '))
        if deseo == 'si':
            newGen = str(input('Nombre del nuevo genero: '))
            min1 = float(input('Mínimo valor tempo: '))
            max1 = float(input('Máximo valor tempo: '))
        num_rep,lst = (controller.requerimiento_4(analyzer,generos,newGen,min1,max1))
        print('\n')
        print('***** Req No. 4 resultados *****')
        print()
        print(f'Total de reproducciones: {num_rep}')
        print()

        for map1 in lt.iterator(lst):
            genero = controller.getValue(map1,'genero')
            rango = controller.getValue(map1,'rango')
            rep = controller.getValue(map1,'num_rep')
            num_arts = controller.getValue(map1,'numero_arts')
            arts = controller.getValue(map1,'ten_arts')
            print(f'===== {genero} =====')
            print(f'para {genero} entre {rango}')
            print(f'reproducciones de {genero}: {rep} con {num_arts} diferentes artistas')
            print()
            n = 1
            for id1 in lt.iterator(arts):
                print(f'Artista {n}: {id1}')
                n+=1
            print()
                
        print()

    elif int(inputs[0]) == 7:
        minh = str(input('Valor mínimo hora: '))
        minm = str(input('Valor mínimo de los minutos de la hora anterior: '))
        maxh = str(input('Valor máximo hora: '))
        maxm = str(input('Valor máximo de los minutos de la hora anterior: '))
        minT = datetime.time(minh,minm,'00')
        maxT = datetime.time(maxh,maxm,'00')
        lst,prim,repT= controller.requerimiento_5(analyzer,minh,maxh)
        print()
        print('***** Req No. 5 resultados *****')
        print(f'Hay un total de {repT} reproducciones entre {minT} y {maxT}')
        print()
        print('===== Generos ordenados =====')
        n=1
        for dict in lt.iterator(lst):
            genero = controller.getValue(dict,'genero')
            rep = controller.getValue(dict,'num_rep')
            print(f'TOP {n}: {genero} con {rep} reps')
            n+=1
        print()
        prmGen = controller.getValue(prim,'genero')
        prmRep = controller.getValue(prim,'num_rep')
        print(f'El genero TOP es {prmGen} con {prmRep} reproducciones...')
        print()
        u_tracks = controller.getValue()
        lstPrm = controller.getValue(prim,'hashtag')
        n
        for track in lt.iterator(lstPrm):
            track_id,tple=track
            numH,prmd =tple

    else:
        sys.exit(0)
sys.exit(0)
