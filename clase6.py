contador=0

for i in  range(10):
    print (i)
print('*******************')    

for i in range(1,11):    
    print(i)
print('*******************')
for i in range(2,1,2):    
    print("el numero ",i,"es par")
    contador+=1
print("el numero",i,"es impar")  

#confeccionar un programa que pida 10 numeros y devuelva la suma

suma=0
for i in range(1,11):
    num=int(input ("ingrese numero por favor "))
    suma= suma+num
    print('*******************')
    print("la suma de los numeros es ",suma)  
