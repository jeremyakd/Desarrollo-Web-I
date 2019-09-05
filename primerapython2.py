""" num1 = int(input('ingrese numero: '))
num2 = int(input('ingrese numero: '))
num3
print('la suma es: ', num1+num2) """
#la condicion el if va sin parentesis
condition=True
#ojo el True de Python es con mayuscula
dia=raw_input('Ingrese dia de la semana por favor: ')
while condition:
    if dia=='lunes':
        print('in english is Monday')
        break
        dia=False
    elif dia=='martes':
        print('in english is Tuesday')
        break
        dia=False
    elif dia=='miercoles':
        print('in english is Wednesday')
        break
        dia=False
    elif dia=='jueves':
        print('in english is Thursday')
        break
        dia=False
    elif dia=='viernes':
        print('in english is Friday')
        break
        dia=False
    elif dia=='sabado':
        print('in english is Saturday')
        break
        dia=False
    elif dia=='domingo':
        print('in english is Sunday')
        break
        dia=False
    else:
        print('Not a day')
        dia=input('Ingrese dia de la semana por favor: ')

""" dia=input('Ingrese dia de la semana por favor: ')

if dia=='lunes':
    print('in english is Monday')
elif dia=='martes':
    print('in english is Tuesday')
elif dia=='miercoles':
    print('in english is Wednesday')
elif dia=='jueves':
    print('in english is Thursday')
elif dia=='viernes':
    print('in english is Friday')
elif dia=='sabado':
    print('in english is Saturday')
elif dia=='domingo':
    print('in english is Sunday')
else:
    print('Not a day') """