import re
import json

def validar_respuesta(respuesta:str, validacion_regex:str):
    '''
    Valida la respuesta del usuario comparandola contra un patron regex indicado

    Recibe el string de la respuesta del usuario por input y el string del patron Regex contra el que comparar

    Devuelve el string respuesta en caso de coincidir o -1 si no es correcto
    '''
    if respuesta:
        if re.match(validacion_regex, respuesta):
            return respuesta
    return -1

def cargar_json(path:str) -> list:
    '''
    Extrae la lista de personajes del archivo json para lectura

    Recibe el string que representa el archivo a abrir

    Devuelve la lista de diccionarios
    '''
    with open (path, "r") as archivo:
        buffer_dict = json.load(archivo)
    return buffer_dict["results"]
    
def buscar_index_min(lista:list, clave:str) -> int:
    '''
    Busca la posicion en la que se encuentra el menor valor de la clave indicada

    Recibe la lista en la que buscar y la clave sobre la que buscar el menor valor

    Devuelve la posicion donde se encuentra el menor valor de la clave
    '''
    index_min = 0
    for i in range(len(lista)):
        if int(lista[i][clave]) < int(lista[index_min][clave]):
            index_min = i
    return index_min

def ordenar_lista(lista:list, clave:str) -> list:
    '''
    Ordena la lista recibida en orden ascendente segun el valor de la clave indicada

    Recibe la lista a ordenar y la clave mediante la cual ordenar

    Devuelve la lista ordenada
    '''
    lista_ordenada = lista.copy()
    for i in range(len(lista_ordenada)):
        index_minmax = buscar_index_min(lista_ordenada[i:], clave) + i
        lista_ordenada[i],lista_ordenada[index_minmax] = lista_ordenada[index_minmax],lista_ordenada[i]
    return lista_ordenada

def mostrar_lista(lista:list, clave:str="height") -> None:
    '''
    Imprime formateados con el Nombre del personaje y la clave indicada los personajes de la lista recibida

    Recibe la lista a imprimir y la clave a imprimir
    '''
    print("")
    for pers in lista:
        print("Nombre: {0} - {1}: {2}".format(pers["name"], clave.capitalize(), pers[clave]))
    print("")

def mostrar_personaje_mas_alto_genero(lista:list) -> None:
    '''
    Imprime en pantalla el personaje mas alto de cada genero

    Recibe la lista de personajes
    '''
    flag_female = True
    flag_male = True
    flag_na = True
    for pers in lista:
        if pers["gender"] == "male" and (flag_male == True or int(pers["height"]) > int(alto_male["height"])):
            alto_male = pers
            flag_male = False
        elif pers["gender"] == "female" and (flag_female == True or int(pers["height"]) > int(alto_female["height"])):
            alto_female = pers
            flag_female = False
        elif pers["gender"] == "n/a" and (flag_na == True or int(pers["height"]) > int(alto_na["height"])):
            alto_na = pers
            flag_na = False
    print("Personaje masculino mas alto: {0}, Altura: {1}".format(alto_male["name"], alto_male["height"]))
    print("Personaje femenino mas alto: {0}, Altura: {1}".format(alto_female["name"], alto_female["height"]))
    print("Personaje sin genero mas alto: {0}, Altura: {1}".format(alto_na["name"], alto_na["height"]))
    print("")

def buscador_personajes(lista:list, busqueda:str) -> None:
    '''
    Busca en la lista por nombre de personaje, segun la busqueda del usuario

    Recibe la lista de personajes y el str de busqueda del usuario
    '''
    patron = busqueda.capitalize()
    for pers in lista:
        if re.search(patron, pers["name"]):
            print("Nombre: {0}, Altura: {1}, Peso: {2}, Genero: {3}\n".format(pers["name"],pers["height"],pers["mass"],pers["gender"]))

def exportar_csv(lista:list):
    '''
    Exporta a archivo csv la lista de personajes

    Recibe la lista de personajes a exportar
    '''
    contenido_guardar = ""
    for pers in lista:
        contenido_guardar += "Nombre: {0}, Altura: {1}, Peso: {2}, Genero: {3}\n".format(pers["name"],pers["height"],pers["mass"],pers["gender"])
    try:
        with open ("Lista_personajes.csv", "w") as archivo:
            archivo.write(contenido_guardar)
        print("Archivo .csv creado correctamente")
    except:
        print("Error, archivo no creado")