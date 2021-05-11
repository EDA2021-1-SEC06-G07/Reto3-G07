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
import random
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import orderedmapstructure as oms
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
                'artistas_u':None,
                'tracks_u': None,
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

    analyzer['artistas_u'] = om.newMap(omaptype='RBT')
    analyzer['tracks_u'] = om.newMap(omaptype='RBT')

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

    addArtista(analyzer,evento)
    addTrack(analyzer,evento)

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
def addArtista(analyzer,event):
    value = event['artist_id']
    omap = analyzer['artistas_u']

    entryInstr = oms.contains(omap, value)
    if entryInstr == False:
        datentry = newValues()
        om.put(omap, value, datentry)
    else:
        entry = om.get(omap,value)
        datentry = me.getValue(entry)
    lt.addLast(datentry, event)

def addTrack(analyzer,event):
    value = event['track_id']
    omap = analyzer['tracks_u']

    entryInstr = oms.contains(omap, value)
    if entryInstr == False:
        datentry = newValues()
        om.put(omap, value, datentry)
    else:
        entry = om.get(omap,value)
        datentry = me.getValue(entry)
    lt.addLast(datentry, event)

def addKeyValueInstr(analyzer,event):
    value = float(event['instrumentalness'])
    omap = analyzer['instrumentalness']

    entryInstr = oms.contains(omap, value)
    if entryInstr == False:
        datentry = newValues()
        om.put(omap, value, datentry)
    else:
        entry = om.get(omap,value)
        datentry = me.getValue(entry)
    lt.addLast(datentry, event)

def addKeyValueLive(analyzer,event):    
    value = float(event['liveness'])
    omap = analyzer['liveness']

    entryInstr = oms.contains(omap, value)
    if entryInstr == False:
        datentry = newValues()
        om.put(omap, value, datentry)
    else:
        entry = om.get(omap,value)
        datentry = me.getValue(entry)
    lt.addLast(datentry, event)

def addKeyValueSpe(analyzer,event):    
    value = float(event['speechiness'])
    omap = analyzer['speechiness']

    entryInstr = oms.contains(omap, value)
    if entryInstr == False:
        datentry = newValues()
        om.put(omap, value, datentry)
    else:
        entry = om.get(omap,value)
        datentry = me.getValue(entry)
    lt.addLast(datentry, event)


def addKeyValueDance(analyzer,event):
    value = float(event['danceability'])
    omap = analyzer['danceability']

    entryInstr = oms.contains(omap, value)
    if entryInstr == False:
        datentry = newValues()
        om.put(omap, value, datentry)
    else:
        entry = om.get(omap,value)
        datentry = me.getValue(entry)
    lt.addLast(datentry, event)

def addKeyValueVal(analyzer,event):
    value = float(event['valence'])
    omap = analyzer['valence']

    entryInstr = oms.contains(omap, value)
    if entryInstr == False:
        datentry = newValues()
        om.put(omap, value, datentry)
    else:
        entry = om.get(omap,value)
        datentry = me.getValue(entry)
    lt.addLast(datentry, event)
    
def addKeyValueLoud(analyzer,event):
    value = float(event['loudness'])
    omap = analyzer['loudness']

    entryInstr = oms.contains(omap, value)
    if entryInstr == False:
        datentry = newValues()
        om.put(omap, value, datentry)
    else:
        entry = om.get(omap,value)
        datentry = me.getValue(entry)
    lt.addLast(datentry, event)

def addKeyValueTempo(analyzer,event):
    value = float(event['tempo'])
    omap = analyzer['tempo']

    entryInstr = oms.contains(omap, value)
    if entryInstr == False:
        datentry = newValues()
        om.put(omap, value,datentry )
    else:
        entry = om.get(omap,value)
        datentry = me.getValue(entry)
    lt.addLast(datentry, event)

def addKeyValueAcous(analyzer,event):
    value = float(event['acousticness'])
    omap = analyzer['acousticness']

    entryInstr = oms.contains(omap, value)
    if entryInstr == False:
        datentry = newValues()
        om.put(omap, value, datentry)
    else:
        entry = om.get(omap,value)
        datentry = me.getValue(entry)
    lt.addLast(datentry, event)

