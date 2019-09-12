"""Desarrollar un programa que solicite la carga de 10 números e imprima la suma de 
o últimos 5 valores ingresados."""

x=0
suma=0

for i in range(10):
	x=x+1
	numero=int(input("ingrese un número :"))
	if x>5:
		suma=suma+numero 
print("la suma de los ultimos 5 valores ingresados es: ",suma)
			
