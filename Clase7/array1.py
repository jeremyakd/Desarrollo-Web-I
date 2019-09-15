empleados=[]  #lista
empleados1=() # tupla
empleados3={} # diccionario

def cargar_sueldos(empleados):
    for i in range(5):
        s=int(input("ingrese sueldo por favor"))
        empleados.append(s)
    calcular(empleados)

print(empleados)    
  

def calcular(empleados):
        sum=0
        
        for e in empleados:
            sum=sum+e
        print("la suma de todos los empleados es:",sum)
             
cargar_sueldos(empleados)

