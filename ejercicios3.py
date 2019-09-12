#Desarrollar un programa que muestre la tabla de multiplicar de un número ingresado 
#por teclado.


x=0
multiplo=int(input("ingrese un  valor para ver su tabla de multiplicar : "))
for i in range(10):
	x=x+1
	print(multiplo," x ",x," es igual a : ",(x*multiplo))