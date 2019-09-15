num1 = int(input("ingrese primer numero por favor: "))
num2 = int(input("ingrese segundo numero por favor: "))
print ('la suma es', num1+num2)  #el if  no lleva parentesis ni llaves

if num1 > num2:
   print('el primer numero es mayor')
else:
   print('el segundo numero es mayor')  


dia = int(input("ingrese dia  por favor: "))

if dia == 1:
        print("el dia elegido es lunes")
elif dia == 2:
        print("el dia elegido es Martes")
elif dia == 3:
        print("el dia elegido es Miercoles")
elif dia == 4:
        print("el dia elegido es Jueves")
elif dia == 5:
        print("el dia elegido es Viernes")
elif dia == 6:
        print("el dia elegido es Sabado")
elif dia == 7:
        print("el dia elegido es Domingo")
else:
        print("no corresponde a ningun dia de la semana.")      


