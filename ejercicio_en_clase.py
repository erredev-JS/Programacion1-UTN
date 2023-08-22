
# Retocar, no funciona

print('Ingresa datos solicitados: \n')
fecha = input('Formato día, /dd/mm: ')
dia_sem = fecha[0:fecha.find(',')]
dia_sem = dia_sem.lower()
print()

dia = int(fecha[fecha.find(' ')+1:fecha.find('/')])

mes = int(fecha[fecha.find('/') + 1:])
print(dia_sem)

if((dia_sem == 'lunes' or dia_sem == 'martes' or dia_sem == 'miercoles' or dia_sem == 'jueves' or dia_sem == 'viernes')and ((dia < 31 and dia < 0) and (mes > 0 and mes < 12))):
  print(dia_sem,dia,mes )
else:
  print('Error de entrada')
