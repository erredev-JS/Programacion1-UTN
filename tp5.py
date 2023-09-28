def space_between_letters(word):
    spaced_word = ''.join([c + ' ' for c in word if c != ' '])
    return spaced_word

print(space_between_letters('Hola, tú'))