import random

def count_characters(phrase_list):
    dic_letters = {}
    for sentence1 in phrase_list:
        for letter1 in sentence1:
            dic_letters[letter1] = 0


    for sentence2 in phrase_list:
        for letter2 in sentence2:
            if letter2 in dic_letters:
                dic_letters[letter2] += 1
    for clave, value in dic_letters.items():
        print(f"El carácter {clave} aparece: {value} veces.")

def prin_cards(cards):
    for i in range(len(cards)):
        print(f"{cards[i][0]} {cards[i][1]} {cards[i][2]} {cards[i][3]} {cards[i][4]} {cards[i][5]}   ")




#Coloca los símbolos en posiciones aleatoreas cada vezz que se inicia el juego
import random as ran
def posicionate_characters():
    #lista de símbolos
    char = ["♥", "♠", "♣", "♦", "♫", "۞", "§", "Ŧ", "Ʃ", "♥", "♠", "♣", "♦", "♫", "۞", "§", "Ŧ", "Ʃ"]
    #Mezcla los elementos de la lista de forma aleatoria
    ran.shuffle(char)
    cards = [[],
        [],
        []
        ]
    #Distribuye los elementos de carácteres en una matriz de 3x3
    for i, select_char in enumerate(char):
        cards[i % 3].append(select_char)
    #Devuelve la matriz 3x3 con los elementos en ella
    return cards




#comprueba que el número ingresado no esté adivinado
def comprb_valid_num(msg, numeros_correctos):
    while True:
        numero = int(input(msg))
        if numero in numeros_correctos:
            print("Ya se adivinó ese número")
        else:
            return numero




#encuentra el símbolo en la posicion pasada por el usuarioy devuelve la lista de "?" con el símbolo en su respectiva posicion
def find_card1(position, enigm, card):
    row = (position -1) // 6
    column = (position - 1) % 6
    enigm[row][column] = card[row][column]
    return enigm




#compara las posiciones ingresadas por el usuario y si son iguales muestra un mensaje y las parejas de cartas adivinadas se mostrarán el resto del juego.
def compare_cards(u_try, u_compare, enimg, card, to_convert, correct):
    row1 = (u_try -1) // 6
    column1 = (u_try - 1) % 6
    row2 = (u_compare -1) // 6
    column2 = (u_compare - 1) % 6
    if card[row1][column1] == card[row2][column2] and u_try != u_compare:
        print("\nCoincidencia!\n")
        enimg[row1][column1] = card[row1][column1]
        enimg[row2][column2] = card[row2][column2]
        to_convert[row2][column2] = "√"
        to_convert[row1][column1] = "√"
        correct = True
    else:
        print("\nNo hay coincidencia :(\n")
        enimg[row1][column1] = "?"
        enimg[row2][column2] = "?"
        correct = False
    return (enimg, to_convert, correct)

def calc_diagonal(matriz):
    matriz_rows = len(matriz)
    diag = []
    i = 0
    while i < matriz_rows:
        diag.append(matriz[i][i])
        i += 1
    return diag


#Pone en una lista la diagonal inversa de una matriz
def calc_inv_diagonal(matriz):
    inv_position = len(matriz) - 1
    i = 0
    inv_diag = []
    while inv_position > i-1:
        inv_diag.append(matriz[inv_position][inv_position])
        inv_position -= 1
    return inv_diag


def mouseGame(tiempo=0):
    opc = random.randint(1,3)
    if opc == 3:
        tiempo += 7
        return tiempo
    elif opc == 2:
            tiempo += 3
            return mouseGame(tiempo)
    elif opc == 1:
        tiempo += 5
        return mouseGame(tiempo)
