from data_stark import lista_heroes
import re

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

def extraer_iniciales(nombre_heroe:str):
    '''
    Extrae las iniciales del heroe omitiendo el articulo 'the' o el guion

    Recibe el nombre de heroe en string

    Devuelve las iniciales del heroe separadas por un '.'
    '''
    retorno = "N/A"
    if  type(nombre_heroe) == str and len(nombre_heroe) > 0:
        separadores = "( the |-| )"
        if re.search(separadores, nombre_heroe):
            nombre_completo = re.sub(separadores, " ", nombre_heroe)
            nombre = nombre_completo.split(" ")[0]
            apellido = nombre_completo.split(" ")[1]
            iniciales = nombre[:1]+"."+apellido[:1]+"."
            retorno = iniciales
        else:
            iniciales = nombre_heroe[:1]+"."
            retorno = iniciales

    return retorno

def definir_iniciales_nombre(heroe:dict):
    '''
    Agrega la clave iniciales al diccionario cuyo valor seran las iniciales del heroe separadas
    por un punto

    Recibe el diccionario del heroe

    Devuelve False en caso de encontrar un error o True en caso de realizarse
    '''
    if type(heroe) == dict and "nombre" in heroe.keys():
        iniciales = extraer_iniciales(heroe["nombre"])
        heroe["iniciales"] = iniciales
        retorno = True
    else:
        retorno = False
    
    return retorno

def agregar_iniciales_nombre(lista_heroes:list):
    '''
    Itera la lista de heroes agregando a cada diccionario la clave iniciales con las iniciales del heroe

    Recibe la lista de heroes

    Devuelve True en caso finalizar con exito o False en caso de error
    '''
    if type(lista_heroes) == list and len(lista_heroes) > 0:
        for heroe in lista_heroes:
            error = definir_iniciales_nombre(heroe)
            if error == False:
                print("El origen de datos no contiene el formato correcto")
                retorno = False
                break
            retorno = True
    
    return retorno

def stark_imprimir_nombres_con_iniciales(lista_heroes:list):
    '''
    Imprime en pantalla el nombre de los heroes junto con sus iniciales

    Recibe la lista de heroes
    '''
    agregar_iniciales_nombre(lista_heroes)
    if type(lista_heroes) == list and len(lista_heroes) > 0:
        for heroe in lista_heroes:
            print("* {0} ({1})".format(heroe["nombre"], heroe["iniciales"]))

def generar_codigo_heroe(id_heroe:int, genero_heroe:str):
    '''
    Genera un string con el genero del heroe y el identificador del mismo

    Recibe el entero identificador del heroe y el genero del heroe como string 
    (valores 'M', 'F' o 'NB')

    Devuelve N/A en caso de no ser correcto o el codigo generado en caso de ser correcto
    '''
    str_id_heroe = str(id_heroe)
    if re.search("[0-9]+", str_id_heroe) and re.search("^(M|F|NB)$", genero_heroe): 
        if genero_heroe == "NB":
            id_heroe = str_id_heroe.zfill(7)
        elif genero_heroe == "M" or genero_heroe == "F":
            id_heroe = str_id_heroe.zfill(8)
        codigo_heroe = "{0}-{1}".format(genero_heroe, id_heroe)
        retorno = codigo_heroe
    else:
        retorno = "N/A"

    return retorno

def agregar_codigo_heroe(heroe:dict, id_heroe:int):
    '''
    Agrega la clave 'codigo_heroe' al diccionario 'heroe' recibido, cuyo valor sera el codigo de heroe

    Recibe el diccionario del heroe y el identificador del heroe

    Devuelve False en caso de encontrar un error o True en caso de realizarse
    '''
    codigo_heroe = generar_codigo_heroe(id_heroe, heroe["genero"])
    if len(heroe) > 0 and len(codigo_heroe) == 10:
        heroe["codigo_heroe"] = codigo_heroe
        retorno = True
    else:
        retorno = False

    return retorno

def stark_generar_codigos_heroes(lista_heroes):
    '''
    Itera la lista de heroes y asigna la clave codigo_heroe a cada heroe. Imprime en pantalla la cantidad de heroes a
    los que se agigno la clave, y el codigo del primer y ultimo heroe

    Recible la lista de heroes
    '''
    if len(lista_heroes) > 0:
        for heroe in lista_heroes:
            if type(heroe) == dict and "genero" in heroe.keys():
                id_heroe = lista_heroes.index(heroe)
                agregar_codigo_heroe(heroe, id_heroe)
            else:
                print("El origen de datos no contiene el formato correcto")
    else:
        print("Lista vacia")

    cantidad_heroes= len(lista_heroes)
    print("Se asignaron {0} codigos".format(cantidad_heroes))
    print("* El código del primer héroe es: {0}".format(lista_heroes[0]["codigo_heroe"]))
    print("* El código del último héroe es: {0}".format(lista_heroes[cantidad_heroes-1]["codigo_heroe"]))

