"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import orderedmap as om
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newAnalyzer():
    analyzer = {'eventos': None,
                'track_id': None}
    analyzer['eventos'] = lt.newList('ARRAY_LIST', compareDate)
    
    analyzer['track_id'] = om.newMap(omaptype='BST',
                                    comparefunction=compareIds)  
    return analyzer                                                                
# Funciones para agregar informacion al catalogo
def addEvent(analyzer, evento):
    lt.addLast(analyzer['eventos'], evento)
    addTrackId(analyzer['track_id'], evento)

# Funciones para creacion de datos

def addTrackId(map1, evento):
    
    track_id = evento['track_id']
    entry = om.get(map1, track_id)
    if entry is None:
        datentry = newDataEntry(evento)
        om.put(map1, track_id, datentry)
    
    return map

def newDataEntry(evento):
    entry = {'evento': None, 'features': None}
    entry['evento'] = evento
    entry['features'] = mp.newMap(numelements=123,
                                maptype='CHAINING',
                                loadfactor=4.0)
    return entry
# Funciones de consulta
def crimesSize(analyzer):
    
    return lt.size(analyzer['eventos'])


def indexHeight(analyzer):
   
    return om.height(analyzer['track_id'])


def indexSize(analyzer):
    
    return om.size(analyzer['track_id'])


def minKey(analyzer):
    
    return om.minKey(analyzer['track_id'])


def maxKey(analyzer):
    
    return om.maxKey(analyzer['track_id'])

# Funciones utilizadas para comparar elementos dentro de una lista
def compareDate(evento1, evento2):
    if evento1['created_at'] > evento2['created_at']:
        return 1
    else:
        return -1

def compareIds(id1,id2):
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1


# Funciones de ordenamiento
