"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    grupos = []
    
    with open("files/input/data.csv", "r") as file:
        for line in file:
            
            columns = line.strip().split('\t')
            column = columns[4].split(",")
            for pareja in column:
                pareja = pareja.split(":") 
                clave = pareja[0] 
                grupos.append((clave, 1))
    
    grupos = sorted(grupos, key=lambda x: x[0])

    result = {}
    for key, value in grupos:
        if key not in result.keys():
            result[key] = 0
        result[key] += value

    return result