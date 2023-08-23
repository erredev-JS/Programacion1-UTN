dias = ('Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes')

print('Ingresa datos solicitados:\n')

fecha = input('Formato día, /dd/mm: ')

dia_sem = fecha[0:fecha.find(',')].capitalize()

dia = int(fecha[fecha.find('/') + 1:fecha.find('/', fecha.find('/') + 1)])
mes = int(fecha[fecha.rfind('/') + 1:])

if (dia_sem in dias) and ((dia > 0 and dia <= 31) and (mes > 0 and mes <= 12)):
  if(dia_sem == 'Lunes' or dia_sem == 'Martes' or dia_sem == 'Miercoles'):
      examenes = input('Hoy se tomaron los examenes?: \n (Responder "Si o No")\n')
      if(examenes == 'Si'):
         aprobaron =  int(input('Cuantos estudiantes aprobaron?:\n'))      
         desaprobaron = int(input('Cuantos estudiantes no aprobaron?:\n'))
         total_alumnos = aprobaron + desaprobaron
         porcentaje_aprobados = (aprobaron / total_alumnos) * 100
         print(f'El porcentaje de alumnos aprobados es {porcentaje_aprobados}%')
  elif(dia_sem == 'Jueves'):
      porcentaje_asistencia = float(input('Ingresa el porcentaje de asistencia a clase sin el "%":\n'))  
      if(porcentaje_asistencia > 50):
          print('Asistio la mayoria')
      else:
          print('No asistio la mayoria')     
  elif(dia_sem == 'Viernes'):
      if(dia == 1 and(mes == 1 or mes == 7)):
          print('Comienzo de nuevo ciclo\n')
          cantidad_alumnos = int(input('Ingresar cantidad de alumnos del nuevo ciclo:\n'))       
          monto_arancel = float(input('Ingresar cantidad de alumnos del nuevo ciclo:\n'))
          ingreso_total = monto_arancel * cantidad_alumnos
          print(f'El ingreso total es de ${ingreso_total}')       
else:
      print('Error de entrada')
