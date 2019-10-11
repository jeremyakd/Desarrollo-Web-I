# Desarrollar un programa que muestre la tabla de multiplicar de un número ingresado por teclado.

num = input('ingrese un número: ')
numlenght = len(num)
num = int(num)
for i in range(1,11):
    print(f'{num} x {i:>2} = {num*i:>{numlenght+1}}')
