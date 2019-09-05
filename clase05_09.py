contador=0

for i in range (11):
    print(i)

print("**********************")

for i in range(2,11,2):
    print("El numero ",i, " es par.")
    contador+=1


print(u"el ultimo for itero", contador, " veces.")

# hacer un programa que pida 10 numeros y devuelva su suma#
suma=0
for i in range (1,11):
    num=int(input("Ingrese num"))
    suma= suma+num

print("La suma total es: ", suma)
    