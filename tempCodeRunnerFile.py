# Ejercicio 12
precios_frutas = {
    'manzana': 1.5,  # Precio por kilo de manzana
    'banana': 2.0,   # Precio por kilo de banana
    'pera': 1.8,     # Precio por kilo de pera
    # Agrega más frutas y sus precios aquí
}

# Pedir al usuario que ingrese la fruta y la cantidad de kilos
fruta = input('Ingrese el nombre de la fruta: ').lower()
kilos = float(input('Ingrese la cantidad de kilos: '))


# Verificar si la fruta está en el diccionario
if fruta in precios_frutas:
    # Calcular el precio total
    precio_total = precios_frutas[fruta] * kilos
    #resultado
    mensaje = 'El precio de {} kilos de {} es: ${:.2f}'
    print(mensaje.format(kilos, fruta, precio_total))
else:
    # Mostrar un mensaje si la fruta no está en el diccionario
    print('Lo siento, no tenemos el precio para la fruta ingresada.')

