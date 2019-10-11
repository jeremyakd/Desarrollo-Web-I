# Realizar un programa que imprima 25 términos de la serie 11 - 22 - 33 - 44, etc.
# (no se ingresan valores por teclado)

i=1
while (i < 26):
    print(f'Término Nº{i:<2}: {i*11:>3}')
    i += 1
