#Ejercicio Integrador 03

#La división de alimentos de industrias Wayne está trabajando en un pequeño software
#  para cargar datos de heroínas y héroes, para para tener un control de las condiciones 
#  de heroes existentes, nos solicitan:
#Nombre de Heroína/Héroe
#EDAD (mayores a 18 años)
#Sexo ("m", "f" o "nb")
#Habilidad ("fuerza", "magia", "inteligencia").
#A su vez, el programa deberá mostrar por consola lo siguiente:

#Dar el nombre de Héroe | Heroína de 'fuerza' más joven.
#El sexo y nombre de Heroe | Heroína de mayor edad.
#La cantidad de Heroinas que tienen habilidades de 'fuerza' o 'magia'.
#El promedio de edad entre Heroinas.
#El promedio de edad entre Heroes de fuerza.

flag_fuerza_mas_joven = True
flag_mayor_edad = True
contador_heroinas_fuerza_magia = 0
acumulador_edad_heroinas = 0
contador_heroinas = 0
acumulador_edad_heroes_fuerza = 0
contador_heroes_fuerza = 0

while (True):

    nombre = input("Ingrese nombre de Heroe/Heroina: ").capitalize()

    while (True):
        edad = input("Ingrese edad: ")
        if not edad.isnumeric():
            print("No ingreso un numero")
            continue
        edad = int(edad)
        if edad > 18:
            break
        print("Ingrese edad mayor a 18 años")

    while (True):
        sexo = input("Ingrese sexo de Heroe/Heroina: 'm', 'f', 'nb': ").lower()
        if sexo == 'm' or sexo == 'f' or sexo == 'nb':
            break
        print("Ingrese 'm', 'f' o 'nb'")

    while (True):
        habilidad = input("Ingrese habilidad de Heroe/Heroina: 'fuerza', 'magia', 'inteligencia': ").lower()
        if habilidad == 'fuerza' or habilidad == 'magia' or habilidad == 'inteligencia':
            break
        print("Ingrese 'fuerza', 'magia' o 'inteligencia'")

    if habilidad == 'fuerza':
        if flag_fuerza_mas_joven == True or edad < edad_fuerza_mas_joven:
            edad_fuerza_mas_joven = edad
            nombre_fuerza_mas_joven = nombre
            flag_fuerza_mas_joven = False
        if sexo == 'm':
            contador_heroes_fuerza += 1
            acumulador_edad_heroes_fuerza += edad

    if flag_mayor_edad == True or edad > edad_mayor_edad:
        edad_mayor_edad = edad
        nombre_mayor_edad = nombre
        sexo_mayor_edad = sexo
        flag_mayor_edad = False

    if sexo == 'f':
        if habilidad == 'fuerza' or habilidad == 'magia':
            contador_heroinas_fuerza_magia += 1
        contador_heroinas += 1
        acumulador_edad_heroinas += edad

    continuar = input("Presione 's' para salir o enter para continuar agregando datos: ").lower()
    if continuar == 's':
        break

promedio_edad_heroinas = acumulador_edad_heroinas / contador_heroinas
promedio_edad_heroes_fuerza = acumulador_edad_heroes_fuerza / contador_heroes_fuerza

print("El nombre de Heroe/Heroina de fuerza mas joven es:",nombre_fuerza_mas_joven, 
    "con", edad_fuerza_mas_joven, "años")
print("El sexo y nombre de Heroe/Heroina de mayor edad es:", sexo_mayor_edad, nombre_mayor_edad,
    "con", edad_mayor_edad,"años")
print("La cantidad de Heroinas que tienen habilidades de fuerza o magia es:", contador_heroinas_fuerza_magia)
print("El promedio de edad entre Heroinas es:", promedio_edad_heroinas, "años")
print("El promedio de edad entre Heroes de fuerza es:", promedio_edad_heroes_fuerza, "años")