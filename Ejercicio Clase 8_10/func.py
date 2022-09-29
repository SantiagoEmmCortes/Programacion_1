import json
import re

def stark_normalizar_datos(lista:list):
    '''
    Castea al tipo de dato correcto las keys necesarias de una lista

    Recibe una lista de diccionarios
    '''
    if lista:
        flag_datos_normalizados = False
        for heroe in lista:
            if type(heroe["altura"]) != float or type(heroe["peso"]) != float or type(heroe["fuerza"]) != int and flag_datos_normalizados == False:
                heroe["altura"] = float(heroe["altura"])
                heroe["peso"] = float(heroe["peso"])
                heroe["fuerza"] = int(heroe["fuerza"])
                flag_datos_normalizados = True
    else:
        print("Error: Lista de heroes vacia")

def imprimir_dato(dato:str):
    '''
    Recibe un string y lo imprime en pantalla
    '''
    print(dato)

def imprimir_menu_desafio_5():
    '''
    Imprime el menu de opciones en pantalla
    '''
    menu = "A  - Heroes masculinos\nB  - Heroes femeninos\nC  - Heroe masculino mas alto\nD  - Heroe femenino mas alto\n"
    menu += "E  - Heroe masculino mas bajo\nF  - Heroe femenino mas bajo\nG  - Promedio de altura de heroes masculinos\n"
    menu += "H  - Promedio de altura de heroes femeninos\nJ  - Cantidad de heroes con cada color de ojos\n"
    menu += "K - Cantidad de heroes con cada color de pelo\nL - Cantidad de heroes con cada inteligencia\n"
    menu += "M - Color de ojos de cada heroe\nN - Color de pelo de cada heroe\nO - Inteligencia de cada heroe\n"
    menu += "Z - Salir\n\n"
    imprimir_dato(menu)

def stark_menu_principal_desafio_5():
    '''
    Imprime el menu de opciones y pide al usuario elegir una opcion. Valida que la letra ingresada sea correcta.

    En caso de ser correcta la letra ingresada la retorna, si es incorrecta retorna -1
    '''
    imprimir_menu_desafio_5()
    opcion = input("Seleccione una opcion: ")
    if re.search("^([A-HJ-OZa-hj-oz]{1})$", opcion):
        retorno = opcion
    else:
        retorno = "-1"
    
    return retorno

def stark_marvel_app_5(lista:list):
    '''
    Imprime el menu de opciones, pide al usuario elegir una opcion, valida que sea correcta y ejecuta la opcion seleccionada

    Recibe la lista de heroes
    '''
    while True:
        opcion = stark_menu_principal_desafio_5().upper()
        if opcion == "A":
            print("Heroes masculinos")
        elif opcion == "B":
            print("Heroes femeninos")
        elif opcion == "C":
            print("Heroe masculino mas alto")
        elif opcion == "D":
            print("Heroe femenino mas alto")
        elif opcion == "E":
            print("Heroe masculino mas bajo")
        elif opcion == "F":
            print("Heroe femenino mas bajo")
        elif opcion == "G":
            print("Promedio de altura de heroes masculinos")
        elif opcion == "H":
            print("Promedio de altura de heroes femeninos")
        elif opcion == "J":
            print("Cantidad de heroes con cada color de ojos")
        elif opcion == "K":
            print("Cantidad de heroes con cada color de pelo")
        elif opcion == "L":
            print("Cantidad de heroes con cada inteligencia")
        elif opcion == "M":
            print("Color de ojos de cada heroe")
        elif opcion == "N":
            print("Color de pelo de cada heroe")
        elif opcion == "O":
            print("Inteligencia de cada heroe")
        elif opcion == "Z":
            break
        else:
            print("Seleccione una opcion correcta")

def leer_archivo(path:str):
    '''
    Abre el archivo indicado en modo lectura

    Recibe un string que indicará el nombre y extensión del archivo a leer

    Retornará la lista de héroes como una lista de diccionarios.
    '''
    with open(path,"r") as archivo:
        buffer_dict = json.load(archivo)
    return buffer_dict["heroes"]

def guardar_archivo(nombre_archivo:str, contenido_guardar:str):
    '''
    Guarda en un archivo del nombre indicado, el string indicado en parametro

    Recibe el string del nombre de archivo y el string a guardar

    Devuelve True si no hubo errores o False en caso contrario
    '''
    try:
        with open(nombre_archivo,"w+") as archivo:
            archivo.write(contenido_guardar)
        retorno = True
        print("Se creó el archivo: {0}".format(nombre_archivo))
    except:
        retorno = False
        print("Error al crear el archivo: {0}".format(nombre_archivo))
    return retorno


def capitalizar_palabras(palabras:str):
    '''
    Capitaliza todas las palabras que recibe

    Recibe un string con una o mas palabras

    Devuelve las palabras capitalizadas
    '''
    capitalizadas = palabras.title()
    return capitalizadas

def obtener_nombre_capitalizado(heroe:dict):
    '''
    Formatea el nombre del heroe con todas las palabras capitalizadas

    Recibe el diccionario del heroe

    Retorna el nombre del heroe capitalizado
    '''
    nombre_capitalizado = capitalizar_palabras(heroe["nombre"])
    return nombre_capitalizado

def obtener_nombre_y_dato(heroe:dict, clave:str):
    '''
    Formatea el nombre del heroe y la clave recibida y lo devuelve en string

    Recibe el diccionario del heroe y un string que representara la clave del heroe a imprimir

    Devuelve un string que contenga el nombre del heroe y la clave
    '''
    nombre = obtener_nombre_capitalizado(heroe)
    clave_cap = capitalizar_palabras(clave)
    nombre_y_dato = "Nombre: {0} | {1}: {2}".format(nombre, clave_cap, heroe[clave])
    return nombre_y_dato

