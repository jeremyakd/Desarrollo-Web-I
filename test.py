import random
print("\nEjercicio E:")
suma=0
lista =[]
​
for i in range(10):
    num=random.randint(0,100)
    print("numero generado: ", num)
    lista.append(num)
​
​
for i in range(10):
    if (i>4):
        suma+= lista[i]
print("La suma de las ultimas 5 cifras es: ",suma)
​
print("Lista completa \n ", lista)