# Desarrollar un programa que solicite la carga de 10 n�meros e imprima la suma de lo �ltimos 5 valores ingresados.

suma=0

for i in range(10):
    num = int(input('Ingrese el '+str(i+1)+'° numero: '))
    if(i>4):
        suma+=num

print('la suma de los ultimos 5 numeros es: '+str(suma))