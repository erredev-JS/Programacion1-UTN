#Tienda de ropa

"""Geier Indumentaria.
Es un programa que prepara una orden de compra. Primeramente nos presenta un menú con las opciones “Comprar”, “Consultar stock” y “Forma de pago y descuentos”. Seleccionando “2”  muestra la lista de artículos con sus respectivos precios. Para darle al cliente la opción de comprar si lo desea o “salir”. Seleccionando “3” nos da información de las alternativas de pago. El precio del flete, recargos si abona con tarjeta o descuento si abona en efectivo. Y seleccionando “1” nos lleva a la compra. Nos muestra la lista de artículos con los precios. Luego tenemos que indicar la cantidad de tipo de artículos que vamos a comprar y de acuerdo a esto el programa solicita el código del artículo y la cantidad que queremos del mismo. Una vez especificado todos los artículos  nos pregunta sobre el modo de pago “tarjeta/efectivo”. Al indicar un método el programa calcula la recarga o el descuento correspondiente y si suma el flete.
Por último muestra el detalle de la compra: cantidad, artículo, precio total por artículo,
y monto total de la compra.
"""
# Variables del stock
list_article = ["Pantalones", "Camisas", "Remeras", "Faldas", "Corbatas", "Jogging"]
list_price = [5000, 7500, 3990, 6000, 2400, 6750]




# Variables del precio
payment_validation = 0
sub_total = 0
freight_cost = 2500
total = 0
# Mensajes de bienvenida y sistema para entrar
print("Bienvenido al sistema de menú interactivo de Geier Indumentaria")
option_menu = 5
print("menú 1: Compras ")
print("menú 2: Consultar stock. ")
print("menú 3: Forma de pago y descuentos: ")




    # Ciclo para ingresar al menú y también de validación del primer dato de cod_article
while option_menu != 0:
    option_menu =(input("Por favor, ingrese [1] para el menú 1, [2] para el menú 2, [3] para el menú 3 o [0] para salir: "))
    # Verificar si la opción ingresada es válida
    if option_menu == "1" or option_menu == "2" or option_menu == "3" or option_menu == "0":
        option_menu = int(option_menu)
        # Salir del programa
        if option_menu == 0:
            print("Usted ha ingresado 0 para salir del programa. ¡Hasta pronto!")
            break
        # Mostrar lista de precios
        elif option_menu == 1:
            print("Usted ha ingresado 1. Compras: ...")
            print("Lista de precios")
            list_article = ["Pantalones", "Camisas", "Remeras", "Faldas", "Corbatas", "Jogging"]
            list_price = [5000, 7500, 3990, 6000, 2400, 6750]




            for i in range(6):
                print(f"(cod:{i + 1}). {list_article[i]} ${list_price[i]}")




            order = {}
            article_types = int(input("¿Cuántos tipos de artículos contiene el pedido?: "))




            if article_types > 6:
                print("Número ingresado incorrecto")
            else:
                # Pedir información sobre los artículos a comprar
                for n in range(article_types):
                    while True:
                        cod_article = (input("Ingrese el código del artículo: "))
                        if len(cod_article) == 1 and cod_article.isdigit():
                            break
                        else:
                            print("Error. Debes ingresar solo un dígito.")
                    cod_article = int(cod_article)
                    if (cod_article < 1) or (cod_article > 6):
                        print("Número ingresado incorrecto")
                    else:
                        article = list_article[cod_article - 1]
                        amount = int(input(f"Ingresar la cantidad de {article} que desea pedir: "))




                        if article in order:
                            order[article] += amount
                        else:
                            order[article] = amount




                        price = list_price[cod_article - 1] * amount
                        sub_total += price
                #Preguntar método de pago hasta que se ingrese un valor válido
                while payment_validation == 0:
                    payment_method = input(f"¿Cuál va a ser el método de pago? \nEfectivo/Tarjeta\n").lower()




                    if payment_method == "efectivo":
                        if sub_total > 10000:
                            total = sub_total - freight_cost
                            break
                        else:
                            total = sub_total
                            break
                    elif payment_method == "tarjeta":
                        total += sub_total + (sub_total * 0.15)
                        break
                    else:
                        print("Método ingresado inválido. Intente otra vez.\n")
            # Mostrar resumen de compra
            total_articles = sum(order.values())
            for article, amount in order.items():
                print(f'Se compraron {amount} de {article} ${list_price[list_article.index(article)] * amount}')




            print(f"El precio final de la compra es: ${total}")
        # Opción para consultar stock
        elif option_menu == 2:
            print("Usted ha ingresado 2. Consultar stock: ... ")
            print("Stock de artículos: ")




            for i in range(6):
                print(f"(cod:{i + 1}). {list_article[i]} - Precio unitario: ${list_price[i]} ")
        # Opción para mostrar formas de pago y descuentos
        elif option_menu == 3:
            print(f"\n Usted ha ingresado 3. Formas de pago y descuentos: ...")
            print("Para pagos con tarjetas, hay un recargo del 15%")
            print("El envío de los productos cuesta $2.500")
            print(f"Si la compra supera los $10.000 pesos, el envío es gratis.\n")
        # Si la opción ingresada no corresponde
        else:
            print("La opción ingresada no corresponde, inténtelo nuevamente.")
    # Si el valor ingresado no es válido
    else:
        print("Valor ingresado inválido")









