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
n = 1
par = 0
inpar = 0
while n != 0:
  n = int(input('Ingresa un numero entero positivo: '))
  if(n < 0):
      print('Recuerda ingresar un numero entero positivo!')
  elif(n % 2 == 0 and n != 0):
      par += 1
  elif(n % 1 == 0 and n != 0):
      inpar += 1
print(f'Ingresaste 0, los numeros pares ingresados fueron {par} y los numeros inpares fueron {inpar}')