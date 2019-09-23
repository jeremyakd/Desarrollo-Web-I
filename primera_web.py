""" num1 = int(input('Ingrese numero: '))
num2 = int(input('Ingrese otro numero: '))

print('La suma es: ',num1+num2)

if num1 > num2:
    print('El primer numero mayor')
else:
    print('El segundo numero mayor')
 """

 
diaDeLaSemana = input('Ingrese un dia de la semana: ')

if diaDeLaSemana == 'lunes':
    print('Es el primer dia de la semana')
elif diaDeLaSemana == 'martes':
    print('Es el segundo dia de la semana')
elif diaDeLaSemana == 'miercoles':
    print('Es el tercer dia de la semana')
elif diaDeLaSemana == 'jueves':
    print('Es el cuarto dia de la semana')
elif diaDeLaSemana == 'viernes':
    print('Es el quinto dia de la semana')
elif diaDeLaSemana == 'sabado':
    print('Es el sexto dia de la semana')
elif diaDeLaSemana == 'domingo':
    print('Es el septimo dia de la semana')
else:
    print('Introduzca un dia valido')