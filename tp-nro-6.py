## Funciones en  funciones_ejercicios.py ##
import funciones_ejercicios as funcion
# Ejercicio 1

op = 1
list = []
while op != 0:
  op = int(input('Ingresa un numero para agregarlo a la lista, si quieres salir ingresa 0\n'))
  if op != 0:
    list.append(op)

print(list)

# Ejercicio 2

op_delete = int(input('Ingresa un numero que quieras borrar de la lista, si el numero no esta en la lista, no podras borrarlo'))

if op_delete in list:
  print('El numero si esta en la lista, procederemos a borrarlo')
  list.remove(op_delete)
else:
  print('El numero no esta en la lista')
print(list)


# Ejercicio 3

suma = 0;


for n in list:
  suma += n


print(f'la suma de los numeros de la lista es {suma}')


# Ejercicio 4

new_num = input('Ingresa un numero, para crear una nueva lista de numeros que sean inferiores a ese numero:\n')

new_list = [n for n in list if n < int(new_num)]

print(new_list)


# Ejercicio 5 

element_count = {}
for num in list:
    if num in element_count:
        element_count[num] += 1
    else:
        element_count[num] = 1

tuple_list = [(element, count) for element, count in element_count.items()]

# Ejercicio 6

# Crear listas para los nombres de primaria y secundaria
primary_school = []
high_school = []

# Ingresar los nombres de pila de los ALUMNOS DE PRIMARIA
print('Ingresar los nombres de pila de los ALUMNOS DE PRIMARIA (Cuando no quiera ingresar más nombres, ingrese "x"):')
while True:
    name_primary = input().capitalize()
    if name_primary == 'X':
        break
    if name_primary.isalpha():  # Verificar si el valor ingresado es una palabra
        primary_school.append(name_primary)
    else:
        print("El valor ingresado no es una palabra")

# Ingresar los nombres de pila de los ALUMNOS DE SECUNDARIA
print('Ingresar los nombres de pila de los ALUMNOS DE SECUNDARIA (Cuando no quiera ingresar más nombres, ingrese "x"):')
while True:
    name_high = input().capitalize()
    if name_high == 'X':
        break
    if name_high.isalpha():  # Verificar si el valor ingresado es una palabra
        high_school.append(name_high)
    else:
        print("El valor ingresado no es una palabra")

# Obtener nombres de nivel primario sin repetición
unique_primary = list(set(primary_school))
print("NIVEL PRIMARIO")
for name in unique_primary:
    print(f"-{name}")

# Obtener nombres de nivel secundario sin repetición
unique_high = list(set(high_school))
print("NIVEL SECUNDARIO")
for name in unique_high:
    print(f"-{name}")

# Nombres repetidos en primaria
repeated_primary = [name for name in primary_school if primary_school.count(name) > 1]
print("Nombres repetidos nivel PRIMARIO")
for name in repeated_primary:
    print(f"-{name}")

# Nombres repetidos en secundaria
repeated_high = [name for name in high_school if high_school.count(name) > 1]
print("Nombres repetidos nivel SECUNDARIO")
for name in repeated_high:
    print(f"-{name}")

# Estudiantes del primario que no se repiten en el secundario
not_in_high_school = [name for name in unique_primary if name not in unique_high]
print("Estudiantes del primario que no se repiten en el secundario")
for name in not_in_high_school:
    print(name)

# Ejercicio 7

phrase_list = []
for i in range(3, 0, -1):
    phrase = input(f"Ingrese {i} oraciones: ")
    phrase_list.append(phrase)
funcion.count_characters(phrase_list)

# Ejercicio 8

#lista de listas de goles de cada equipo:
goal_list=[(0,4,2,1,2,3,1,2,3,0),(5,0,3,2,2,0,0,3,1,2),(0,2,0,1,3,0,1,2,4,2),(1,0,2,0,1,2,3,1,1,0),(1,1,2,1,0,2,1,3,0,3),(1,2,3,1,0,0,2,4,3,1),(4,5,0,0,2,4,0,1,2,1),(2,2,1,0,3,1,3,0,1,1),(0,2,1,0,3,4,5,1,0,2),(0,2,3,3,1,0,0,3,1,0)]


