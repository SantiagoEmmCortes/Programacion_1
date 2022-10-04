'''
{
			"id": 1,
			"nombre": "bulbasaur",
            "tipo": ["planta"],
            "evoluciones": ["ivysaur", "venusaur"],
			"poder": 4,
			"fortaleza":["agua"],
			"debilidad":["fuego"]
		},
'''

import pokemon_func as poke

def simulacro():
	'''
	
	'''
	lista_pokemones = poke.cargar_json("Simulacro_Parcial_2/pokedex.json")
	lista_para_csv = []
	opcion_anterior = ""
	while True:
		print("1 - Listar los ultimos N Pokemones\n2 - Ordenar y listar pokemones por poder (asc/desc)\n"
			"3 - Ordenar y listar pokemones por ID (asc/desc)\n"
			"4 - Calcular la cantidad promedio de las key tipo lista y listar los que superen o no el promedio(mayor/menor)\n"
			"5 - Buscar y listar pokemones por tipo\n"
			"6 - Exportar lista de héroes a CSV ordenados segun opcion elegida anteriormente\n7 - Salir\n")
		opcion = input("Seleccione opcion: ")
		opcion = poke.validar_respuesta(opcion, "^[1-7]{1}$")
		if opcion == "1":
			cantidad = input("Cantidad de pokemones a imprimir: ")
			cantidad_pokemones = poke.validar_respuesta(cantidad, "^[0-9]{1,2}$")
			cantidad_pokemones = poke.validar_largo_lista(lista_pokemones, cantidad_pokemones)
			lista_para_csv = lista_pokemones[(len(lista_pokemones)-cantidad_pokemones):].copy()
			poke.mostrar_lista(lista_para_csv)
			opcion_anterior = opcion
			clave_anterior = "tipo"
		elif opcion == "2":
			respuesta = input("Seleccione orden ascendente(asc) o descendente(desc): ").lower()
			orden = poke.validar_respuesta(respuesta, "^(asc|desc)$")
			if orden == -1:
				print("Opcion invalida, ordenando automaticamente de manera ascendente")
				orden = "asc"
			lista_para_csv = poke.ordenar_lista(lista_pokemones, "poder", orden)
			poke.mostrar_lista(lista_para_csv, "poder")
			opcion_anterior = opcion
			clave_anterior = "poder"
		elif opcion == "3":
			respuesta = input("Seleccione orden ascendente(asc) o descendente(desc): ").lower()
			orden = poke.validar_respuesta(respuesta, "^(asc|desc)$")
			if orden == -1:
				print("Opcion invalida, ordenando automaticamente de manera ascendente")
				orden = "asc"
			lista_para_csv = poke.ordenar_lista(lista_pokemones, "id", orden)
			poke.mostrar_lista(lista_para_csv, "id")
			opcion_anterior = opcion
			clave_anterior = "id"
		elif opcion == "4":
			respuesta = input("Ingrese clave a promediar: (evoluciones, fortaleza, debilidad, tipo): ").lower()
			clave = poke.validar_respuesta(respuesta, "^(evoluciones|fortaleza|debilidad|tipo)$")
			if clave == -1:
				print("Clave ingresada invalida, clave utilizada: tipo")
				clave = "tipo"
			mayor_menor = poke.validar_respuesta(input("Imprimir mayor o menor al promedio: ").lower(), "^(mayor|menor)$")
			if mayor_menor == -1:
				print("Seleccion invalida, imprimiendo mayores al promedio")
				mayor_menor = "mayor"
			lista_para_csv = poke.mostrar_mayor_menor_promedio(lista_pokemones, clave, mayor_menor)
			poke.mostrar_lista(lista_para_csv, clave)
			opcion_anterior = opcion
			clave_anterior = clave
		elif opcion == "5":
			respuesta = input("Seleccione tipo a buscar (planta, fuego, volador, agua, electrico, fantasma, veneno, hielo, psiquico, lucha, acero): ").lower()
			tipo = poke.validar_respuesta(respuesta, "^(planta|fuego|volador|agua|electrico|fantasma|veneno|hielo|psiquico|lucha|acero)$")
			if tipo == -1:
				print("Tipo ingresado invalido, tipo utilizado: fuego")
				tipo = "fuego"
			poke.listar_pokemon_por_tipo(lista_pokemones, tipo)
		elif opcion == "6":
			if opcion_anterior == "":
				print("Debe ingresar opcion entre 1 y 4 antes de exportar lista a csv\n")
			else:
				poke.exportar_csv(lista_para_csv, opcion_anterior, clave_anterior)
		elif opcion == "7":
			print("Fin del programa")
			break

simulacro()