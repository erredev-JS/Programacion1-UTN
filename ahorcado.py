import random as r

# Crear una lista de palabras para el programa.
word_list = ['java', 'spring', 'programacion', 'python', 'water']

def choose_random_word(word_list):
    # Conseguimos la palabra gracias al número aleatorio y la lista.
    return r.choice(word_list)
# Crear la máscara de guiones para luego usarla con zip.
def initialize_dash_word(word):
    return '-' * len(word)

word = choose_random_word(word_list)
dash_word = initialize_dash_word(word)

# Establecer el número máximo de intentos.
max_attempts = 3

# Contador de intentos
attempts = 0

print(f'¡Bienvenidos al juego de Ahorcado! Tienen {max_attempts} intentos posibles antes de perder')

# Iniciamos un bucle mientras la máscara contenga '-' o los intentos sean menores a max_attempts.
while '-' in dash_word and attempts < max_attempts:
    attempt = input('Ingresa tu intento: ').lower()
    if not attempt.isalpha():
        print('Error de entrada, debes ingresar un carácter válido.')
        continue
    if attempt in word:
        # Si el intento se encuentra en la palabra base, mantendremos C de WORD,
        # si no, mantendremos D de dash_word ('-') e iremos actualizando la cadena iterando en cada caracter.
        dash_word = ''.join([c if c == attempt else d for c, d in zip(word, dash_word)])
        print('Correcto! ingresaste la letra adecuada.')
        print(dash_word.capitalize())
    else:
        # Si el intento no se encuentra en la palabra, sumaremos un intento,
        # luego se lo restaremos al máximo de intentos para tener un seguimiento del programa.
        attempts += 1
        print(f'¡Incorrecto!, intentos restantes: {max_attempts - attempts}')
        print(dash_word.capitalize())

# Al terminar el bucle, cuando no hayan más guiones en la máscara, habremos encontrado la palabra y ganado el juego,
# en caso contrario habremos perdido.
if '-' not in dash_word:
    print('¡Felicidades! Has adivinado la palabra:', word.capitalize())
else:
    print('Agotaste todos tus intentos. La palabra era:', word.capitalize())
