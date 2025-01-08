"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
    with open("files/input/data.csv", "r") as file:
        month_frequency = dict()
        # iterate over the lines
        for index,line in enumerate(file):
            # split the line
            line:list[str] = line.strip().split('	')
            # Date
            date = line[2]
            # get the month
            month = date.split('-')[1]
            print(month)
            # if the month is not in the list add it
            if month not in month_frequency.keys():
                month_frequency[month] = 1
            # if is in the list add 1 to the count
            else:
                month_frequency[month] += 1
        # convert to the list of tuples
        month_frequency = list(month_frequency.items())
        # sort
        month_frequency = sorted(month_frequency, key=lambda x: x[0])
        # transform the month to string
        month_frequency = [(str(month), count) for month, count in month_frequency ]
    return month_frequency
