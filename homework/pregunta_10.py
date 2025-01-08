"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    grupos = []
    
    with open("files/input/data.csv", "r") as file:
        for line in file:
            
            columns = line.strip().split('\t')
            letra = columns[0] 
            columna3 = columns[3].split(",")
            valor3 = len(columna3)
            columna4 = columns[4].split(",")
            valor4 = len(columna4)
            
            grupos.append((letra, valor3, valor4))


    return grupos