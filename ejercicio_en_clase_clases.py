# Create a Motorcycle with classes.

class Motorcycle:
    state = 'New'
    def __init__(self, color = '', matricula = '', combustible_litros = 0, numero_ruedas = 0, marca = '', modelo = '', fecha_fabricacion = 0, velocidad_punta = 0, peso = 0, motor = False) -> None:
        self.color = color
        self.matricula = matricula
        self.combustible_litros = combustible_litros
        self.numero_ruedas = numero_ruedas
        self.marca = marca
        self.modelo = modelo
        self.fecha_fabricacion = fecha_fabricacion
        self.velocidad_punta = velocidad_punta
        self.peso = peso
        self.motor = motor
    def start(self):
        if self.motor == False:
            print('El motor ha arrancado')
            self.motor = True
        elif self.motor == True:
            print('El motor ya esta en marcha')

    def stop(self):
        if self.motor == True:
            print('El motor se ha detenido')
        elif self.motor == False:
            print('El motor ya estaba detenido')
    def show_price(self, precio):
        print(f"El precio de {self.marca} es ${precio}")



moto_test = Motorcycle('','',10,'2','','','','','',False)
moto_test2 = Motorcycle('','',10,'2','','','','','',False)
moto_test.start()
moto_test.start()
moto_test.stop()
moto_test.stop()
moto_test2.price = 500
print(f'El precio de la motocicleta 2 es {moto_test2.price}')
moto_test2.show_price(20)
moto_test.show_price(20)