#"Goles de cada equipo:"
print("Goles de cada equipo:")
i=1
for team in goal_list:
    print(f"Equipo {i}: {team}")
    i+=1


# Cantidad de triunfos por equipo
# Total de goles realizados y recividos por equipos
print("-----------------------------")
for i in range(10):
    victory=0
    defeat=0
    tie=0
    goals_scored=0
    goals_against=0
    print(f"partidos del equipo: {i+1}")
    for j in range(10):
        #Total de goles realizados y recividos por equipos
        goals_scored+=goal_list[i][j]
        goals_against+=goal_list[j][i]
        # Cantidad de triunfos por equipo
        if(i!=j):
            if(goal_list[i][j]>goal_list[j][i]):
                victory+=1
            elif(goal_list[i][j]<goal_list[j][i]):
                defeat+=1
            else:
                tie+=1
    print(f"Victorias: {victory}\nDerrotas:{defeat}\nEmpates: {tie}")
    print(f"Total de goles marcados: {goals_scored}\nTotal de goles recibidos: {goals_against}\nPuntos: {victory*3 + tie}
\n-----------------------------")

# Ejercicio 9

print("Bienvenid@ al Juego de memoria. ")
cards = funcion.posicionate_characters()
#se le mostrará al user para saber visualmente cuanto ha avanzado en el juego
enigm_cards = [["?", "?", "?", "?", "?", "?"],
                ["?", "?", "?", "?", "?", "?"],
                ["?", "?", "?", "?", "?", "?"]
                ]


to_adivinate = [[1,2,3,4,5,6],
                [7,8,9,10,11,12],
                [13,14,15,16,17,18]
                ]
#lista de los números ya adivinados correctamente
list_of_correct_nums = []


#mientras todavia no haya adivinado todos los elementos el código se ejecutará
while "?" in [item for row in enigm_cards for item in row]:
    print()
    funcion.prin_cards(to_adivinate)
    while True:
        try:
            coincidence = False


            #el user ingresa una posicion a adivinar
            user_try = funcion.comprb_valid_num("Ingrese un número para ver la figura: ", list_of_correct_nums)


            funcion.prin_cards(funcion.find_card1(user_try, enigm_cards, cards))


            print()


            user_compare = funcion.comprb_valid_num("Ingrese un número para comparar la figura: ", list_of_correct_nums)


            funcion.prin_cards(funcion.find_card1(user_compare, enigm_cards, cards))


            print()


            #compara los simbolos de las posiciones, si son iguales se guardan
            enigm_cards, to_adivinate, coincidence = funcion.compare_cards(user_try, user_compare, enigm_cards, cards, to_adivinate, coincidence)
            if coincidence == True:
                list_of_correct_nums.append(user_try)
                list_of_correct_nums.append(user_compare)
            break
        except ValueError:
            print("Ingrese un número del 1 al 18")
       
print("Felicidades has adivinado todos los símbolos!")

# Ejercicio 10

first_matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
diagonal = funcion.calc_diagonal(first_matrix)
print(diagonal)


inv_diagonal = funcion.calc_inv_diagonal(first_matrix)
print(inv_diagonal)

# Ejercicio 11

coin_dictionary = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
currency = input("Ingrese el nombre de una divisa: ").title()
if currency in coin_dictionary:
    print(coin_dictionary[currency])
else:
    print("La divisa no está registrada")

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



# Ejercicio 13

user = {}

# Pedir al user que ingrese su nombre, edad, dirección y teléfono

user['nombre'] = input('Ingrese su nombre: ')
user['edad'] = input('Ingrese su edad: ')
user['dirección'] = input('Ingrese su dirección: ')
user['telefono'] = input('Ingrese su número de teléfono: ')

# Mostrar la información del user por pantalla

msj = '{} tiene {} años, vive en {} y su número de teléfono es {}.'
print(msj.format(user['nombre'], user['edad'], user['dirección'], user['telefono']))



