"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

with open("data.csv", "r") as file:
    datos = file.readlines()

datos = [line.replace('\n', '') for line in datos]
datos = [line.split('\t') for line in datos]

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    return 214

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    resultado = []
    buscar = set(list(map(lambda dato: (str(dato[0])), datos)))

    buscar = list(buscar)
    buscar.sort()

    for i in buscar:
        conteoi = len(list(filter(lambda dato: (dato[0]==i), datos)))
        resultado.append((i, conteoi))

    return resultado

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    resultado = []
    buscar = set(list(map(lambda dato: (str(dato[0])), datos)))

    buscar = list(buscar)
    buscar.sort()

    for i in buscar:
        listai = list(filter(lambda dato: (dato[0]==i), datos))
        conteoi = 0
        for numero in listai:
            conteoi += int(numero[1])
        resultado.append((i, conteoi))

    return resultado


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    resultado = []
    buscar = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]

    for i in buscar:
        conteoi = len(list(filter(lambda dato: (dato[2][5:7]==i), datos)))
        resultado.append((i, conteoi))

    return resultado

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    resultado = []
    buscar = set(list(map(lambda dato: (str(dato[0])), datos)))

    buscar = list(buscar)
    buscar.sort()

    for i in buscar:
        listai = list(filter(lambda dato: (dato[0]==i), datos))
        listai = [dato[1] for dato in listai]
        resultado.append((str(i), int(max(listai)), int(min(listai))))

    return resultado

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    diccionarios = [i[4] for i in datos]
    diccionarios = [i.split(',') for i in diccionarios]

    final = []

    for i in diccionarios:
        final += i
    
    buscar = set(list(map(lambda dato: (str(dato[0:3])), final)))

    buscar = list(buscar)
    buscar.sort()

    resultado = []

    for i in buscar:
        conteoi = list(filter(lambda dato: (dato[0:3]==i), final))
        conteoi = list(map(lambda dato: (int(str(dato[4:]))), conteoi))

        if conteoi:
            resultado.append((i, min(conteoi), max(conteoi)))

    return resultado

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """

    respuesta = []

    buscar = set(list(map(lambda dato: (int(dato[1])), datos)))

    for i in buscar:
        temp = []
        for dato in datos:
            if int(dato[1]) == i:
                temp.append(str(dato[0]))

        respuesta.append((i, temp))

    return respuesta

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    respuesta = []
    buscar = set(list(map(lambda dato: (int(dato[1])), datos)))

    for i in buscar:
        temp = []
        for dato in datos:
            if int(dato[1]) == i:
                temp.append(str(dato[0]))

        temp = list(set(temp))
        temp.sort()

        respuesta.append((i, temp))

    return respuesta

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """

    diccionarios = [i[4] for i in datos]
    diccionarios = [i.split(',') for i in diccionarios]

    final = []

    for i in diccionarios:
        final += i
    
    buscar = set(list(map(lambda dato: (str(dato[0:3])), final)))

    buscar = list(buscar)
    buscar.sort()

    resultado = {}

    for i in buscar:
        conteoi = list(filter(lambda dato: (dato[0:3]==i), final))
        conteoi = list(map(lambda dato: (int(str(dato[4:]))), conteoi))

        if conteoi:
            resultado[i] = len(conteoi)

    return resultado

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    respuesta = []

    for i in datos:
        columna4 = i[3].split(',')
        columna5 = i[4].split(',')
        respuesta.append((str(i[0]), len(columna4), len(columna5)))

    return respuesta


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    diccionarios = [i[3] for i in datos]
    diccionarios = [i.split(',') for i in diccionarios]

    final = []

    for i in diccionarios:
        final += i
    
    buscar = set(list(map(lambda dato: (str(dato)), final)))

    buscar = list(buscar)
    buscar.sort()

    resultado = {}

    for i in buscar:
        conteo = 0;
        for j in range(len(diccionarios)):
            if str(i) in diccionarios[j]:
                conteo += int(datos[j][1])
        resultado[str(i)] = int(conteo)

    return resultado


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    buscar = set(list(map(lambda dato: (str(dato[0])), datos)))

    buscar = list(buscar)
    buscar.sort()

    resultado = {}

    for i in buscar:
        conteo = list(filter(lambda dato: (dato[0] == i), datos))
        diccionarios = [i[4] for i in conteo]
        diccionarios = [i.split(',') for i in diccionarios]
        final = []
        for j in diccionarios:
            final += j
        cuenta = sum(list(map(lambda dato: (int(dato[4:])), final)))

        resultado[str(i)] = int(cuenta)

    return(resultado)
