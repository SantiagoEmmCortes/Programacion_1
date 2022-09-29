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

def informar_heroe_y_altura():
    for heroe in lista_heroes:
        print("Nombre: {0}, Altura: {1:.2f}".format(heroe["nombre"], float(heroe["altura"])))
    
def informar_heroe_mas_alto():
    heroe_mas_alto = lista_heroes[0]
    for heroe in lista_heroes:
        if float(heroe["altura"]) > float(heroe_mas_alto["altura"]):
            heroe_mas_alto = heroe
        
    print("Heroe mas alto: {0}, con altura: {1:.2f}".format(heroe_mas_alto["nombre"],float(heroe_mas_alto["altura"])))

def informar_heroe_mas_bajo():
    heroe_mas_bajo = lista_heroes[0]
    for heroe in lista_heroes:
        if float(heroe["altura"]) < float(heroe_mas_bajo["altura"]):
            heroe_mas_bajo = heroe
        
    print("Heroe mas bajo: {0}, con altura: {1:.2f}".format(heroe_mas_bajo["nombre"],float(heroe_mas_bajo["altura"])))

def informar_promedio_altura():
    acumulador_altura = 0
    for heroe in lista_heroes:
        acumulador_altura += float(heroe["altura"])
        altura_promedio = acumulador_altura / len(lista_heroes)

    print("Altura promedio de los superheroes: {0:.2f}".format(altura_promedio))

def informar_heroe_mas_pesado():
    heroe_mas_pesado = lista_heroes[0]
    for heroe in lista_heroes:
        if float(heroe["peso"]) > float(heroe_mas_pesado["peso"]):
            heroe_mas_pesado = heroe

    print("Heroe mas pesado: {0}, con peso: {1:.2f}".format(heroe_mas_pesado["nombre"],float(heroe_mas_pesado["peso"])))

def informar_heroe_menos_pesado():
    heroe_menos_pesado = lista_heroes[0]
    for heroe in lista_heroes:
        if float(heroe["peso"]) < float(heroe_menos_pesado["peso"]):
            heroe_menos_pesado = heroe
        
    print("Heroe menos pesado: {0}, con peso: {1:.2f}".format(heroe_menos_pesado["nombre"],float(heroe_menos_pesado["peso"])))

def informar_heroes_genero_M():
    for heroe in lista_heroes:
        if heroe["genero"] == 'M':
            print("Nombre: {0}".format(heroe["nombre"]))

def informar_heroes_genero_F():
    for heroe in lista_heroes:
        if heroe["genero"] == 'F':
            print("Nombre: {0}".format(heroe["nombre"]))

def informar_heroe_mas_alto_genero_M():
    heroe_mas_alto_M = lista_heroes[0]
    for heroe in lista_heroes:
        if heroe["genero"] == 'M':
            if float(heroe["altura"]) > float(heroe_mas_alto_M["altura"]):
                heroe_mas_alto_M = heroe
        
    print("Heroe mas alto masculino: {0}, con altura: {1:.2f}".format(heroe_mas_alto_M["nombre"],float(heroe_mas_alto_M["altura"])))

def informar_heroe_mas_alto_genero_F():
    heroe_mas_alto_F = lista_heroes[0]
    for heroe in lista_heroes:
        if heroe["genero"] == 'F':
            if float(heroe["altura"]) > float(heroe_mas_alto_F["altura"]):
                heroe_mas_alto_F = heroe
        
    print("Heroe mas alto femenino: {0}, con altura: {1:.2f}".format(heroe_mas_alto_F["nombre"],float(heroe_mas_alto_F["altura"])))

def informar_heroe_mas_bajo_genero_M():
    heroe_mas_bajo_M = lista_heroes[0]
    for heroe in lista_heroes:
        if heroe["genero"] == 'M':
            if float(heroe["altura"]) < float(heroe_mas_bajo_M["altura"]):
                heroe_mas_bajo_M = heroe
        
    print("Heroe mas bajo masculino: {0}, con altura: {1:.2f}".format(heroe_mas_bajo_M["nombre"],float(heroe_mas_bajo_M["altura"])))

