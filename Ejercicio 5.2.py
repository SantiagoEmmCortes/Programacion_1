#Ejercicio 02

#1- Una cervecería desea guardar los nombres de sus clientes a medida que van realizando
#  los pedidos para luego imprimir los nombres de todos los clientes.
#  Se solicita crear un programa que almacene dichos nombres en una lista hasta que
#  el usuario desee y luego, una vez finalizado el ingreso, imprima la lista por pantalla.

#2- Utilizando el programa anterior, ahora se necesitan guardar más datos del cliente.
#  Se tiene que guardar en cada posición de la lista,  el nombre, la cantidad de cervezas
#  compradas y la edad del cliente. Para lo cual se deberá crear un diccionario con los
#  siguientes datos

#nombre: Karen
#cantidad_cervezas: 2
#edad: 36
#Al finalizar la carga se deberán mostrar por pantalla a todos los clientes que sean
#  mayores de 30 años.

#3- Se anexará al programa anterior una lista que contenga diccionarios que guarden
#  las distintas características que tienen las cervezas que se venden. 
#Por ejemplo: { “Ipa”: { “codigo” : 25007 , ”ibu” : 18 , ”marca” : ”Patagonia” } }
#4 - Se agrega al diccionario del punto dos un campo que indique que tipo de cerveza
#  consume, ya que estas pueden ser más de una y de distinto tipo, dicho campo deberá
#  ser una lista.

#nombre: Marina
#cantidad: 2
#edad: 30
#cerveza_comprada: ipa , apa
#Imprimir los datos de la cerveza ipa junto a los datos del cliente.


lista_diccs = []
dicc_clientes = {}
#i=0
#dicc_trabajo = {}

while (True):

    nombre = input("Nombre: ")
    dicc_clientes["nombre"] = nombre
    cant_cervezas = input("Cantidad de cervezas: ")
    dicc_clientes["cantidad_cervezas"] = cant_cervezas
    edad = input("Edad: ")
    edad = int(edad)
    dicc_clientes["edad"] = edad
    lista_diccs.append(dicc_clientes.copy())

    continuar = input("Presione 's' para salir o enter para continuar agregando datos: ").lower()
    if continuar == 's':
        break

print("Clientes: ", lista_diccs)

for i in range(len(lista_diccs)):
    if lista_diccs[i]['edad'] > 30:
        print(lista_diccs[i])
        
#TODO Incompleto, revisar