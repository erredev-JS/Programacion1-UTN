# Ejercicio 1

abc = 'abcdefghijklmnñopqrstuvwxyz'
corrimiento = int(input('Ingresa cuantos caracteres a la derecha quieres para la encriptación Cesar: '))
for i in range(5):
  msj = input('Ingresa tu mensaje ').lower()

  msj_encriptado = ''
  for letra in msj:
    if letra in abc:
      indice = abc.find(letra)
      indice = (indice + corrimiento) % len(abc)
      msj_encriptado += abc[indice]
    elif letra == ' ':
        msj_encriptado += ' '
     
  print(f'El mensaje encriptado {i + 1} es: {msj_encriptado}')
     
else:
      print(f' El mensaje encriptado es: {msj_encriptado}')

# Ejercicio 2
n = int(input('Ingresa un numero entero positivo: '))
num_str = str(n)
par_count = 0
impar_count = 0

for char in num_str:
    digit = int(char)
    resto = digit % 2
    if resto == 0:
        print(f'El dígito {digit} es par.')
        par_count += 1
    else:
        print(f'El dígito {digit} es impar.')
        impar_count += 1

print(f'En el número {n}, hay {par_count} dígitos pares y {impar_count} dígitos impares.')

