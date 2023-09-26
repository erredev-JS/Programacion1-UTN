import random as r
word_list = ['java', 'spring', 'programacion', 'python', 'water'] # Crear una lista de palabras para el programa.

random_num = r.randrange(0,len(word_list)) # Obtenemos un numero aleatorio en base al largo de la lista, guardandolo en una variable para no tener magic strings.

word = word_list[random_num] # Conseguimos la palabra gracias al numero aleatorio y la lista.

dash_word = '-' * len(word) # Crear la mascara de guiones para luego usarla con zip


max_attempts = 3  # Establecer el número máximo de intentos

attempts = 0 # Contador de intentos
print(f'¡Bienvenidos al juego de Ahorcado! Tienen {max_attempts} intentos posibles antes de perder')

while '-' in dash_word and attempts < max_attempts: # Iniciamos un bucle mientras la mascara contenga '-' o los intentos sean menores a max_attempts
    attempt = input('Ingresa tu intento: ').lower()
    if  not attempt.isalpha():
        print('Error de entrada, debes ingresar un caracter valido.')
        continue
    if attempt in word: # Si el intento se encuentra en la palabra base, mantendremos C de WORD, si no, mantendremos D de dash_word ('-') e iremos actualizando la cadena iterando en cada caracter.
        dash_word = ''.join([c if c == attempt else d for c, d in zip(word, dash_word)])
        print('Correcto! ingresaste la letra adecuada.')
        print(dash_word.capitalize())
    else: # Si el intento no se encuentra en la palabra, Sumaremos un intento, luego se lo restaremos a el maximo de intentos para tener un seguimiento del programa.
        attempts += 1
        print(f'Intentos restantes: {max_attempts - attempts}')
        print(dash_word.capitalize())


if '-' not in dash_word: # Al terminar el bucle, cuando no hayan mas guiones en la mascara, habremos encontrado la palabra y ganado el juego, en caso contrario habremos perdido.
    print('¡Felicidades! Has adivinado la palabra:', word.capitalize())
else:
    print('Agotaste todos tus intentos. La palabra era:', word.capitalize())