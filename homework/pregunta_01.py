"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """

    # read the data.csv file with open
    with open('files/input/data.csv') as f:
        # read the lines
        lines = f.readlines()
        # initialize the sum
        suma: int = 0
        # iterate over the lines
        for index,line in enumerate(lines):
            # split the line
            line:list[str] = line.strip().split('	')
            # add the second element to the sum
            suma += int(line[1])
        return suma