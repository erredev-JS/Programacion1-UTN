import random as r

def choose_random_word(word_list):
    return r.choice(word_list)

def initialize_dash_word(word):
    return '-' * len(word)

def play_hangman():
    word_list = ['java', 'spring', 'programacion', 'python', 'water']
    word = choose_random_word(word_list)
    dash_word = initialize_dash_word(word)
    max_attempts = 6
    attempts = 0
    print(f'¡Bienvenidos al juego de Ahorcado! Tienes {max_attempts} intentos posibles antes de perder')

    while '-' in dash_word and attempts < max_attempts:
        attempt = input('Ingresa tu intento: ').lower()
        if not attempt.isalpha():
            print('Error de entrada, debes ingresar un carácter válido.')
            continue
        if attempt in word:
            dash_word = ''.join([c if c == attempt else d for c, d in zip(word, dash_word)])
            print('Correcto!, ingresaste la letra adecuada.')
            print(dash_word.capitalize())
        else:
            attempts += 1
            print(f'¡Incorrecto!, intentos restantes: {max_attempts - attempts}')
            print(dash_word.capitalize())

    if '-' not in dash_word:
        print('¡Felicidades! Has adivinado la palabra:', word.capitalize())
    else:
        print('Agotaste todos tus intentos. La palabra era:', word.capitalize())

if __name__ == "__main__":
    play_hangman()
