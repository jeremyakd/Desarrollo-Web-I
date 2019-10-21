contador=0

for i in range(10):
    print(i)

print("**********************************************")

for i in range(1,11):
    print(i)

print("**********************************************")

for i in range(3,12,2):
    print("El numero ",i, " es par.")
    contador+=1
print(u"el ultimo for iteró", contador, "veces.")


# confeccioner un programa que pida 10 numeros y devuelva su suma.

suma=0
for i in range(1,11):
    num=int(input(str(i)+ "- Ingrese un numero por favor: "))
    suma=suma+num

print("la suma total es:", suma)