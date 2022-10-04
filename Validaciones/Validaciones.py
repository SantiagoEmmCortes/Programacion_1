import re

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