def addKeyValueEnergy(analyzer,event):
    value = float(event['energy'])
    omap = analyzer['energy']

    entryInstr = oms.contains(omap, value)
    if entryInstr == False:
        datentry = newValues()
        om.put(omap, value, datentry)
    else:
        entry = om.get(omap,value)
        datentry = me.getValue(entry)
    lt.addLast(datentry, event)

def newValues():
    lstEvent = lt.newList(datastructure='ARRAY_LIST')
    return lstEvent

# Funciones de consulta
def listSize(lst):
    return lt.size(lst)

def subList(lst,pos,numelem):
    return lt.subList(lst,pos,numelem)

def keysSize(omap):
    keys = oms.keySet(omap)
    return lt.size(keys)

def getValue(map1,key):
    entry = mp.get(map1,key)
    return me.getValue(entry)




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
def caracterizar_reproducciones_R1(analyzer,feature,minF,maxF):
    omap = analyzer[feature]
    values = oms.values(omap,minF,maxF)
    
    artistas = lt.newList('ARRAY_LIST')
    events = lt.newList('ARRAY_LIST')
    for valor in lt.iterator(values):
        añadir_evento_artista_AY(valor,events,artistas)
         
    return (lt.size(events),lt.size(artistas))

def añadir_evento_artista_AY(values,lstEvent,lstArtistas):
    for event in lt.iterator(values):
        lt.addLast(lstEvent,event)
        if event['artist_id'] not in lt.iterator(lstArtistas):
            lt.addLast(lstArtistas,event['artist_id'])

def musica_festejar_R2(analyzer,minE,maxE,minD,maxD):
    omapEnergy = analyzer['energy']
    omapDance = analyzer['danceability']

    rta = relacionar_features_AY(omapEnergy,omapDance,
                                minE,maxE,minD,maxD)

    return rta

def musica_estudiar_R3(analyzer,minI,maxI,minT,maxT):
    omapInstr = analyzer['instrumentalness']
    omapTempo = analyzer['tempo']

    rta = relacionar_features_AY(omapInstr,omapTempo,
                                minI,maxI,minT,maxT)
                                
    return rta

def relacionar_features_AY(feature1,feature2,min1,max1,min2,max2):
    rank1= oms.values(feature1,min1,max1)
    rank2 = oms.values(feature2,min2,max2)

    lstR1 = obtener_valores_AY(rank1)
    lstR2 = obtener_valores_AY(rank2)
    
    omap = keyValuesNewOmap(lstR2,'track_id')

    tracksOmap = oms.keySet(omap)
    pistas = lt.newList('ARRAY_LIST')
    tracksU = lt.newList('ARRAY_LIST')

    for pista in lt.iterator(lstR1):
        if (pista['track_id'] in lt.iterator(tracksOmap))and(pista['track_id']  not in lt.iterator(tracksU)):
            lt.addLast(pistas,pista)
            lt.addLast(tracksU,pista['track_id'])
    
    fiveEvents = al_azar_AY(pistas)
    return (lt.size(tracksU),fiveEvents)

def keyValuesNewOmap(lst,value):
    omap = om.newMap(omaptype='RBT',comparefunction=compareValues)
    for valor in lt.iterator(lst):
        entryInstr = oms.contains(omap, valor[value])
        if entryInstr == False:
            datentry = newValues()
            om.put(omap, valor[value], datentry)
        else:
            entry = om.get(omap,valor[value])
            datentry = me.getValue(entry)
        lt.addLast(datentry, valor)
    return omap

def obtener_valores_AY(lstValues):
    events = lt.newList('ARRAY_LIST')
    for valor in lt.iterator(lstValues):
        añadir_evento_AY(valor,events)
    return events

def añadir_evento_AY(values,lst):
    for valor in lt.iterator(values):
        lt.addLast(lst,valor)

def al_azar_AY(pistas):
    eventos = lt.newList('ARRAY_LIST')
    marca = 0
    while marca < 5:
        rdm = random.randrange(1,lt.size(pistas))
        evento = lt.getElement(pistas,rdm)
        
        if evento not in lt.iterator(eventos):
            lt.addLast(eventos,evento)
            marca += 1
        
    return eventos

