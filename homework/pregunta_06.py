"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    grupos = {}
    
    with open("files/input/data.csv", "r") as file:
        for line in file:
            
            columns = line.strip().split('\t')
            column = columns[4].split(",")
            for pareja in column:
                pareja = pareja.split(":") 
                clave = pareja[0]
                valor = int(pareja[1]) 
            
                if clave not in grupos:
                    grupos[clave] = []
                grupos[clave].append(valor)


    resultado = []
    for clave, valores in grupos.items():
        maximo = max(valores)
        minimo = min(valores)
        resultado.append((clave, minimo, maximo))

    resultado = sorted(resultado, key=lambda x: x[0])

    return resultado