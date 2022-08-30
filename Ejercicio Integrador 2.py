#Ejercicio Integrador 02

#La división de alimentos está trabajando en un pequeño software para cargar las compras de ingredientes
# para la cocina de Industrias Wayne. 
#Realizar el algoritmo permita ingresar los datos de una compra de ingredientes para
# preparar comida al por mayor, HASTA QUE EL CLIENTE QUIERA.
#PESO: (entre 10 y 100 kilos)
#PRECIO POR KILO: (mayor a 0 [cero]).
#TIPO VALIDAD: ("v", "a", "m");(vegetal, animal, mezcla).
#Además tener en cuenta que si compro más de 100 kilos en total tenes 15% de descuento sobre el precio bruto. 
# O si compro más de 300 kilos en total, tenes 25% de descuento sobre el precio bruto.

#El importe total a pagar, BRUTO sin descuento.
#El importe total a pagar con descuento (Solo si corresponde).
#Informar el tipo de alimento más caro.
#El promedio de precio por kilo en total.

importe_total_bruto = 0
contador_kilos = 0
flag_tipo_mas_caro = True

while (True):
    
    while (True):
        peso = input("Ingrese peso: ")
        if not peso.isnumeric():
            print("No ingreso un numero")
            continue
        peso = int(peso)
        if peso >= 10 and peso <= 100:
            break
        print("Ingrese peso entre 10 y 100 kilos")

    while (True):
        precio_por_kilo = input("Ingrese precio por kilo: $")
        if not precio_por_kilo.isnumeric():
            print("No ingreso un numero")
            continue
        precio_por_kilo = int(precio_por_kilo)
        if precio_por_kilo > 0:
            break
        print("Ingrese precio mayor a 0")

    while (True):
        tipo = input("Ingrese tipo de ingrediente: vegetal(v), animal(a), mezcla(m): ").lower()
        if tipo == 'v' or tipo == 'a' or tipo == 'm':
            break
        print("Ingrese 'v' para vegetal, 'a' para animal o 'm' para mezcla")

    importe = precio_por_kilo * peso
    importe_total_bruto += importe
    contador_kilos += peso

    if (flag_tipo_mas_caro == True or precio_por_kilo > precio_tipo_mas_caro):
        precio_tipo_mas_caro = precio_por_kilo
        tipo_mas_caro = tipo
        flag_tipo_mas_caro = False
    
    continuar = input("Presione 's' para salir o enter para continuar agregando datos: ").lower()
    if continuar == 's':
        break

print("El importe bruto total es: $", importe_total_bruto)

if (contador_kilos > 100 and contador_kilos < 300):
    importe_total_descuento = importe_total_bruto * 0.85
    print("El importe bruto total con descuento es: $", importe_total_descuento)
    print("El descuento es del 15%")
elif (contador_kilos > 300):
    importe_total_descuento = importe_total_bruto * 0.75
    print("El importe bruto total con descuento es: $", importe_total_descuento)
    print("El descuento es del 25%")

if (tipo_mas_caro == 'v'):
    print("El tipo de alimento mas caro es Vegetal")
elif (tipo_mas_caro == 'a'):
    print("El tipo de alimento mas caro es Animal")
else:
    print("El tipo de alimento mas caro es Mezcla")

promedio_peso_por_kilo = importe_total_bruto / contador_kilos
promedio_peso_por_kilo = int(promedio_peso_por_kilo)
print("El promedio de precio por kilo es: $", promedio_peso_por_kilo)