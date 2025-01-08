"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    sequence = []
    with open("files/input/data.csv", "r") as file:
        for line in file:
            columns = line.strip().split('\t')
            sequence.append((columns[0], int(columns[1])))

    sequence = sorted(sequence, key=lambda x: x[0])
    
    result = {}
    for key, value in sequence:
        if key not in result.keys():
            result[key] = 0
        result[key] += value

    letter_frequency = list(result.items())
        
    return letter_frequency
