# Ordenamiento de burbuja

def bubble_sort(arr: list) -> list:
  for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
      if arr[i] > arr[j]:
        # Si arr[i] es mayor que arr[j] Intercambiamos los elementos
        arr[i], arr[j] = arr[j], arr[i]
  return arr



# Ordenamiento de selección

def selection_sort(arr: list) -> list:
    n = len(arr)
    
    # Iterar a través de todos los elementos de la lista.
    for i in range(n):
        # Suponemos que el primer elemento no ordenado es el mínimo.
        min_idx = i
        
        # Comparamos el elemento actual con el mínimo encontrado hasta ahora.
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Intercambiamos el elemento mínimo con el elemento en la posición i.
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Ordenamiento de inserción

def insertion_sort(arr):
    n = len(arr)

    # Iterar a través de todos los elementos de la lista.
    for i in range(1, n):
        # Capturamos el elemento actual para compararlo e insertarlo en su posición correcta.
        current_element = arr[i]

        # Comenzamos a comparar el elemento actual con los elementos a su izquierda.
        j = i - 1
        while j >= 0 and current_element < arr[j]:
            arr[j + 1] = arr[j]  # Desplazamos los elementos mayores a la derecha.
            j -= 1

        # Insertamos el elemento actual en su posición correcta.
        arr[j + 1] = current_element
    return arr

# Ordenamiento de mezcla

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Dividimos la lista en dos mitades
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Llamada recursiva a Merge Sort para ambas mitades
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Fusionamos las dos mitades ordenadas
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Comprobamos si quedan elementos en alguna de las mitades
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

