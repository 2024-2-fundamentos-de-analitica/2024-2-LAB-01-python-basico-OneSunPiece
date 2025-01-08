"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    # read the data.csv file with open
    with open('files/input/data.csv') as f:
        # read the lines
        lines = f.readlines()
        # list of tuples
        letter_frequency:list[tuple] = []

        # iterate over the lines
        for index,line in enumerate(lines):
            # split the line
            line:list[str] = line.strip().split('	')
            # letter
            letter = line[0]


            if letter not in [l[0] for l in letter_frequency]:
                letter_frequency.append((letter,1))
            else:
                for index, l in enumerate(letter_frequency):
                    if l[0] == letter:
                        letter_frequency[index] = (l[0],l[1]+1)
        # sort the list
        letter_frequency = sorted(letter_frequency, key=lambda x: x[0])

        return letter_frequency