def informar_heroe_mas_bajo_genero_F():
    flag_primer_femenino = True
    for heroe in lista_heroes:
        if (heroe["genero"] == 'F' and flag_primer_femenino == True):
            heroe_mas_bajo_F = heroe
            flag_primer_femenino = False
        elif (heroe["genero"] == 'F'):
            if float(heroe["altura"]) < float(heroe_mas_bajo_F["altura"]):
                heroe_mas_bajo_F = heroe
        
    print("Heroe mas bajo femenino: {0}, con altura: {1:.2f}".format(heroe_mas_bajo_F["nombre"],float(heroe_mas_bajo_F["altura"])))

def informar_promedio_altura_genero_M():
    acumulador_altura_M = 0
    contador_heroes_M = 0
    for heroe in lista_heroes:
        if heroe["genero"] == 'M':
            contador_heroes_M += 1
            acumulador_altura_M += float(heroe["altura"])

    if contador_heroes_M == 0:
        print("No hay heroes de genero 'M'")
    else:
        altura_promedio_M = acumulador_altura_M / contador_heroes_M

    print("Altura promedio de los superheroes masculinos: {0:.2f}".format(altura_promedio_M))

def informar_promedio_altura_genero_F():
    acumulador_altura_F = 0
    contador_heroes_F = 0
    for heroe in lista_heroes:
        if heroe["genero"] == 'F':
            contador_heroes_F += 1
            acumulador_altura_F += float(heroe["altura"])

    if contador_heroes_F == 0:
        print("No hay heroes de genero 'F'")
    else:
        altura_promedio_F = acumulador_altura_F / contador_heroes_F

    print("Altura promedio de los superheroes femeninos: {0:.2f}".format(altura_promedio_F))

def informar_cantidad_color_de_ojos():
    # lista_color_ojos = []
    # for heroe in lista_heroes:
    #     lista_color_ojos.append(heroe["color_ojos"])
    # lista_color_ojos = set(lista_color_ojos)
    # lista_color_ojos = list(lista_color_ojos)

    # for color in lista_color_ojos:
    #     cantidad_heroes = 0
    #     for heroe in lista_heroes:
    #         if heroe["color_ojos"] == color:
    #             cantidad_heroes += 1
    #     print("Cantidad de heroes con color de ojos {0}: {1}".format(color,cantidad_heroes))

    dict_ojos = {}

    for heroe in lista_heroes:
        color_ojos = heroe["color_ojos"]
        if color_ojos not in dict_ojos.keys():
            dict_ojos[color_ojos] = 1
        else:
            dict_ojos[color_ojos] += 1

    for color_cantidad in dict_ojos.items():
        print("Cantidad de heroes con color de ojos {0}: {1}".format(color_cantidad[0],color_cantidad[1]))

def informar_cantidad_color_de_pelo():
    dict_pelos = {}

    for heroe in lista_heroes:
        color_pelo = heroe["color_pelo"]
        if color_pelo not in dict_pelos.keys():
            dict_pelos[color_pelo] = 1
        else:
            dict_pelos[color_pelo] += 1

    for color_cantidad in dict_pelos.items():
        print("Cantidad de heroes con color de pelo {0}: {1}".format(color_cantidad[0],color_cantidad[1]))

def informar_cantidad_inteligencias():
    dict_inteligencia = {}

    for heroe in lista_heroes:
        inteligencia = heroe["inteligencia"]
        if inteligencia not in dict_inteligencia.keys():
            if inteligencia == '':
                dict_inteligencia["No tiene"] = 1
            else:
                dict_inteligencia[inteligencia] = 1
        else:
            dict_inteligencia[inteligencia] += 1

    for inteligencia_cantidad in dict_inteligencia.items():
        print("Cantidad de heroes con inteligencia {0}: {1}".format(inteligencia_cantidad[0],inteligencia_cantidad[1]))

