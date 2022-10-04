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
    
    '''
    with open(path,"r") as archivo:
        buffer_dict = json.load(archivo)
    return buffer_dict["pokemones"]

def mostrar_lista(lista:list, clave:str = "tipo"):
    '''
    
    '''
    if lista and type(lista) == list and type(clave) == str:
        print("")
        for pokemon in lista:
            if clave in pokemon.keys():
                print("ID: {0} - Nombre: {1} - {2}: {3}".format(pokemon["id"], pokemon["nombre"], clave.capitalize(), pokemon[clave]))
        print("")
    else:
        print("Error, lista o clave incorrectas")

def validar_largo_lista(lista:list, largo:str) -> int:
    '''
    
    '''
    if lista and type(lista) == list:
        largo = int(largo)
        if largo > 0 and largo <= len(lista):
            return largo
    print("Cantidad invalida, cantidad de pokemones en la lista: {0}".format(len(lista)))
    return len(lista)

def buscar_min_max(lista:list, clave:str, orden:str) -> int:
    '''
    
    '''
    if lista and type(lista) == list:
        index_min_max = 0
        for i in range(len(lista)):
            if orden == "asc" and lista[i][clave] < lista[index_min_max][clave] or orden == "desc" and lista[i][clave] > lista[index_min_max][clave]:
                index_min_max = i
        return index_min_max
    else:
        return -1

def ordenar_lista(lista:list, clave:str, orden:str="asc") -> list:
    '''
    
    '''
    lista_ordenada = lista.copy()
    for i in range(len(lista_ordenada)):
        index_min_max = buscar_min_max(lista_ordenada[i:], clave, orden) + i
        lista_ordenada[i],lista_ordenada[index_min_max] = lista_ordenada[index_min_max],lista_ordenada[i]
    return lista_ordenada

def calcular_promedio(lista:list, clave:str) -> int:
    '''
    
    '''
    if lista and type(lista) == list:
        suma_len = 0
        for pokemon in lista:
            if type(pokemon[clave]) == list:
                suma_len += len(pokemon[clave])
        promedio = suma_len / len(lista)
        return promedio
    else:
        return -1
    
def mostrar_mayor_menor_promedio(lista:list, clave:str, mayor_menor:str):
    '''
    
    '''
    lista = ordenar_lista(lista, "id")
    lista_mayor_menor = []
    promedio = calcular_promedio(lista, clave)
    print("Promedio de {0}: {1:.2f}".format(clave, promedio))
    for pokemon in lista:
        if mayor_menor == "mayor" and type(pokemon[clave] == list):
            if len(pokemon[clave]) >= promedio:
                lista_mayor_menor.append(pokemon)
        elif mayor_menor == "menor" and type(pokemon[clave] == list):
            if len(pokemon[clave]) < promedio and len(pokemon[clave]) != 0:
                lista_mayor_menor.append(pokemon)
    return lista_mayor_menor

def listar_pokemon_por_tipo(lista:list, tipo:str):
    '''
    
    '''
    lista = ordenar_lista(lista, "id")
    if lista and type(lista) == list:
        lista_tipo = []
        for pokemon in lista:
            for tipos in pokemon["tipo"]:
                if re.search(tipo, tipos):
                    lista_tipo.append(pokemon)
        mostrar_lista(lista_tipo, "tipo")
    else:
        print("Error, lista vacia")

def exportar_csv(lista:list, opcion:str, clave:str):
    '''
    
    '''
    nombre_archivo = "lista_{0}.csv".format(opcion)
    contenido_guardar = ""
    for pokemon in lista:
        contenido_guardar += "ID: {0} - Nombre: {1} - {2}: {3},".format(pokemon["id"], pokemon["nombre"], clave.capitalize(), pokemon[clave])
    try:
        with open (nombre_archivo, "w+") as archivo:
            archivo.write(contenido_guardar)
        print("Se creó el archivo: {0}".format(nombre_archivo))
    except:
        print("Error al crear el archivo: {0}".format(nombre_archivo))
