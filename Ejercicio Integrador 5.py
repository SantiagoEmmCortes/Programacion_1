#Ejercicio Integrador 05
#En la base de datos de la división de armamento de industrias Wayne se tiene una
#  información la cual están con la necesidad de cambiar el formato la lista de habilidades
#  con sus respectivos puntos de combate, actualmente cada una de ellas está presente como
#  un diccionario pero para su nuevo sistema requieren que el tipo de dato sea una tupla la
#  cual albergue solamente el nombre de la habilidad y su poder al estilo ("rayo laser", 99).
# A su vez, todas y cada una de las habilidades deben estar dentro de una lista de 
#  habilidades, la cual debe ser el valor de una key que conforme un diccionario, como key
#  para albergarlas usaremos “habilidades_UTN”.

#Ordenar la lista de "habilidades_UTN" según el número de cada tupla, de manera ascendente. 
#Una vez hecho esto, deberá recorrer dicha lista imprimiendo sus valores,
# conjuntamente con la key que integra dicha estructura de datos.


habilidades = [
    {
        "Nombre": "Vision-X",
        "Poder": 64
    },
    {
        "Nombre": "Vuelo",
        "Poder": 32
    },
    {
        "Nombre": "Inteligencia",
        "Poder": 256
    },
    {
        "Nombre": "Metamorfosis",
        "Poder": 1024
    },
    {
        "Nombre": "Super Velocidad",
        "Poder": 128
    },
    {
        "Nombre": "Magia",
        "Poder": 512
    }
]


habilidades_UTN = []

for habilidad in habilidades:
    nombre_habilidad = habilidad["Nombre"]
    poder_habilidad = habilidad["Poder"]
    tupla_habilidad = (nombre_habilidad, poder_habilidad)
    habilidades_UTN.append(tupla_habilidad)

for i in range(len(habilidades_UTN)):
        print("Habilidad {0}: {1}".format(i+1,habilidades_UTN[i]))

#Trabajo incompleto, no logro ordenar las tuplas de la manera que pide