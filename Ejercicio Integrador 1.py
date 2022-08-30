#Ejercicio Integrador 01

#Debemos realizar la carga de 5 (cinco) productos de prevención de contagio, de cada una debe obtener los siguientes datos:
#El tipo (validar "barbijo", "jabón" o "alcohol")
#El precio: (validar entre 100 y 300)
#La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las 1000 unidades)
#La marca y el Fabricante.
  
# Se debe informar lo siguiente:
#A-Del más caro de los barbijos, la cantidad de unidades y el fabricante.
#B-Del ítem con más unidades, el fabricante.
#C-Cuántas unidades de jabones hay en total.

flag_barbijo_caro = True
flag_item_mas_unidades = True
cantidad_jabones = 0

for iteracion in range(5):
    
    while(True):
        tipo_producto = input("Ingrese tipo de producto(jabon, barbijo, alcohol): ").lower()
        if tipo_producto == 'barbijo' or tipo_producto == 'jabon' or tipo_producto == 'alcohol':
            break
        print("Ingrese producto valido")

    while(True):
        precio = input("Ingrese precio: $")
        if not precio.isnumeric():
            print("No ingreso un numero")
            continue
        precio = int(precio)
        if precio >= 100 and precio <= 300:
            break
        print("Ingrese precio entre 100 y 300")

    while (True):
        cantidad = input("Ingrese cantidad: ")
        if not cantidad.isnumeric():
            print("No ingreso un numero")
            continue
        cantidad = int(cantidad)
        if cantidad >= 0 and cantidad <= 1000:
            break
        print("Ingrese cantidad entre 0 y 1000")

    marca = input("Ingrese marca: ").capitalize()
    fabricante = input("Ingrese fabricante: ").capitalize()

    if tipo_producto == 'barbijo':
        if (flag_barbijo_caro == True or precio > precio_barbijo_caro):
            precio_barbijo_caro = precio
            cantidad_barbijo_caro = cantidad
            fabricante_barbijo_caro = fabricante
            flag_barbijo_caro = False
    elif tipo_producto == 'jabon':
        cantidad_jabones += cantidad
    
    if (flag_item_mas_unidades == True or cantidad > item_mas_unidades):
        item_mas_unidades = cantidad
        fabricante_mas_unidades = fabricante
        flag_item_mas_unidades = False

print("Barbijo mas caro hay: ", cantidad_barbijo_caro, " y lo fabrica: ", fabricante_barbijo_caro)
print("El item con mas unidades lo fabrica: ", fabricante_mas_unidades)
print("Jabones hay: ", cantidad_jabones)