def sanitizar_entero(numero_str:str):
    '''
    Analiza el string recibido y determina si es un numero entero positivo.

    Recibe un string que representa un posible numero entero

    Devuelve el numero convertido en entero
    '''
    if not re.search("^-{0,1}[0-9]+$", numero_str):
        retorno = -1
    elif int(numero_str) < 0:
        retorno = -2
    else:
        try:
            entero = int(numero_str)
            retorno = entero
        except:
            retorno = -3

    return retorno

def sanitizar_flotante(numero_str:str):
    '''
    Analiza el string recibido y determina si es un numero flotante positivo.

    Recibe un string que representa un posible numero flotante

    Devuelve el numero convertido en flotante
    '''
    if not re.search("^-{0,1}[0-9.]+$", numero_str):
        retorno = -1
    elif float(numero_str) < 0:
        retorno = -2
    else:
        try:
            flotante = float(numero_str)
            retorno = flotante
        except:
            retorno = -3

    return retorno

def sanitizar_string(valor_str:str, valor_por_defecto:str = "-"):
    '''
    Analiza el string recibido y determina si es solo texto. En caso de contener una barra, la
    reemplaza por un espacio. 

    Recibe un string que representa el texto a validar y un string que representa un valor por defecto

    Devuelve, en caso de que se verifique que el parametro es solo texto, el texto convertido a
    minusculas y sin espacios en blanco al principio o final.
    Si contiene numeros devuelve 'N/A'
    Si el parametro recibido esta vacio devuelve el valor por defecto convertido a minusculas
    '''
    if not re.search("[0-9]+", valor_str):
        if len(valor_str) == 0:
            retorno = valor_por_defecto.lower().strip()
        else:
            if valor_str.count("/"):
                valor_str = re.sub("/", " ", valor_str)
            valor_str = valor_str.lower().strip()
            retorno = valor_str
    else:
        retorno = "N/A"

    return retorno
    
def sanitizar_dato(heroe:dict, clave:str, tipo_dato:str):
    '''
    Sanitiza el valor del diccionario correspondiente a la clave y al tipo de dato recibido

    Recibe el diccionario con los datos del personaje, la clave del diccionario a sanitizar 
    y el tipo de dato a sanitizar

    Devuelve True en caso de haber sanitizado algun dato o False en caso contrario
    '''
    retorno = False
    tipo_dato = tipo_dato.lower()
    if tipo_dato == "string" or tipo_dato == "entero" or tipo_dato == "flotante":
        if clave in heroe.keys():
            if tipo_dato == "string":
                sanitizar_string(heroe[clave],"-")
            elif tipo_dato == "entero":
                sanitizar_entero(heroe[clave])
            else:
                sanitizar_flotante(heroe[clave])
            retorno = True
        else:
            retorno = "La clave especificada no existe en el héroe"
    else:
        retorno = "Tipo de dato no reconocido"

    return retorno

def stark_normalizar_datos(lista_heroes:list):
    '''
    Recorre la lista de heroes y sanitiza los datos: altura, peso, color_ojos, color_pelo, fuerza
    e inteligencia.

    Recibe la lista de heroes a sanitizar
    '''
    if len(lista_heroes) > 0:
        for heroe in lista_heroes:
            sanitizar_dato(heroe, "altura", "flotante")
            sanitizar_dato(heroe, "peso", "flotante")
            sanitizar_dato(heroe, "color_ojos", "string")
            sanitizar_dato(heroe, "color_pelo", "string")
            sanitizar_dato(heroe, "fuerza", "entero")
            sanitizar_dato(heroe, "inteligencia", "string")
        print("Datos normalizados")
    else:
        print("Error: Lista de heroes vacia")

def generar_indice_nombres(lista_heroes:list):
    '''
    Itera la lista de heroes y genera otra lista donde cada elemento es cada palabra que componen el nombre de los personajes

    Recibe la lista de heroes

    Devuelve la lista de elementos nuevos
    '''
    lista_nombres = []
    if len(lista_heroes) > 0:
        for heroe in lista_heroes:
            if type(heroe) == dict and "nombre" in heroe.keys():
                lista_palabras = re.findall("[a-zA-Z0-9]+", heroe["nombre"])
                for palabra in lista_palabras:
                    lista_nombres.append(palabra)
            else:
                print("El origen de datos no contiene el formato correcto")
    else:
        print("Lista vacia")

    return lista_nombres

def stark_imprimir_indice_nombre(lista_heroes:list):
    '''
    Recorre la lista de heroes e mprime en pantalla cada palabra que compone los nombres de los
    heroes separadas por un guion

    Recibe la lista de heroes
    '''
    lista_indices = generar_indice_nombres(lista_heroes)
    print("-".join(lista_indices))

def convertir_cm_a_mtrs(valor_cm:float):
    '''
    Recibe un numero flotante que equivale a una medida en cm y lo convierte a la unidad metros
    
    Recibe un numero flotante positivo

    Devuelve el numero en unidad metros o -1 en caso de no ser un numero positivo flotante
    '''
    if type(valor_cm) == float and valor_cm >= 0:
        metros = valor_cm / 100
        retorno = metros
    else:
        retorno = -1

    return retorno

