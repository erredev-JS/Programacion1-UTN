import random
def mouseGame(tiempo=0):
    opc = random.randint(1,3)
    if opc == 3:
        tiempo += 7
        return tiempo
    elif opc == 2:
            tiempo += 3
            return mouseGame(tiempo)
    elif opc == 1:
        tiempo += 5
        return mouseGame(tiempo)
