import random
# Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:

# a)	La cantidad de valores negativos ingresados.
# b)	La cantidad de valores positivos ingresados.
# c)	La cantidad de múltiplos de 15.
# d)	El valor acumulado de los números ingresados que son pares.

def funcion_1(num):
    countNegativos=0
    countPositivos=0
    countMultiplos15=0
    sumaPares=0

    for i in range(num):
        ingreso=random.randint(-100,100)
        print(ingreso)
        if (ingreso>0):
            countPositivos+=1
        elif (ingreso<0):
            countNegativos+=1
    
        if(ingreso>15 and ingreso%15==0):
            countMultiplos15+=1
        elif (ingreso!=0 and ingreso%2==0):
            sumaPares+=ingreso
        
    print('Cantidad de numeros negativos: '+str(countNegativos))
    print('Cantidad de numeros positivos: '+str(countPositivos))
    print('Cantidad de numeros multiplos de 15: '+str(countMultiplos15))
    print('Suma de numeros pares: '+str(sumaPares))


funcion_1(10)
