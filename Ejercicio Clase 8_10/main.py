'''
{
    "nombre": "Howard the Duck",
    "identidad": "Howard (Last name unrevealed)",
    "empresa": "Marvel Comics",
    "altura": "79.349999999999994",
    "peso": "18.449999999999999",
    "genero": "M",
    "color_ojos": "Brown",
    "color_pelo": "Yellow",
    "fuerza": "2",
    "inteligencia": ""
}
'''
from func import *


def stark_app():
    lista_heroes = leer_archivo("Ejercicio Clase 8_10\data_stark.json")
    sumar_dato_heroe_genero(lista_heroes, "peso", "F")
    #stark_marvel_app_5(lista_heroes)

stark_app()