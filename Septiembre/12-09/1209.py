empleados1=() # tupla
empleados3={} # diccionario
############################################################

empleados=[] # lista <-------------- declaramos una lista


def cargar_sueldos(empleados):
    for i in range(5):
        s=int(input("Ingrese sueldo por favor: "))
        empleados.append(s)
    empleados.sort()
    calcular(empleados)

print(empleados)

def calcular(empleados):
    sum=0
    for e in empleados:
        sum=sum+e
    print("La suma de todos los sueldos es :",sum)

def ordena_lista(empleados):
    empleados.sort()
    print("Lista ordenada de forma ascendete: ")
    print(empleados)
    empleados.sort(reverse=True)
    print ("Lista ordenada de forma descentete: ")
    print(empleados)
    

cargar_sueldos(empleados)
calcular(empleados)
ordena_lista(empleados)