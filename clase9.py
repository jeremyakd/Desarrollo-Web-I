# contador=0 

# for i in range(1,11,2):
#     print(i)
#     contador+=1

# print(u"el ultimo for iteró", contador, "veces.")    

# confeccionar un programa que pida 10 numeros y devuelva su suma
suma = 0

for i in range(1,11):
    num = int(input(f"ingrese el num {i}: "))
    suma = suma + num
print("La suma de los numeros ingresados es: ", suma)    