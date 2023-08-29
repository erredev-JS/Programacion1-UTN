# Ejercicio 1

year_pc = int(input("Ingrese los años de su computador: "))
if year_pc <= 2:
    print("Su computador es nuevo")
else:
    print("Su computador es viejo")

#Ejercicio 2

year_pc = int(input("Ingrese los años de su computador: "))
if (year_pc <= 2) and (year_pc >= 0) :
    print("Su computador es nuevo")
elif year_pc < 0:
    print("Error de entrada ")
else:
    print("Su computador es viejo")

# Ejercicio 3

nombres = input("Ingrese ambos nombres separados: ")
nombres_separados = nombres.split(" ")
if (nombres_separados[0][0]== nombres_separados[1][0]):
  print("Hay concidencia")
else:
  print("No hay concidencia")

# Ejercicio 4
print('Partido ROJO (A) Partido VERDAD (B) Partido AZUL(C)')
voto = input("Ingrese a que candidato va a votar: ")
voto = voto.lower()
if voto == "a":
    print("Usted a votado por el partido ROJO")
elif voto == "b":
    print("Usted a votado por el partido VERDAD")
elif voto == "c":
    print("Usted a votado por el partido AZUL")
else:
    print("Opción erronea")

# Ejercicio 5

letra = input('Ingresa un caracter: \n')
vocales = ('a','e','i','o','u')
if(len(letra) > 1):
   print('Error de entrada, ingresar solo un carácter')
else:
  if(letra in vocales):
    print(f'La letra "{letra}" es una vocal')

# Ejercicio 6

año = int(input('Ingresar año:'))
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print('Año bisiesto')
else:
    print('Año no bisiesto')

# Ejercicio 7
a,b,c = int(input('Ingresar primer numero: ')), int(input('Ingresar segundo numero: ')), int(input('Ingresar tercer numero: '))
max = a
if (b > max):
  max = b
if (c > max):
 max = c

print(f"El número mas grande es {max}")

# Ejercicio 8

user = input("Ingrese su usuario: ")
password = input("Ingrese su contraseña: ")


if ((user == "Gwenevere") and (password == "excalibur")):
    print("Usuario y contraseña correctos. Puede ingresar a Camelot")
else:
    print("Acceso denegado")

# Ejercicio 9


nombre = input('Ingresa tu nombre: ')
sexo = input('Ingresa tu sexo (Masculino/Femenino): ')
if(sexo ==  'Femenino' or sexo == 'Masculino'):
   
  if((sexo == 'Femenino') and (nombre[0]< 'M') or ((sexo == 'Masculino') and (nombre[0] > 'N'))):
   print('Perteneces al grupo A')
  else:
     print('Perteneces algrupo B')
else: 
   print('Error de entrada')
   # Ejercicio 10

edad = int(input('Ingresa tu edad: '))
if(edad < 4):
   print('Entrada gratuita')
elif(edad >= 4 and edad < 18):
   print('Valor de entrada 500$')
elif(edad >= 18):
  print('Valor de entrada 1000$')
# Ejercicio 11

pregunta = input(
  '¿Quieres una pizza vegetariana[1] o no vegetariana[2]?\n (Responder [1 o 2]\n'
)

if pregunta == '1':
  print('Ingredientes vegetarianos\n [Pimiento(1) , Tofu(2)]')
  ingrediente = input('Ingresa una opcion de ingrediente:\n')
  if(ingrediente == '1'):
    ingrediente_adicional = 'Pimiemto'
    print('La pizza es vegatariana\n')
    print(f'Y sus ingredientes son Mozzarella, Tomate y {ingrediente_adicional}')
  elif(ingrediente == '2'):
    ingrediente_adicional = 'Tofu'
    print('La pizza es vegatariana\n')
    print(f'Y sus ingredientes son Mozzarella, Tomate y {ingrediente_adicional}')
elif pregunta == '2':
  print('Ingredientes no vegetarianos\n [Pepperoni(1) , Jamon(2), Salmon(3)]')
  if(pregunta == '2'):
    ingrediente = input('Ingresa una opcion de ingrediente:\n')
    if(ingrediente == '1'):
      ingrediente_adicional = 'Pepperoni'
      print('La pizza no es vegatariana\n')
      print(f'Y sus ingredientes son Mozzarella, Tomate y {ingrediente_adicional}')
    elif(ingrediente == '2'):
      ingrediente_adicional = 'Jamon'
      print('La pizza no es vegatariana\n')
      print(f'Y sus ingredientes son Mozzarella, Tomate y {ingrediente_adicional}')
    elif(ingrediente == '3'):
      ingrediente_adicional = 'Salmon'
      print('La pizza no es vegatariana\n')
      print(f'Y sus ingredientes son Mozzarella, Tomate y {ingrediente_adicional}')
