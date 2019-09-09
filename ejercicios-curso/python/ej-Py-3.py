# Desarrollar un programa que muestre la tabla de multiplicar de un n�mero ingresado po4 teclado.

num=int(input('Ingrese un número para obtener su tabla: '))
for i in range(1,11):
    producto=num*i
    print(str(num)+'x'+str(i)+'='+str(producto))