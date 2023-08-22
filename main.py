dias = ['Lunes', 'Martes','Miercoles', 'Jueves', 'Viernes']


print('Ingresa datos solicitados: \n')
fecha = input('Formato día, /dd/mm: ')
dia_sem = fecha[0:fecha.find(',')]
print()

dia = fecha[fecha.find(' ')+1:fecha.find('/')]

mes = fecha[fecha.find('/') + 1:]

print(dia_sem)
print(dia)
print(mes)

if(dias.index(dia_sem) == True):
  print(dia_sem,dia,mes)
else:
  print('Error de entrada')