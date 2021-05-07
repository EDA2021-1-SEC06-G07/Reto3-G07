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
    #loadFeature(analyzer)
    #loadSentiment(analyzer)
    loadEvent(analyzer)
    
    return analyzer

"""
def loadSentiment(analyzer):
    sentimentfile = cf.data_dir + 'sentiment_values.csv'
    input_file = csv.DictReader(open(sentimentfile, encoding="utf-8"),
                                delimiter=",")
    for sentiment in input_file:
        model.addSentiment(analyzer, sentiment)

def loadDates(analyzer):
    eventsfile = cf.data_dir + 'user_track_hashtag_timestamp-small.csv'
    input_file = csv.DictReader(open(eventsfile, encoding="utf-8"),
                                delimiter=",")
    for evento in input_file:
        model.addEvent(analyzer, evento)
"""
def loadEvent(analyzer):
    eventfile = cf.data_dir + 'context_content_features-small.csv'
    input_file = csv.DictReader(open(eventfile, encoding="utf-8"),
                                delimiter=",")
    for event in input_file:
        model.addEvent(analyzer, event)

# Funciones para la carga de datos

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
def listSize(analyzer):
    
    return model.listSize(analyzer)


def indexHeight(analyzer):
    
    return model.indexHeight(analyzer)


def indexSize(analyzer):
    
    return model.indexSize(analyzer)


def minKey(analyzer):
    
    return model.minKey(analyzer)


def maxKey(analyzer):
    
    return model.maxKey(analyzer)