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

def stark_normalizar_datos(lista:list):
    '''
    Castea al tipo de dato correcto las keys necesarias de una lista

    Recibe una lista de diccionarios
    '''
    if lista:
        flag_datos_normalizados = False
        for heroe in lista:
            if type(heroe["altura"]) != float or type(heroe["peso"]) != float or type(heroe["fuerza"]) != int:
                heroe["altura"] = float(heroe["altura"])
                heroe["peso"] = float(heroe["peso"])
                heroe["fuerza"] = int(heroe["fuerza"])
                flag_datos_normalizados = True
        if flag_datos_normalizados == True:
            print("Datos normalizados")
    else:
        print("Error: Lista de heroes vacia")

def obtener_nombre(heroe:dict):
    '''
    Recibe un diccionario que representa a un heroe
    
    Devuelve el nombre del heroe de ese diccionario
    '''
    string_nombre = "Nombre: " + heroe["nombre"]
    return string_nombre

def imprimir_dato(dato:str):
    '''
    Recibe un string y lo imprime en pantalla
    '''
    print(dato)

def stark_imprimir_nombres_heroes(lista:list):
    '''
    Recorre la lista recibida por parametro e imprime el nombre de cada uno de los heroes

    Acepta una lista de heroes

    Devuelve el nombre de cada uno de los heroes de la lista o -1 en caso de error
    '''
    if type(lista) == list and len(lista) > 0:
        for heroe in lista:
            nombre_heroe = obtener_nombre(heroe)
            imprimir_dato(nombre_heroe)
    else:
        return -1

def obtener_nombre_y_dato(heroe:dict,clave:str):
    '''
    Recibe un diccionario y la clave deseada del mismo

    Devuelve un string que contenga el nombre del heroe y el dato (clave) del heroe a imprimir
    '''
    nombre_heroe = "Nombre: " + heroe["nombre"]
    dato_heroe = clave + ": "+ str(heroe[clave])
    string_nombre_y_dato = nombre_heroe + "|" + dato_heroe
    return string_nombre_y_dato

def stark_imprimir_nombres_alturas(lista:list):
    '''
    Recibe una lista de diccionarios

    Itera la lista de heroes imprimiendo el nombre y altura de cada heroe
    '''
    if type(lista) == list and len(lista) > 0:
        for heroe in lista:
            nombre_heroe_altura = obtener_nombre_y_dato(heroe, "altura")
            imprimir_dato(nombre_heroe_altura)
    else:
        return -1

def calcular_max(lista:list, clave:str):
    '''
    Calcula el maximo de la clave recibida

    Recibe una lista de diccionarios y la clave a utilizar para calcular

    Devuelve el diccionario que contiene el maximo de la clave
    '''
    stark_normalizar_datos(lista_heroes)
    retorno = -1
    if type(lista) == list and len(lista) > 0 and type(clave) == str:
        maximo = lista[0]
        for heroe in lista:
            if heroe[clave] > maximo[clave]:
                maximo = heroe
        retorno = maximo
    
    return retorno

def calcular_min(lista:list, clave:str):
    '''
    Calcula el minimo de la clave recibida

    Recibe una lista de diccionarios y la clave a utilizar para calcular

    Devuelve el diccionario que contiene el minimo de la clave
    '''
    stark_normalizar_datos(lista_heroes)
    retorno = -1
    if type(lista) == list and len(lista) > 0 and type(clave) == str:
        minimo = lista[0]
        for heroe in lista:
            if heroe[clave] < minimo[clave]:
                minimo = heroe
        retorno = minimo
    
    return retorno

def calcular_min_max_dato(lista:list, calculo:str, clave:str):
    '''
    Calcula el minimo/maximo de la clave recibida

    Recibe una lista de diccionarios, la clave a utilizar para calcular y el tipo de calculo ("minimo" o "maximo")

    Devuelve el diccionario que contiene el minimo/maximo de la clave
    '''
    if calculo == "minimo":
        min_max = calcular_min(lista,clave)
    elif calculo == "maximo":
        min_max = calcular_max(lista,clave)
    return min_max