def generos_musicales(analyzer,generos,newGen,min1,max1):
    generos = generos.lower()
    generos = generos.split(',')

    lst_new_gen = None
    if newGen != None:
        lst_new_gen = oms.values(analyzer['tempo'],min1,max1)

    
    reggae = oms.values(analyzer["tempo"],60,90)
    down_tempo = oms.values(analyzer["tempo"],70,100)
    chill_out = oms.values(analyzer["tempo"],90,120)
    hip_hop = oms.values(analyzer["tempo"],85,115)
    jazz_funk= oms.values(analyzer["tempo"],120,125)
    pop= oms.values(analyzer["tempo"],100,130)
    r_b= oms.values(analyzer["tempo"],60,80)
    rock =oms.values(analyzer["tempo"],110,140)
    metal = oms.values(analyzer["tempo"],140,160)

    num_rep = 0
    lst_rep_gen = lt.newList('ARRAY_LIST')

    for genero in generos:
        if genero == "reggae":
            rango = '60 - 90'
            map1 = obtener_valores_R4_AY(genero,reggae,rango)
            suma = getValue(map1,'num_rep')
            lt.addLast(lst_rep_gen,map1)
            num_rep+=suma

        elif genero == "down-tempo":
            rango = '70 - 100'
            map1 = obtener_valores_R4_AY(genero,down_tempo,rango)
            suma = getValue(map1,'num_rep')
            lt.addLast(lst_rep_gen,map1)
            num_rep+=suma
        elif genero == "chill-out":
            rango = '90 - 120'
            map1 = obtener_valores_R4_AY(genero,chill_out,rango)
            suma = getValue(map1,'num_rep')
            lt.addLast(lst_rep_gen,map1)
            num_rep+=suma
        elif genero == "hip-hop":
            rango = '85 - 115'
            map1 = obtener_valores_R4_AY(genero,hip_hop,rango)
            suma = getValue(map1,'num_rep')
            lt.addLast(lst_rep_gen,map1)
            num_rep+=suma
        elif genero == "jazz and funk":
            rango = '120 - 125'
            map1 = obtener_valores_R4_AY(genero,jazz_funk,rango)
            suma = getValue(map1,'num_rep')
            lt.addLast(lst_rep_gen,map1)
            num_rep+=suma
        elif genero == "pop":
            rango = '100 - 130'
            map1 = obtener_valores_R4_AY(genero,pop,rango)
            suma = getValue(map1,'num_rep')
            lt.addLast(lst_rep_gen,map1)
            num_rep+=suma
        elif genero == "r&B":
            rango = '60 - 80'
            map1 = obtener_valores_R4_AY(genero,r_b,rango)
            suma = getValue(map1,'num_rep')
            lt.addLast(lst_rep_gen,map1)
            num_rep+=suma
        elif genero == "rock":
            rango = '110 - 140'
            map1 = obtener_valores_R4_AY(genero,rock,rango)
            suma = getValue(map1,'num_rep')
            lt.addLast(lst_rep_gen,map1)
            num_rep+=suma
        elif genero == "metal":
            rango = '100 - 160'
            map1 = obtener_valores_R4_AY(genero,metal,rango)
            suma = getValue(map1,'num_rep')
            lt.addLast(lst_rep_gen,map1)
            num_rep+=suma
        else:
            if newGen != None:
                rango = f'{min1} - {max1}'
                map1 = obtener_valores_R4_AY(newGen,lst_new_gen,rango)
                suma = getValue(map1,'num_rep')
                lt.addLast(lst_rep_gen,map1)
                num_rep+=suma
    return (num_rep,lst_rep_gen)        

def obtener_valores_R4_AY(genero,lst,rango):
    lst_genero = obtener_valores_AY(lst)
    omap_genero= keyValuesNewOmap(lst_genero,'artist_id')
    artistas_u = oms.keySet(omap_genero)
    num_arts = lt.size(artistas_u)
    ten_arts = lt.subList(artistas_u,1,10)
    rep = lt.size(lst_genero)
    map1 = mp.newMap(numelements=5)
    mp.put(map1,'genero',genero)
    mp.put(map1,'num_rep',rep)
    mp.put(map1,'numero_arts',num_arts)
    mp.put(map1,'ten_arts',ten_arts)
    mp.put(map1,'rango',rango)
    return map1
        