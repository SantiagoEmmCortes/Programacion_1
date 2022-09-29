from data_stark import lista_heroes

#   {
#     "nombre": "Howard the Duck",
#     "identidad": "Howard (Last name unrevealed)",
#     "empresa": "Marvel Comics",
#     "altura": "79.349999999999994",
#     "peso": "18.449999999999999",
#     "genero": "M",
#     "color_ojos": "Brown",
#     "color_pelo": "Yellow",
#     "fuerza": "2",
#     "inteligencia": ""
#   },

#Puntos B y C
def informar_heroe_y_altura():
    for heroe in lista_heroes:
        print("Nombre: {0}, Altura: {1:.2f}".format(heroe["nombre"], float(heroe["altura"])))
    
#Heroe mas alto
def informar_heroe_mas_alto():
    heroe_mas_alto = lista_heroes[0]
    for heroe in lista_heroes:
        if float(heroe["altura"]) > float(heroe_mas_alto["altura"]):
            heroe_mas_alto = heroe
        
    print("Heroe mas alto: {0}, con altura: {1:.2f}".format(heroe_mas_alto["nombre"],float(heroe_mas_alto["altura"])))

#Heroe mas bajo
def informar_heroe_mas_bajo():
    heroe_mas_bajo = lista_heroes[0]
    for heroe in lista_heroes:
        if float(heroe["altura"]) < float(heroe_mas_bajo["altura"]):
            heroe_mas_bajo = heroe
        
    print("Heroe mas bajo: {0}, con altura: {1:.2f}".format(heroe_mas_bajo["nombre"],float(heroe_mas_bajo["altura"])))

#Altura promedio de heroes
def informar_promedio_altura():
    acumulador_altura = 0
    for heroe in lista_heroes:
        acumulador_altura += float(heroe["altura"])
        altura_promedio = acumulador_altura / len(lista_heroes)

    print("Altura promedio de los superheroes: {0:.2f}".format(altura_promedio))

#Heroe mas pesado
def informar_heroe_mas_pesado():
    heroe_mas_pesado = lista_heroes[0]
    for heroe in lista_heroes:
        if float(heroe["peso"]) > float(heroe_mas_pesado["peso"]):
            heroe_mas_pesado = heroe

    print("Heroe mas pesado: {0}, con peso: {1:.2f}".format(heroe_mas_pesado["nombre"],float(heroe_mas_pesado["peso"])))

#Heroe menos pesado
def informar_heroe_menos_pesado():
    heroe_menos_pesado = lista_heroes[0]
    for heroe in lista_heroes:
        if float(heroe["peso"]) < float(heroe_menos_pesado["peso"]):
            heroe_menos_pesado = heroe
        
    print("Heroe menos pesado: {0}, con peso: {1:.2f}".format(heroe_menos_pesado["nombre"],float(heroe_menos_pesado["peso"])))

while(True):
    opcion = input("\nSeleccione opcion:\n1 - Lista de heroes con altura\n2 - Heroe mas alto\n3 - Heroe mas bajo\n"
                "4 - Promedio de altura de heroes\n5 - Heroe mas pesado\n6 - Heroe menos pesado\n7 - Salir\n\n")
    if opcion == '1':
        informar_heroe_y_altura()
    elif opcion == '2':
        informar_heroe_mas_alto()
    elif opcion == '3':
        informar_heroe_mas_bajo()
    elif opcion == '4':
        informar_promedio_altura()
    elif opcion == '5':
        informar_heroe_mas_pesado()
    elif opcion == '6':
        informar_heroe_menos_pesado()
    elif opcion == '7':
        break
    else:
        print("Ingrese opcion valida")