def stark_calcular_imprimir_heroe(lista:list, calculo:str, clave:str):
    '''
    Calcula el minimo/maximo de la clave recibida y lo imprime en pantalla

    Recibe una lista de diccionarios, la clave a utilizar para calcular y el tipo de calculo ("minimo" o "maximo")

    Devuelve el nombre del heroe junto con la clave, del diccionario que contiene el minimo/maximo
    '''
    if type(lista) == list and len(lista) > 0 and type(clave) == str and type(calculo) == str:
        min_max_heroe = calcular_min_max_dato(lista, calculo, clave)
        heroe_nombre_clave = obtener_nombre_y_dato(min_max_heroe, clave)
        imprimir_dato(heroe_nombre_clave)
    else:
        return -1

def sumar_dato_heroe(lista:list, clave:str):
    '''
    Suma los datos de la clave recibida por parametro

    Recibe una lista de diccionarios y la clave a sumar

    Devuelve la suma de todos los datos de la clave pasada por parametro
    '''
    stark_normalizar_datos(lista)
    suma_claves = 0
    for heroe in lista:
        if type(heroe) == dict and len(heroe) > 0:
            suma_claves += heroe[clave]
    return suma_claves

def dividir(dividendo:float, divisor:float):
    '''
    Realiza la division entre los parametros

    Recibe dos numeros, dividendo y divisor

    Devuelve el resultado de la division entre parametros o 0 si el divisor es 0
    '''
    retorno = 0
    if divisor != 0:
        division = dividendo / divisor
        retorno = division
    return retorno

def calcular_promedio(lista:list, clave:str):
    '''
    Calcula el promedio de la clave recibida por parametro dentro de una lista de diccionarios

    Recibe una lista de diccionarios y la clave sobre la cual calcular el promedio

    Devuelve el promedio de la clave pasada por parametro
    '''
    suma_clave = sumar_dato_heroe(lista, clave)
    promedio = dividir(suma_clave, len(lista))
    return promedio

def stark_calcular_imprimir_promedio_altura(lista:list):
    '''
    Calcula la altura promedio de la lista de heroes y la imprime en pantalla

    Recibe una lista de heroes
    '''
    if type(lista) == list and len(lista) > 0:
        promedio_altura = calcular_promedio(lista, "altura")
        str_promedio_altura = "Promedio de altura: " + str(promedio_altura)
        imprimir_dato(str_promedio_altura)
    else:
        print(-1)

def imprimir_menu():
    '''
    Imprime en pantalla el menu de opciones
    '''
    str_menu = '''\nSeleccione opcion:\n1 - Lista de heroes\n2 - Lista de heroes con altura\n3 - Heroe mas alto
4 - Heroe mas bajo\n5 - Promedio de altura de heroes\n6 - Heroe mas pesado\n7 - Heroe menos pesado\n8 - Salir\n'''
    imprimir_dato(str_menu)

def validar_entero(numero:str):
    '''
    Verifica que el parametro ingresado sea un string conformado unicamente por numeros

    Recibe un string de numeros

    Devuelve True si el string esta conformado unicamente por numeros o False si no lo esta
    '''
    validacion = numero.isnumeric()
    return validacion

def stark_menu_principal():
    '''
    Imprime el menu de opciones y recibe por input el numero de opcion elegida, si es correcto lo castea a entero,
    si es incorrecto devuelve -1
    '''
    retorno = -1
    imprimir_menu()
    opcion = input("Opcion elegida:")
    if validar_entero(opcion) == True:
        opcion = int(opcion)
        retorno = opcion
    return retorno
    
def stark_marvel_app(lista:list):
    while(True):
        opcion = stark_menu_principal()
        if opcion == 1:
            stark_imprimir_nombres_heroes(lista)
        elif opcion == 2:
            stark_imprimir_nombres_alturas(lista)
        elif opcion == 3:
            stark_calcular_imprimir_heroe(lista, "maximo", "altura")
        elif opcion == 4:
            stark_calcular_imprimir_heroe(lista, "minimo", "altura")
        elif opcion == 5:
            stark_calcular_imprimir_promedio_altura(lista)
        elif opcion == 6:
            stark_calcular_imprimir_heroe(lista, "maximo", "peso")
        elif opcion == 7:
            stark_calcular_imprimir_heroe(lista, "minimo", "peso")
        elif opcion == 8:
            break
        else:
            print("Ingrese opcion valida")

stark_marvel_app(lista_heroes)