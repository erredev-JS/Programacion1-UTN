# Tabajo Practico n° 4 Eje 1
x = 0
while x <= 30:
    x += 1
    if x == 4 or x == 6 or x == 10:
        print('The value ' + str(x) + ' of x was skipped')
        pass
    else:
        print('The value of the loop is: '+ str(x))
    if x == 15:
        print('The execution of the loop was broken when x was ' + str(x))
        break
#Eje 2
sentence= input("Escribe una oración: ").upper()
while sentence:
  if sentence[-1]==" ":
    break
  sentence+=". "+ input("Escribe una oración: ").upper()
  print(sentence)
#Eje 3
balance = 0
logbook = "\n"
entry = "."
while entry != "":
    print("\n")
    entry = input("¿Qué operación desea realizar? \n Deposito(D) --- Retiro(R), e ingrese el monto.\n Para finalizar ingrese un espacio vacío: ")
    if entry != "":
        operation = entry[0]
        entry = entry.split()
        del entry[0]
        sum = int(entry[0])
        operation = operation.upper()
    if operation == "D":
        deposit = sum
        logbook = logbook + f"D {deposit} \n"
        balance = balance + deposit
    elif operation == "R":
        whitdrew = sum
        if balance - whitdrew < 0:
            print("Saldo insuficiente \n")
        else:
            logbook = logbook + f"R {whitdrew} \n"
            balance = balance - whitdrew
    else:
        print("Operación ingresada inválida \n")


print(f"Bitácora: \n {logbook}")


print(f"Saldo final: {balance}")
#Eje 4
numbers=[]
escape=1
number_prime=0
while escape==1:
    num=int(input('Ingresar numero:'))
    if num>=1:
        numbers.append(num)
        divisor=0
        for n in range(1,num+1):
            if num%n==0:
                divisor+=1
        if divisor==2:
            number_prime+=1
    elif num==0:
        break
    else:
        print('Ingresar numeros positivos')
   
print(f'Numero ingresados:{numbers}')
print(f'Numeros primos:{number_prime}')
#Eje 5
year= int(input("Ingresar un año:"))
for n in range(year+1):
    if year%4==0 and year%10==0 and year%100!=0:
        print(n)
#Eje 6
for i in range(1,21):
    if i % 2 != 0:
        continue
    else:
        print(i)
#Eje 7
list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,27,28,29,30,31,32,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
search= int(input("Ingrese el numero que desea buscar:"))
for i in list:
   
    if search in list:
        print("Lo encontre!")
        break
    else:
        print("El numero no esta en la lista ")
#Eje 8
print("Bienvenido al sistemas de menú interactivo")
option = 5
print("menú 1: Atencion ")
print("menú 2: Trámites ")
print("menú 3: Consultas ")
while option != 0:
    option_1 =int(input("Por favor ingrese 1(uno), para el menú 1. Ingrese 2(dos), para el menú 2. Ingrese 3(tres) para el menú 3 o ingrese 0(cero) para salir: "))
    if option_1 == 0:
        print("Usted ha ingresado 0 para salir del programa. Hasta pronto. ")
        break
    elif option_1 == 1:
        print("Usted ha ingresado 1.  Atención: ...")
    elif option_1 == 2:
        print("Usted ha ingresado 2. Trámites: ... ")
    elif option_1 == 3:
        print("Usted ha ingresado 3. Consultas: ...")
    else:
        print("La opción ingresada no corresponde, inténtelo nuevamente. ")