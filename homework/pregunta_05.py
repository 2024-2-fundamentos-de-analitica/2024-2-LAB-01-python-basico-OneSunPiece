"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    grupos = {}
    
    with open("files/input/data.csv", "r") as file:
        for line in file:
            
            columns = line.strip().split('\t')
            letra = columns[0] 
            valor = int(columns[1]) 
            
            if letra not in grupos:
                grupos[letra] = []
            grupos[letra].append(valor)


    resultado = []
    for letra, valores in grupos.items():
        maximo = max(valores)
        minimo = min(valores)
        resultado.append((letra, maximo, minimo))

    resultado = sorted(resultado, key=lambda x: x[0])

    return resultado