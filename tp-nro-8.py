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
