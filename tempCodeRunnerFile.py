import random as r # Importo la libreria random como "r" para poder usarla en el programa

# Defino la lista de palabras que usará el programa.

word_list = ['Computadora', 'Internet', 'Python', 'Java', 'Programación']

# Guardo el numero aleatorio en una variable para facilitar la lectura del codigo y su mantenimiento.

random_number = r.randrange(0,len(word_list))

# Obtengo la palabra de entre word_list usando el numero aleatorio como indice.

word = word_list[random_number]

dash_word = ''
for l in word:
    dash_word += '-'

game_word = ''
tries = 0


word_arr = word.split()
dash_arr = dash_word.split()


while tries < 3:
    attempt = input('Ingresa una letra para que crees que está en la palabra: ')
    if attempt != 0:
        tries += 1