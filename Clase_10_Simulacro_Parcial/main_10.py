'''
{
    "nombre": "Howard the Duck",
    "identidad": "Howard (Last name unrevealed)",
    "altura": 79.35,
    "peso": 18.45,
    "fuerza": 2,
    "inteligencia": ""
}
'''
from func_10 import *

def parcial():
    lista_heroes = leer_json("Clase_10_Simulacro_Parcial/data_stark.json")
    lista_para_csv = []
    while True:
        print("1 - Listar los primeros N héroes\n2 - Ordenar y Listar héroes por altura (asc/desc)\n"
            "3 - Ordenar y Listar héroes por fuerza (asc/desc)\n"
            "4 - Calcular promedio de clave numerica y ordenar en forma ascendente los que superen o no el promedio\n"
            "5 - Buscar y listar héroes por inteligencia\n"
            "6 - Exportar lista de héroes a CSV ordenados segun opcion elegida anteriormente\n7 - Salir")
        opcion = input("Seleccione opcion: ")
        opcion = validar_respuesta(opcion, "^[1-7]{1}$")
        opcion_anterior = ""
        if opcion == "1":
            cantidad = input("Cantidad de heroes a mostrar: ")
            cantidad_heroes = validar_respuesta(cantidad, "^[0-9]{1,2}$")
            cantidad_heroes = validar_largo_lista(lista_heroes, cantidad_heroes)
            lista_para_csv = lista_heroes[:cantidad_heroes].copy()
            mostrar_lista_clave(lista_para_csv)
            opcion_anterior = opcion
            clave_anterior = "fuerza"
        elif opcion == "2":
            orden = validar_respuesta(input("Ordenar de manera ascendente(asc) o descendente(desc): ").lower(), "^(asc|desc)$")
            if orden == -1:
                orden = "asc"
                print("Orden invalido, ordenados automaticamente de manera ascendente")
            lista_para_csv = ordenar_clave_asc_desc(lista_heroes, "altura", orden)
            mostrar_lista_clave(lista_para_csv, "altura")
            opcion_anterior = opcion
            clave_anterior = "altura"
        elif opcion == "3":
            orden = validar_respuesta(input("Ordenar de manera ascendente(asc) o descendente(desc): ").lower(), "^(asc|desc)$")
            if orden == -1:
                orden = "asc"
                print("Orden invalido, ordenados automaticamente de manera ascendente")
            lista_para_csv = ordenar_clave_asc_desc(lista_heroes, "fuerza", orden)
            mostrar_lista_clave(lista_para_csv, "fuerza")
            opcion_anterior = opcion
            clave_anterior = "fuerza"
        elif opcion == "4":
            clave = validar_respuesta(input("Clave numerica (altura, peso, fuerza): ").lower(), "^(altura|peso|fuerza)$")
            if clave == -1:
                clave = "fuerza"
                print("Clave invalida, clave utilizada: fuerza")
            mayor_menor = validar_respuesta(input("Imprimir mayor o menor al promedio: ").lower(), "^(mayor|menor)$")
            if mayor_menor == -1:
                mayor_menor = "mayor"
                print("Seleccion invalida, imprimiendo mayores al promedio")
            lista_para_csv = mostrar_mayor_menor_promedio(lista_heroes, clave, mayor_menor)
            mostrar_lista_clave(lista_para_csv, clave)
            opcion_anterior = opcion
            clave_anterior = clave
        elif opcion == "5":
            inteligencia = validar_respuesta(input("Inteligencia (good, average, high): ").lower(), "^(good|average|high)$")
            if inteligencia == -1:
                inteligencia = "average"
                print("Seleccion invalida, inteligencia buscada: 'average'")
            listar_heroes_inteligencia(lista_heroes, inteligencia)
        elif opcion == "6":
            if opcion_anterior == "":
                print("Debe ingresar opcion entre 1 y 4 antes de exportar lista a csv\n")
            else:
                exportar_csv(opcion_anterior, lista_para_csv, clave_anterior)
        elif opcion == "7":
            print("Fin del programa")
            break

parcial()