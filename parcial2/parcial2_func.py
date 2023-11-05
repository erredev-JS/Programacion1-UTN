# Row checker

def row_check(dna_matrix: list) -> int:
    total_mutant_adn = 0  # Inicializamos el contador de secuencias mutantes
    for row in dna_matrix:
        count_equal = 1  # Inicializamos el contador de caracteres iguales a 1
        prev_element = row[0]  # Tomamos el primer elemento de la fila como referencia
        for element in row:
            if element == prev_element:
                count_equal += 1
                if count_equal == 4:
                    total_mutant_adn += 1  # Contamos la secuencia mutante
                    break
            else: 
                count_equal = 1  # Reiniciamos el contador si los caracteres son diferentes
            prev_element = element
    
    return total_mutant_adn

# Column checker

def column_check(dna_matrix: list) -> int:
    total_mutant_adn = 0  # Inicializamos el contador de secuencias mutantes
    for i in range(len(dna_matrix)):
        count_equal = 1  # Inicializamos el contador de caracteres iguales a 1
        prev_element = dna_matrix[i][0]  # Tomamos el primer elemento de la columna como referencia
        for j in range(len(dna_matrix)):
            element = dna_matrix[j][i]
            if element == prev_element:
                count_equal += 1
                if count_equal == 4:
                    total_mutant_adn += 1  # Contamos la secuencia mutante
                    break
            else:
                count_equal = 1  # Reiniciamos el contador si los caracteres son diferentes
            prev_element = element
    return total_mutant_adn

# Oblique checker

def oblique_check(dna_matrix: list) -> int:
    oblique_list = []  # Inicializamos una lista para almacenar las secuencias diagonales
    rows, columns = 6, 6

    # Verificación de diagonales hacia la derecha
    for sum_value in range(3, 2 * rows - 2):
        oblique = ""
        for row in range(max(0, sum_value - columns + 1), min(sum_value, rows - 1) + 1):
            column = sum_value - row
            oblique += dna_matrix[row][column]

        if len(oblique) >= 4:
            oblique_list.append(oblique)  # Agregamos la secuencia diagonal a la lista

    # Verificación de diagonales hacia la izquierda
    for sum_value in range(3, 2 * rows - 2):
        oblique = ""
        for row in range(max(0, sum_value - columns + 1), min(sum_value, rows - 1) + 1):
            column = columns - 1 - (sum_value - row)
            oblique += dna_matrix[row][column]

        if len(oblique) >= 4:
            oblique_list.append(oblique)  # Agregamos la secuencia diagonal a la lista
    
    return row_check(oblique_list)  # Llamamos a la función de verificación de filas para las diagonales

# Main function, is mutant()

def is_mutant() -> bool:
    print('\nLos caracteres validos para una secuencia de DNA son  ["A","T","C","G"]\n')
    valid_characters = ['A','T','C','G']
    dna_matrix = []

    while len(dna_matrix) < 6:
            valid_row = True
            dna_row = input(f'Ingresa el DNA del mutante para la fila {len(dna_matrix) + 1}, en formato "ATGCGA" o ingresa "0" para salir:\n').upper()
            print()
            if dna_row == "0":
                break
            for i in dna_row:
                if i not in valid_characters:
                    valid_row = False
            if valid_row == True and len(dna_row) == 6:
                dna_row = [i for i in dna_row]
                dna_matrix.append(dna_row)  # Agregamos la fila de ADN a la matriz
            else: 
                print('Ingresa un DNA valido, con un largo de 6 letras\n')
    
    if len(dna_matrix) > 1:
        total_mutant_adn = row_check(dna_matrix) + column_check(dna_matrix) + oblique_check(dna_matrix)
        return True if total_mutant_adn > 1 else False
    return "Gracias por usar el programa :D"
