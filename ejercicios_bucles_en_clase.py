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
digitos_pares_totales = 0
digitos_impares_totales = 0

while True:
    num = int(input("Ingresa un número entero positivo (ingresa 0 para terminar): "))
    
    if num == 0:
        break
    
    pares = 0
    impares = 0
    numero = num
    
    while numero > 0:
        digito = numero % 10
        if digito % 2 == 0:
            pares += 1
        else:
            impares += 1
        numero //= 10
    
    digitos_pares_totales += pares
    digitos_impares_totales += impares
    
    print(f"El número {num} tiene {pares} dígitos pares y {impares} dígitos impares.")

print(f"Total de dígitos pares: {digitos_pares_totales}")
print(f"Total de dígitos impares: {digitos_impares_totales}")