else:
  print('Error de entrada')      
  
# Ejercicio 12

fecha_actual = int(input("Ingrese la fecha actual: "))
fecha_aleatoria = int(input("Ingrese una fecha aleatoria: "))
if (fecha_actual > fecha_aleatoria):
  print("Pasaron ",fecha_actual-fecha_aleatoria," años desde esa fecha")
else:
  print("Faltan",fecha_aleatoria-fecha_actual," años para esa fecha")

# Ejercicio 13

num1 = int(input('Ingresar numero: '))
num2 = int(input('Ingresar otro numero: '))

if num1 <= 0 or num2 <= 0:
    print('Se ingresaron números negativos o nulos')
else:
    if num1 > num2:
        if num1 % num2 == 0:
            print(f'{num1} es múltiplo de {num2}')
        else:
            print(f'{num1} NO es múltiplo de {num2}')
    elif num2 > num1:
        if num2 % num1 == 0:
            print(f'{num2} es múltiplo de {num1}')
        else:
            print(f'{num2} NO es múltiplo de {num1}')

# Ejercicio 14

print("Ingresar los coeficientes de una ecuacion de primer grado ax + b = 0")
a = int(input("a= "))
b = input("b= ")

if a == 0 and b != 0:
  print("No hay solución")
elif a != 0 and b == "-x":
  print("infinitas soluciones")
elif a != 0 :
  b = int(b)
  x = -b/a
  print("la solución es x= ", x)

# Ejercicio 15

import math 
operacion = input("Desea saber el area de un triangulo (t) o de un circulo (c) ").lower()  
if (operacion == "c"):
  r=int(input("Escriba el radio del circulo"))
  print("El area del circulo es de: ", math.pi*(r ** 2))
elif(operacion == "t"):
  h = int(input("Ingrese la altura del triangulo: "))
  b = int(input("Ingrese la base del triangulo: "))
  print("El area del triangulo es de: ", (b * h) / 2)
else:
    print("valor ingresado no valido ")

# Ejercicio 16

operacion = input("Ingrese la operacion que desea realizar, 1: para suma; 2: para el producto; 3: para la resta; 4: para ver la division:\n")
a = int(input("Ingrese un numero entero: "))
b = int(input("Ingrese otro valor: "))
if operacion == '1':
   print(a + b)
elif operacion == '2':
    print(a * b)
elif operacion == '3':
    print(a - b)
elif operacion == '4':
    print(a / b)
else:
   print("Error ")

# Ejercicio 17

fecha = input("Ingrese el día: ").lower()
if (fecha == "lunes"):   
 print("Feliz comienzo de Semana")
elif (fecha == "sábado") or (fecha == "domingo"):
  print("Estas en fin de semana")    
elif (fecha == "viernes"): 
  print("Feliz fin de semana")        
elif(fecha == "martes" or "miércoles" or  "jueves"):
 print("Estás a la mitad de la semana")                    
else:
  print("El día ingresado no es válido")

# Ejercicio 18

horas_trabajadas = int(input('Ingresar las horas trabajadas en el mes: '))
salario_hora = int(input('Ingresar su salario por hora: '))
if horas_trabajadas > 48:
  horas_extras = horas_trabajadas - 48
  print(f'Las horas extras trabajadas fueron: {horas_extras}')
  salario_horas_extras = (salario_hora*0.1) + salario_hora
  salario_total = (48 * salario_hora) + (horas_extras+ salario_horas_extras)
  print(f'Salario total: ${salario_total}')
else:
  print(f'No trabajo horas extras. Las horas trabajadas fueron:  {horas_trabajadas}')
salario_total=horas_trabajadas * salario_hora


# Ejercicio 19

cant_lapiz = int(input("Ingrese la cantidad de lapices a comprar: "))
precio = 60 * cant_lapiz
if cant_lapiz >= 1000:
    precio_final = precio - (precio * 0.7)
else:
    precio_final = precio


print(f"Se debe pagar ${precio_final} por los {cant_lapiz} lapices")

#Ejercio 20

nota_1 = int(input("Ingrese la primer nota en una escala del 1 al 10: "))
nota_2 = int(input("Ingrese la segunda nota en una escala del 1 al 10: "))
nota_3 =int(input("Ingrese la tercer nota en una escala del 1 al 10: "))
nota_4 = int(input("Ingrese la cuarta nota en una escala del 1 al 10: "))
promedio = ((nota_1 + nota_2 + nota_3 + nota_4) / 4)
if promedio >= 6:
    print("Aprobado ")
else:
    print("Desaprobado")