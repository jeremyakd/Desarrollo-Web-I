"""For

Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
a)	La cantidad de valores negativos ingresados.
b)	La cantidad de valores positivos ingresados.
c)	La cantidad de múltiplos de 15.
d)	El valor acumulado de los números ingresados que son pares.

Desarrollar un programa que solicite la carga de 10 números e imprima la suma de lo últimos 5 valores 
ingresados.

Desarrollar un programa que muestre la tabla de multiplicar de un número ingresado 
por teclado.

While

Realizar un programa que imprima 25 términos de la serie 11 - 22 - 33 - 44, etc. 
(No se ingresan valores por teclado).


Mostrar los múltiplos de 8 hasta el valor 500. Debe aparecer en pantalla 8 -16 -24, etc."""
x=0
y=0
z=0
w=0
for i in range (10):
	valor= int(input("ingrese un valor entero :"))
	if valor > 0:
		x=x+1
		
	else:
		y=y+1
	resto=valor % 15 
	if resto==0:
		z=z+1
	if valor  %2==0:
		w=w+1	

    		
			
print("la cantidad de valores positivos son :",x)
print("la cantidad de valores negativos son :",y)
print("la cantidad de valores multiples de 15  son :",z)
print("la cantidad de valores pares son :",w)