def generar_separador(patron:str, largo:int, imprimir:bool = True):
    '''
    Genera un string que contiene el patron recibido tantas veces como la cantidad recibida por
    parametro uno junto al otro. Si el parametro imprimir es True, lo imprime en pantalla.

    Recibe un string de entre 1 y 2 caracteres como patron, el numero que indica la cantidad de 
    veces a repetir el patron, y en caso de no querer imprimirlo en pantalla un parametro de 
    tipo booleano.

    Devuelve el separador generado
    '''
    separador = ''
    if (len(patron) > 0 and len(patron) < 3) and (largo > 0 and largo < 236):
        for i in range(largo):
                separador += patron
        retorno = separador
        if imprimir == True:
            print(separador)
    else:
        retorno = "N/A"

    return retorno

def generar_encabezado(titulo:str):
    '''
    Genera un string que contenga el parametro titulo entre dos separadores

    Recibe el string a usar como titulo

    Devuelve el encabezado generado
    '''
    separador = generar_separador("*", 75, False)
    encabezado = separador + "\n" + titulo.upper() + "\n" + separador
    
    return encabezado

def imprimir_ficha_heroe(heroe:dict):
    '''
    Genera una ficha de heroe y la imprime en pantalla

    Recibe por parametro el heroe del que imprimir la ficha
    '''
    agregar_codigo_heroe(heroe, lista_heroes.index(heroe))
    agregar_iniciales_nombre(lista_heroes)
    altura = convertir_cm_a_mtrs(float(heroe["altura"]))
    peso = float(heroe["peso"])
    ficha_heroe = ""
    ficha_heroe += generar_encabezado("principal") + "\n"
    ficha_heroe += "     NOMBRE DEL HÉROE:               {0}({1})\n".format(heroe["nombre"], heroe["iniciales"])
    ficha_heroe += "     IDENTIDAD SECRETA:              {0}\n".format(heroe["identidad"])
    ficha_heroe += "     CONSULTORA:                     {0}\n".format(heroe["empresa"])
    ficha_heroe += "     CODIGO DE HEROE:                {0}\n".format(heroe["codigo_heroe"])
    ficha_heroe += generar_encabezado("fisico") + "\n"
    ficha_heroe += "     ALTURA:                         {0:.2f}Mtrs.\n".format(altura)
    ficha_heroe += "     PESO:                           {0:.2f}Kg.\n".format(peso)
    ficha_heroe += "     FUERZA:                         {0}N\n".format(heroe["fuerza"])
    ficha_heroe += generar_encabezado("señas particulares") + "\n"
    ficha_heroe += "     COLOR DE OJOS:                  {0}\n".format(heroe["color_ojos"])
    ficha_heroe += "     COLOR DE PELO                   {0}\n".format(heroe["color_pelo"])

    print(ficha_heroe)

def stark_navegar_fichas(lista_heroes:list):
    '''
    Imprime la ficha del primer personaje y permite al usuario navegar las fichas de los 
    personajes hasta que desee salir

    Recibe la lista de heroes a recorrer
    '''
    marcador = 0
    while True:
        imprimir_ficha_heroe(lista_heroes[marcador])
        opcion = input("[1]Ir a la izquierda     [2]Ir a la derecha     [S]Salir\n").lower()
        if opcion == "1":
            marcador -= 1
            if marcador == -1:
                marcador = 23
        elif opcion == "2":
            marcador += 1
            if marcador == 24:
                marcador = 0
        elif opcion == "s":
            break

def imprimir_menu():
    '''
    Imprime un menu de opciones en pantalla
    '''
    print("1- Imprimir la lista de nombres junto con sus iniciales\n2- Generar codigos de heroes\n"
    "3- Normalizar datos\n4- Imprimir indice de nombres\n5- Navegar fichas\nS- Salir\n")

def stark_menu_principal():
    '''
    Imprime el menu de opciones y pide la seleccion de una de ellas

    Devuelve la respuesta del usuario
    '''
    imprimir_menu()
    opcion = input("Ingrese una opcion:  ")
    return opcion

def stark_marvel_app_3(lista_heroes:list):
    '''
    
    '''
    while True:
        opcion = stark_menu_principal().lower()
        if opcion == "1":
            stark_imprimir_nombres_con_iniciales(lista_heroes)
        elif opcion == "2":
            stark_generar_codigos_heroes(lista_heroes)
        elif opcion == "3":
            stark_normalizar_datos(lista_heroes)
        elif opcion == "4":
            stark_imprimir_indice_nombre(lista_heroes)
        elif opcion == "5":
            stark_navegar_fichas(lista_heroes)
        elif opcion == "s":
            break
        else:
            print("Opcion incorrecta, seleccione una opcion correcta")

stark_marvel_app_3(lista_heroes)