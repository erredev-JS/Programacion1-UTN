def most(a,b):
    if(a > b):
        return a
    else:
        return b
    
def least(a,b):
    if(a < b):
        return a
    else:
        return b
    

a = int(input('Un numero: '))
b = int(input('Otro numero: '))
print(most(a - 3, least(a + 2, b - 5)))