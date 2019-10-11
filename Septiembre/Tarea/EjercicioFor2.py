# Desarrollar un programa que solicite la carga de 10 números e imprima
# la suma de los últimos 5 valores ingresados.

lista =[]
acum=0
print('Ingrese 10 números')
for i in range(1,11):
    lista.append(int(input(f'Ingrese el valor nro {i}: \t')))
    if i>5:
        acum+=lista[i-1]
    
print(f'''
La suma de los 5 últimos valores ingresados es {acum}.
''')