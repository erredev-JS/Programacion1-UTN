# Ejercicio 1

def count_digits(n, digits):
    s = str(n)
    if len(s) <= 1:
        return digits
    else:
        digits += 1
        return count_digits(s[:-1], digits)
   

digit = 1
num = int(input("Ingrese un número: "))
print(count_digits(num, digit))

# Ejercicio 2

def potencia1(n,b):
    if (n == 0):
        return True
    elif (n < 0):
        return False
    else:
        #aca va a hacer la recursion de n restandole b hasta llegar a 0. Si llega a cero es potencia, y si no llega a cero, no es potencia.
        return potencia1(n - b, b)






print("Bienvenido: ")
print("Para saber si un número entero [n] es potencia de otro número entero [b]")
n = int(input("Por favor ingrese un número entero para [n]: "))
b = int(input("Por favor ingrese otro número entero para [b]: "))
potency = potencia1(n,b)
if potency == True:
    print(f"El número {n} es potencia de {b}")
else:
        print(f"El número {n} no es potencia de {b}")


# Ejercicio 3

def string_position(a, b, start = 0):
    count = []
    index = a.find(b, start)
    if index != -1:
        count.append(index)
        count += string_position(a, b, index + 1)
    return count

print(string_position("pablito clavó un clavito, cuantos clavitos clavó pablito", "ito"))

# Ejercicio 4
# Funciones
def par(n):
    if n == 1:
        return False
    else:
        return impar(n-1)
   




def impar(n):
    if n == 1:
        return True
    else:
        return par(n-1)


# Codigo principal


print("Bienvenido: por favor ingrese una opición: ")
while True:
    option = input("Ingrese [1] para saber de forma recursiva  si un número es par o ingrese [2] para saber si un número es impar: ")
    try:
        if (option.isdigit()) and (option == "1" or option == "2"):
            option =  int(option)
           
            if option == 1:
                print("Usted seleccionó par. ")
            else:
                print("Usted seleccionó impar. ")
            n = int(input("Ingrese un número natural: "))
            if n > 0:
                break
            else:
                print("Datos ingresados incorrectos. Reintente. ")
    except:
        print("Debe ingresados incorrectos. Reintente.  ")

if option == 1:
    print(f"¿El número {n} es par? {par(n)}")
elif option == 2:
    print(f"¿El número {n} es impar? {impar(n)}")

# Ejercicio 5

# Funciones

def found_bigest(nums, mayor = None, i = 0):
    if i == len(nums):
        return mayor
    else:
        if mayor is None or nums[i] > mayor:
            mayor = nums[i]
    return found_bigest(nums, mayor, i+1 )

# Codigo principal

nums = [5,2,4444,7,19,4449,100,15,64,69]
big = found_bigest(nums)
print(big)

# Ejercicio 6

# Funciones

def repli(nums, n, index = 0):
    if index == (len(nums)):
        return []


    num_list = []
    for i in range(n):
        num_list.append(nums[index])
       
    return num_list + repli(nums, n, index + 1 )

# Codigo principal

replic_list = repli([1,3,3,7], 4)
print(replic_list)

# Ejercicio 7

# Funciones

def period_sum(n,p):
    if n == 1:
        return n
    else:
        k = n * p + period_sum(n-1,p)
        return k

# Codigo principal

n = int(input("Ingrese el valor de n: "))
p = int(input("Ingrese el valor de p: "))


result = period_sum(n,p)


print(f"El resultado de K({n},{p}) es: {result}")

# Ejercicio 8

# Funciones

def period_sum(n,p):
    if n == 1:
        return n
    else:
        k = n * p + period_sum(n-1,p)
        return k

# Codigo principal

n = int(input("Ingrese la fila:  "))
k = int(input("Ingrese la columna: "))

num = period_sum(n,k)
print(num)

# Ejercicio 9

def combinations_helper(characters, k, current_combination, result):
    if len(current_combination) == k:
        result.append(current_combination)
        return
    
    if len(current_combination) > k:
        return  # Salir si la combinación actual supera la longitud máxima
    
    for char in characters:
        # Evita caracteres repetidos en la combinación
        if char not in current_combination:
            new_combination = current_combination + char
            combinations_helper(characters, k, new_combination, result)

def combinations(characters, k):
    if len(set(characters)) < len(characters):
        return 'La lista no puede contener caracteres repetidos'
    
    result = []
    combinations_helper(characters, k, "", result)
    return result


print(combinations(['a', 'b', 'c'], 1))

# Ejercicio 10

def calc_size(n, base = [841, 1189]):
    if n == 0:
        if base[0] > base[1]:
            base[0], base[1] = base[1], base[0]
        return tuple(base)
    else:
        if n % 2 == 0:
            base[0] = base[0]//2
        else:
            base[1] = base[1]//2
        return calc_size(n - 1, base)


size = int(input("Ingrese la medida de la hoja A(N): "))
print(f"El tamaño de la hoja A{size} es :")
final_size = calc_size(size)
print(f"{final_size[0]}mm x {final_size[1]}mm")