def informar_color_de_ojos_heroes():
    lista_color_ojos = []
    for heroe in lista_heroes:
        lista_color_ojos.append(heroe["color_ojos"])
    lista_color_ojos = set(lista_color_ojos)
    lista_color_ojos = list(lista_color_ojos)

    for color in lista_color_ojos:
        lista_heroes_ojos = []
        for heroe in lista_heroes:
            if heroe["color_ojos"] == color:
                lista_heroes_ojos.append(heroe["nombre"])
        print("Color de ojos: {0} | Heroes: {1}".format(color, lista_heroes_ojos))

def informar_color_de_pelo_heroes():
    lista_color_pelo = []
    for heroe in lista_heroes:
        lista_color_pelo.append(heroe["color_pelo"])
    lista_color_pelo = set(lista_color_pelo)
    lista_color_pelo = list(lista_color_pelo)

    for color in lista_color_pelo:
        lista_heroes_pelo = []
        for heroe in lista_heroes:
            if heroe["color_pelo"] == color:
                lista_heroes_pelo.append(heroe["nombre"])
        print("Color de pelo: {0} | Heroes: {1}".format(color, lista_heroes_pelo))

def informar_inteligencia_heroes():
    lista_inteligencias = []
    for heroe in lista_heroes:
        lista_inteligencias.append(heroe["inteligencia"])
    lista_inteligencias = set(lista_inteligencias)
    lista_inteligencias = list(lista_inteligencias)

    for inteligencia in lista_inteligencias:
        lista_heroes_inteligencia = []
        for heroe in lista_heroes:
            if heroe["inteligencia"] == inteligencia:
                lista_heroes_inteligencia.append(heroe["nombre"])
        print("Inteligencia: {0} | Heroes: {1}".format(inteligencia, lista_heroes_inteligencia))

while(True):
    opcion = input("\nSeleccione opcion:\n1  - Lista de heroes con altura\n2  - Heroe mas alto\n3  - Heroe mas bajo\n"
                "4  - Promedio de altura de heroes\n5  - Heroe mas pesado\n6  - Heroe menos pesado\n"
                "7  - Heroes masculinos\n8  - Heroes femeninos\n9  - Heroe masculino mas alto\n"
                "10 - Heroe femenino mas alto\n11 - Heroe masculino mas bajo\n12 - Heroe femenino mas bajo\n"
                "13 - Promedio de altura de heroes masculinos\n14 - Promedio de altura de heroes femeninos\n"
                "15 - Cantidad de heroes con cada color de ojos\n16 - Cantidad de heroes con cada color de pelo\n"
                "17 - Cantidad de heroes con cada inteligencia\n18 - Color de ojos de cada heroe\n"
                "19 - Color de pelo de cada heroe\n20 - Inteligencia de cada heroe\n21 - Salir\n\n")
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
        informar_heroes_genero_M()
    elif opcion == '8':
        informar_heroes_genero_F()
    elif opcion == '9':
        informar_heroe_mas_alto_genero_M()
    elif opcion == '10':
        informar_heroe_mas_alto_genero_F()
    elif opcion == '11':
        informar_heroe_mas_bajo_genero_M()
    elif opcion == '12':
        informar_heroe_mas_bajo_genero_F()
    elif opcion == '13':
        informar_promedio_altura_genero_M()
    elif opcion == '14':
        informar_promedio_altura_genero_F()
    elif opcion == '15':
        informar_cantidad_color_de_ojos()
    elif opcion == '16':
        informar_cantidad_color_de_pelo()
    elif opcion == '17':
        informar_cantidad_inteligencias()
    elif opcion == '18':
        informar_color_de_ojos_heroes()
    elif opcion == '19':
        informar_color_de_pelo_heroes()
    elif opcion == '20':
        informar_inteligencia_heroes()
    elif opcion == '21':
        break
    else:
        print("Ingrese opcion valida")
