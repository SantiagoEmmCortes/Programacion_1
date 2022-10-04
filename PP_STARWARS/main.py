'''
1 - Listar los personajes ordenados por altura
2 - Mostrar el personaje mas alto de cada genero
3 - Ordenar los personajes por peso
4 - Armar un buscador de personajes 
5 - Exportar lista personajes a CSV
6 - Salir

'''
import funciones

def starwars_app():
    lista_personajes = funciones.cargar_json("PP_STARWARS\data.json")
    while(True):
        print("1 - Listar los personajes ordenados por altura\n2 - Mostrar el personaje mas alto de cada genero\n3 - Ordenar los personajes por peso\n4 - Armar un buscador de personajes\n5 - Exportar lista personajes a CSV\n6 - Salir\n")
        respuesta = input("Seleccione opcion: ")
        respuesta = funciones.validar_respuesta(respuesta, "^[1-6]{1}$")
        if(respuesta=="1"):
            lista_ordenada = funciones.ordenar_lista(lista_personajes, "height")
            funciones.mostrar_lista(lista_ordenada, "height")
        elif(respuesta=="2"):
            funciones.mostrar_personaje_mas_alto_genero(lista_personajes)
        elif(respuesta=="3"):
            lista_ordenada = funciones.ordenar_lista(lista_personajes, "mass")
            funciones.mostrar_lista(lista_ordenada, "mass")
        elif(respuesta=="4"):
            busqueda = input("Ingrese personaje a buscar: ").capitalize()
            funciones.buscador_personajes(lista_personajes, busqueda)
        elif(respuesta=="5"):
            funciones.exportar_csv(lista_personajes)
        elif(respuesta=="6"):
            break

starwars_app()

