﻿"""
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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def init():
    analyzer = model.newAnalyzer()
    return analyzer

def loadData(analyzer):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    loadSentiment(analyzer)
    loadDates(analyzer)
    loadEvent(analyzer)
    
    
    return analyzer


def loadSentiment(analyzer):
    sentimentfile = cf.data_dir + 'sentiment_values.csv'
    input_file = csv.DictReader(open(sentimentfile, encoding="utf-8"),
                                delimiter=",")
    for sentiment in input_file:
        model.addSentiment(analyzer, sentiment)

def loadDates(analyzer):
    timestampfile = cf.data_dir + 'user_track_hashtag_timestamp-small.csv'
    input_file = csv.DictReader(open(timestampfile, encoding="utf-8"),
                                delimiter=",")
    for evento in input_file:
        model.addtimestamp(analyzer, evento)

def loadEvent(analyzer):
    eventfile = cf.data_dir + 'context_content_features-small.csv'
    input_file = csv.DictReader(open(eventfile, encoding="utf-8"),
                                delimiter=",")
    for event in input_file:
        model.addEvent(analyzer, event)

# Funciones para la carga de datos

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
def requerimiento_1(analyzer,feature,minF,maxF):
    return model.caracterizar_reproducciones_R1(analyzer,feature,minF,maxF)

def requerimiento_2(analyzer,minE,maxE,minD,maxD):
    return model.musica_festejar_R2(analyzer,minE,maxE,minD,maxD)

def requerimiento_3(analyzer,minI,maxI,minT,maxT):
    return model.musica_estudiar_R3(analyzer,minI,maxI,minT,maxT)

def requerimiento_4(analyzer,generos,newGen,min1,max1):
    return model.generos_musicales(analyzer,generos,newGen,min1,max1)

def requerimiento_5(analyzer,minh,maxh):
    return model.generos_tiempo(analyzer,minh,maxh)
    
def listSize(lst):
    return model.listSize(lst)

def keysSize(omap):
    return model.keysSize(omap)

def subList(lst,pos,numelem):
    return model.subList(lst,pos,numelem)

def getValue(map1,key):
    return model.getValue(map1,key)

def hola(analyzer):
    return model.hola(analyzer)
