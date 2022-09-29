import json
import re

def leer_json(path:str) -> list:
    '''
    Abre el archivo json indicado en modo lectura

    Recibe un string que indicará el nombre y extensión del archivo a leer

    Retornará la lista de héroes como una lista de diccionarios.
    '''
    with open(path,"r") as archivo:
        buffer_dict = json.load(archivo)
    return buffer_dict["heroes"]

def mostrar_lista_clave(lista:list, clave:str = "fuerza"):
    '''
    Itera la lista de heroes e imprime en pantalla los heroes formateados con su Nombre, identidad y la clave indicada

    Recibe la lista de heroes y la clave a utilizar
    '''
    if lista and type(lista) == list and type(clave) == str:
        print("")
        for heroe in lista:
            if clave in heroe.keys():
                print("Nombre: {0} - Identidad: {1} - {2}: {3}".format(heroe["nombre"], heroe["identidad"], clave.capitalize(), heroe[clave]))
        print("")

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

def validar_largo_lista(lista:list, largo:str) -> int:
    '''
    Valida que el largo de lista indicado por el usuario sea mayor a cero y no supere el largo maximo de la lista

    Recibe la lista de heroes y el string que indica el largo de lista deseado

    Devuelve un entero, del largo buscado por el usuario si es correcto o el largo maximo de lista en caso de ser incorrecto
    '''
    if lista:
        largo = int(largo)
        if largo > 0 and largo <= len(lista):
            return largo
    print("Cantidad invalida, hay {0} heroes: ".format(len(lista)))
    return len(lista)

def buscar_min_max(lista:list, clave:str, orden: str) -> int:
    '''
    Busca la posicion de un minimo o maximo de una clave numerica en una lista

    Recibe la lista de heroes en la que buscar, la clave numerica a evaluar y el orden deseado ('asc' o 'desc')

    Devuelve la posicion en que se encuentra el min/max o -1 si la lista se encuentra vacia
    '''
    if lista:
        index_min_max = 0
        for i in range(len(lista)):
            if orden == "asc" and lista[i][clave] < lista[index_min_max][clave] or orden == "desc" and lista[i][clave] > lista[index_min_max][clave]:
                index_min_max = i
        return index_min_max
    return -1

def ordenar_clave_asc_desc(lista:list, clave:str, orden:str="asc") -> list:
    '''
    Ordena la lista recibida, por la clave numerica recibida, de forma ascendente (asc) o descendente (desc)

    Recibe la lista a ordenar, la clave numerica a utilizar para ordenar y el orden deseado

    Devuelve la lista ordenada
    '''
    lista_ordenada = lista.copy()
    for i in range(len(lista_ordenada)):
        index_min_max = buscar_min_max(lista_ordenada[i:], clave, orden) + i
        lista_ordenada[i],lista_ordenada[index_min_max] =\
         lista_ordenada[index_min_max],lista_ordenada[i]
    return lista_ordenada

def calcular_promedio_clave(lista:list, clave:str) -> int:
    '''
    Calcula el promedio de la clave numerica en la lista de heroes

    Recibe la lista de heroes y la clave a calcular
    
    Devuelve el promedio
    '''
    if lista and type(lista) == list:
        suma_claves = 0
        for heroe in lista:
            if type(heroe[clave]) == float or type(heroe[clave]) == int:
                suma_claves += heroe[clave]
        promedio_clave = suma_claves / len(lista)
        return promedio_clave
    return -1

def mostrar_mayor_menor_promedio(lista:list, clave:str, mayor_menor:str) -> list:
    '''
    Calcula el promedio de una clave numerica en la lista de heroes, y guarda en una lista en orden ascendente los heroes
    mayores o menores al promedio

    Recibe la lista de heroes, la clave a calcular y un string que representa si guardar los mayores o menores

    Devuelve la lista con los heroes mayor/menor al promedio
    '''
    lista_ordenada = ordenar_clave_asc_desc(lista, clave)
    lista_mayor_menor = []
    promedio = calcular_promedio_clave(lista, clave)
    print("Promedio: {0:.2f}".format(promedio))
    for heroe in lista_ordenada:
        if mayor_menor == "mayor":
            if heroe[clave] > promedio:
                lista_mayor_menor.append(heroe)
        elif mayor_menor == "menor":
            if heroe[clave] < promedio:
                lista_mayor_menor.append(heroe)
    return lista_mayor_menor

def listar_heroes_inteligencia(lista:list, inteligencia:str):
    '''
    Imprime en pantalla los heroes con inteligencia igual a la buscada por el usuario

    Recibe la lista de heroes y un string con la inteligencia buscada
    '''
    if lista and type(lista) == list:
        lista_inteligencia = []
        for heroe in lista:
            if heroe["inteligencia"] == inteligencia:
                lista_inteligencia.append(heroe)
        mostrar_lista_clave(lista_inteligencia, "inteligencia")
    else:
        print("Error, lista de heroes vacia")

def exportar_csv(opcion:str, lista_guardar:list, clave:str="fuerza"):
    '''
    Guarda en archivo.csv la lista de heroes ordenada previamente con el numero de opcion seleccionada como nombre de archivo

    Recibe un string que representa la opcion elegida anteriormente por el usuario, la lista ordenada a exportar y la clave
    utilizada para ordenar la lista
    '''
    nombre_archivo = "lista_{0}.csv".format(opcion)
    contenido_guardar = ""
    for heroe in lista_guardar:
        contenido_guardar += "Nombre: {0} - Identidad: {1} - {2}: {3},".format(heroe["nombre"], heroe["identidad"], clave.capitalize(), heroe[clave])
    try:
        with open(nombre_archivo,"w+") as archivo:
            archivo.write(contenido_guardar)
        print("Se creó el archivo: {0}".format(nombre_archivo))
    except:
        print("Error al crear el archivo: {0}".format(nombre_archivo))