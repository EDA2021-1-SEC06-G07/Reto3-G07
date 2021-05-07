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
                'sentiment': None,
                'features': None,
                'instrumentalness': None,
                'liveness': None,
                'danceability': None,
                'valance': None,
                'loudness': None,
                'tempo': None,
                'acousticness': None,
                'energy': None}

    analyzer['features'] = lt.newList('ARRAY_LIST')
    analyzer['sentiment'] = lt.newList('ARRAY_LIST')
    analyzer['eventos'] = lt.newList(datastructure='ARRAY_LIST',cmpfunction=compareId)
    
    analyzer['instrumentalness'] = om.newMap(omaptype='RBT',
                                            comparefunction=compareValues)
    
    analyzer['liveness'] = om.newMap(omaptype='RBT',
                                            comparefunction=compareValues)

    analyzer['speechiness'] = om.newMap(omaptype='RBT',
                                            comparefunction=compareValues)

    analyzer['danceability'] = om.newMap(omaptype='RBT',
                                            comparefunction=compareValues)
    
    analyzer['valence'] = om.newMap(omaptype='RBT',
                                            comparefunction=compareValues)
    
    analyzer['loudness'] = om.newMap(omaptype='RBT',
                                            comparefunction=compareValues)

    analyzer['tempo'] = om.newMap(omaptype='RBT',
                                            comparefunction=compareValues)

    analyzer['acousticness'] = om.newMap(omaptype='RBT',
                                            comparefunction=compareValues)  

    analyzer['energy'] = om.newMap(omaptype='RBT',
                                            comparefunction=compareValues)      

    return analyzer 

# Funciones para agregar informacion al catalogo
def addFeature(analyzer, feature):
    lt.addLast(analyzer['features'], feature)

def addSentiment(analyzer, sentiment):
    if sentiment['vader_avg'] != None:
        tple= (sentiment['hashtag'],sentiment['vader_avg'])
        lt.addLast(analyzer['sentiment'],tple)

def addEvent(analyzer, evento):
    """
    features = analyzer['features']
    sentiment = analyzer['sentiment']

    modEvent = addFeatuere_event(features,evento,analyzer)
    finalEvent = addSentiment_event(sentiment,modEvent)
    """
    lt.addLast(analyzer['eventos'],evento)
    addKeyValueInstr(analyzer, evento)
    addKeyValueLive(analyzer, evento)
    addKeyValueAcous(analyzer, evento)
    addKeyValueDance(analyzer, evento)
    addKeyValueEnergy(analyzer, evento)
    addKeyValueLoud(analyzer, evento)
    addKeyValueTempo(analyzer, evento)
    addKeyValueVal(analyzer, evento)
    addKeyValueSpe(analyzer, evento)
    
# Funciones para creacion de datos
"""
def addFeatuere_event(features,event,analyzer):
    for feature in lt.iterator(features):
        if (event['user_id'] == feature['user_id']) and (event['track_id'] == feature['track_id']):
            event['track_id'] = feature
            return event


def addSentiment_event(sentiments,event):
    if event != None:
        for sentiment in lt.iterator(sentiments):
            hashtag,vader_avg = sentiment
            if event['hashtag'] == hashtag:
                event['hashtag'] = vader_avg
                return event
"""   

def addKeyValueInstr(analyzer,event):
    value = float(event['instrumentalness'])

    entryInstr = om.get(analyzer['instrumentalness'], value)
    if entryInstr is None:
        datentry = newValues(event)
        om.put(analyzer['instrumentalness'], value, datentry)
    else:
        datentry = me.getValue(entryInstr)
    lt.addLast(datentry, event)

def addKeyValueLive(analyzer,event):    
    value = float(event['liveness'])

    entryLive = om.get(analyzer['liveness'], value)
    if entryLive is None:
        datentry = newValues(event)
        om.put(analyzer['liveness'], value, datentry)
    else:
        datentry = me.getValue(entryLive)
    lt.addLast(datentry, event)

def addKeyValueSpe(analyzer,event):    
    value = float(event['speechiness'])

    entrySpe = om.get(analyzer['speechiness'], value)
    if entrySpe is None:
        datentry = newValues(event)
        om.put(analyzer['speechiness'], value, datentry)
    else:
        datentry = me.getValue(entrySpe)
    lt.addLast(datentry, event)


def addKeyValueDance(analyzer,event):
    value = float(event['danceability'])

    entryDance = om.get(analyzer['danceability'], value)
    if entryDance is None:
        datentry = newValues(event)
        om.put(analyzer['danceability'], value, datentry)
    else:
        datentry = me.getValue(entryDance)
    lt.addLast(datentry, event)

def addKeyValueVal(analyzer,event):
    value = float(event['valence'])

    entryVal = om.get(analyzer['valence'], value)
    if entryVal is None:
        datentry = newValues(event)
        om.put(analyzer['valence'], value, datentry)
    else:
        datentry = me.getValue(entryVal)
    lt.addLast(datentry, event)
    
def addKeyValueLoud(analyzer,event):
    value = float(event['loudness'])

    entryLoud = om.get(analyzer['loudness'], value)
    if entryLoud is None:
        datentry = newValues(event)
        om.put(analyzer['loudness'], value, datentry)
    else:
        datentry = me.getValue(entryLoud)
    lt.addLast(datentry, event)

def addKeyValueTempo(analyzer,event):
    value = float(event['tempo'])

    entryTempo = om.get(analyzer['tempo'], value)
    if entryTempo is None:
        datentry = newValues(event)
        om.put(analyzer['tempo'], value, datentry)
    else:
        datentry = me.getValue(entryTempo)
    lt.addLast(datentry, event)

def addKeyValueAcous(analyzer,event):
    value = float(event['acousticness'])

    entryAcous = om.get(analyzer['acousticness'], value)
    if entryAcous is None:
        datentry = newValues(event)
        om.put(analyzer['acousticness'], value, datentry)
    else:
        datentry = me.getValue(entryAcous)
    lt.addLast(datentry, event)

def addKeyValueEnergy(analyzer,event):
    value = float(event['energy'])
    
    entryEnergy = om.get(analyzer['energy'],value)
    if entryEnergy  is None:
        datentry = newValues(event)
        om.put(analyzer['instrumentalness'], value, datentry)
    else:
        datentry = me.getValue(entryEnergy)
    lt.addLast(datentry, event)


def newValues(event):
    lstEvent = lt.newList(datastructure='ARRAY_LIST')
    lt.addLast(lstEvent,event)
    return lstEvent

# Funciones de consulta
def listSize(analyzer):
    
    return lt.size(analyzer['eventos'])


def indexHeight(analyzer):
   
    return om.height(analyzer['instrumentalness'])


def indexSize(analyzer):
    
    return om.size(analyzer['instrumentalness'])


def minKey(analyzer):
    
    return om.minKey(analyzer['instrumentalness'])


def maxKey(analyzer):
    
    return om.maxKey(analyzer['instrumentalness'])

# Funciones utilizadas para comparar elementos dentro de una lista
def compareId(evento1, evento2):
    if evento1['id'] == evento2['id']:
        return 0
    elif evento1['id'] > evento2['id']:
        return 1
    else:
        return -1

def compareValues(v1,v2):
    if (v1 == v2):
        return 0
    elif v1 > v2:
        return 1
    else:
        return -1


# Funciones de ordenamiento
