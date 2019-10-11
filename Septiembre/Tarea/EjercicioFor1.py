# Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
# a) La cantidad de valores negativos ingresados.
# b) La cantidad de valores positivos ingresados.
# c) La cantidad de múltiplos de 15.
# d) El valor acumulado de los números ingresados que son pares.

import os
valores = []
for i in range(1,4):
    valores.append(int(input(f'Ingrese el valor nro {i}: ')))
print('_'*70,'\n')
input()
os.system('clear')

for idx,num in enumerate(valores,start=1):
    print(f'Posición [{idx:>2}]: {num:>6}')
print('_'*70,'\n')


positivos=0
ceros=0
negativos=0
multiplos15=0
paresacum=0
for num in valores:
    if num<0:
        negativos+=1
    if num==0:
        ceros+=1
    if num>0:
        positivos+=1
    if num%15==0:
        multiplos15+=1
    if num%2==0:
        paresacum+=num

labPositivos = 'Positivos: '
labCeros = 'Ceros: '
labNegativos = 'Negativos: '
labMultiplos15 = 'Múltiplos de 15: '
labParesAcum = 'Valor acumulado de nros pares: '
print(f'''\
a) {labNegativos:<32}{negativos:>6} 
b) {labPositivos:<32}{positivos:>6}
c) {labMultiplos15:<32}{multiplos15:>6}
d) {labParesAcum:<32}{paresacum:>6}
   {labCeros:<32}{ceros:>6} ''')

print('_'*70,'\n')