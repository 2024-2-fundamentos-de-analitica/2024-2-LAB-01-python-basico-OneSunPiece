"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    grupos = []
    with open("files/input/data.csv", "r") as file:
        for line in file:
            columns = line.strip().split('\t')
            column = columns[4].split(",")
            for pareja in column:
                pareja = pareja.split(":") 
                valor = pareja[1] 
                grupos.append((columns[0], int(valor)))

    grupos = sorted(grupos, key=lambda x: x[0])
    
    result = {}
    for key, value in grupos:
        if key not in result.keys():
            result[key] = 0
        result[key] += value

    return result