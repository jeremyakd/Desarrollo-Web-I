# Mostrar los múltiplos de 8 hasta el valor de 500. Debe aparecer en pantalla 8 - 16 - 24, etc.

multiplo = 1
while (True):
    if multiplo * 8 < 500:
        print(f'8 x {multiplo:<2}: {multiplo*8}')
    else:
        break
    multiplo += 1