def es_genero(heroe:dict, genero_buscado:str):
    '''
    Evalua si el genero del heroe coincide con el genero buscado

    Recibe el diccionario del heroe y un string que representa el genero del heroe buscado (M, F o NB)

    Devuelve True si coincide, o False si no coincide
    '''
    genero_heroe = heroe["genero"]
    genero_buscado = genero_buscado.upper()
    if re.search("^(M|F|NB)$", genero_buscado):
        if genero_heroe == genero_buscado:
            retorno = True
        else:
            retorno = False
    else:
        retorno = "Genero buscado no valido"
    return retorno

def stark_guardar_heroe_genero(lista_heroes:list, genero_a_evaluar:str):
    '''
    Busca los heroes del genero a evaluar en la lista de heroes, imprime los heroes que coincidan
    y los guarda en un archivo .csv

    Recibe la lista de heroes y el genero buscado

    Devuelve True si pudo guardar el archivo o False caso contrario
    '''
    nombres_genero = ""
    for heroe in lista_heroes:
        if es_genero(heroe, genero_a_evaluar):
            nombre = obtener_nombre_capitalizado(heroe)
            imprimir_dato(nombre)
            nombres_genero += nombre + ","
    if guardar_archivo("heroes_{0}.csv".format(genero_a_evaluar), nombres_genero):
        retorno = True
    else:
        retorno = False
    return retorno
    
def calcular_min_genero(lista:list, clave:str, genero_buscado:str):
    '''
    Calcula el minimo de la clave recibida, del heroe del genero indicado ("M" o "F")

    Recibe una lista de diccionarios, la clave a utilizar para calcular, y el genero buscado

    Devuelve el diccionario que contiene el minimo de la clave indicada y el genero buscado
    '''
    stark_normalizar_datos(lista)
    flag_primer_genero = True
    if type(lista) == list and len(lista) > 0:
        genero_buscado = genero_buscado.upper()
        for heroe in lista:
            if flag_primer_genero == True and heroe["genero"] == genero_buscado:
                heroe_min = heroe
                flag_primer_genero = False
            elif heroe["genero"] == genero_buscado and heroe[clave] < heroe_min[clave]:
                heroe_min = heroe
        retorno = heroe_min
    
    return retorno

def calcular_max_genero(lista:list, clave:str, genero_buscado:str):
    '''
    Calcula el maximo de la clave recibida, del heroe del genero indicado ("M" o "F")

    Recibe una lista de diccionarios, la clave a utilizar para calcular, y el genero buscado

    Devuelve el diccionario que contiene el maximo de la clave indicada y el genero buscado
    '''
    stark_normalizar_datos(lista)
    flag_primer_genero = True
    if type(lista) == list and len(lista) > 0:
        genero_buscado = genero_buscado.upper()
        for heroe in lista:
            if flag_primer_genero == True and heroe["genero"] == genero_buscado:
                heroe_max = heroe
                flag_primer_genero = False
            elif heroe["genero"] == genero_buscado and heroe[clave] > heroe_max[clave]:
                heroe_max = heroe
        retorno = heroe_max
    
    return retorno

def calcular_max_min_dato_genero(lista:list, clave:str, genero_buscado:str, calculo:str):
    '''
    Calcula el max/min de la clave recibida, del heroe del genero indicado ("M" o "F")

    Recibe una lista de diccionarios, la clave a utilizar para calcular, el genero buscado y el
    calculo deseado (maximo o minimo)

    Devuelve el diccionario que contiene el maximo de la clave indicada y el genero buscado
    '''
    if calculo == "minimo":
        max_min = calcular_min_genero(lista, clave, genero_buscado)
    elif calculo == "maximo":
        max_min = calcular_max_genero(lista, clave, genero_buscado)
    return max_min

def stark_calcular_imprimir_guardar_heroe_genero(lista:list, clave:str, genero_buscado:str, calculo:str):
    '''
    Calcula el max/min de la clave recibida, del heroe del genero indicado ("M" o "F"), lo imprime
    en pantalla formateado y lo guarda en un archivo .csv

    Recibe una lista de diccionarios, la clave a utilizar para calcular, el genero buscado y el
    calculo deseado (maximo o minimo)

    Devuelve True si pudo guardar el archivo o False caso contrario
    '''
    str_heroes_calculo_clave_genero = ""
    max_min_heroe = calcular_max_min_dato_genero(lista, clave, genero_buscado, calculo)
    if calculo == "maximo":
        str_print = "Mayor {0}: ".format(clave)
    elif calculo == "minimo":
        str_print = "Menor {0}: ".format(clave)
    heroe_nombre_clave = str_print + obtener_nombre_y_dato(max_min_heroe, clave)
    imprimir_dato(heroe_nombre_clave)
    str_heroes_calculo_clave_genero += heroe_nombre_clave
    if guardar_archivo("heroes_{0}_{1}_{2}.csv".format(calculo, clave, genero_buscado), str_heroes_calculo_clave_genero):
        retorno = True
    else:
        retorno = False
    return retorno

def sumar_dato_heroe_genero(lista:list, clave:str, genero:str):
    '''
    Suma los datos de la clave recibida por parametro, de los heroes del genero indicado

    Recibe una lista de diccionarios, la clave a sumar y el genero buscado

    Devuelve la suma de todos los datos de la clave pasada por parametro, de los heroes del genero buscado
    '''
    stark_normalizar_datos(lista)
    suma_claves = 0
    for heroe in lista:
        if type(heroe) == dict and len(heroe) > 0 and heroe["genero"] == genero:
            suma_claves += heroe[clave]
    if suma_claves > 0:
        retorno = suma_claves
    else:
        retorno = -1
    return retorno

