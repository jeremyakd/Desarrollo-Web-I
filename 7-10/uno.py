# -*- coding: utf-8 -*-

# [] => listas
l_uno = ['lunes', 'martes'] # SE PUEDEN MODIFICAR CON EL INDICE
l_uno[0] = 'PERRO'
print(l_uno)

# () => tupla

uno_pero_tupla =('lunes','martes')

#uno_pero_tupla[0] = 'jueves'  NO SE PUEDE ASIGNAR VALOR A LA TUPLA

tupla_pero_lista = list(uno_pero_tupla) # ACÁ SE CASTEA A LISTA

tupla_pero_lista[0] = 'jueves' # ACÁ SE ASIGNA VALOR

print(tupla_pero_lista)

otra= tuple(tupla_pero_lista) # Y ACÁ SE VUELVE TUPLA OTRA VEZ

print(type(otra))

# {} => DiccionarioS

uno = {
    'uno': 'lunes',
    'dos': 'martes',
    'tres':'miercoles',
    'cuatro':'jueves',
    'cinco': 'viernes',
}


print(uno.keys())
print(uno.values())

uno['cinco'] = 'domingo'


print(uno.keys())
print(uno.values())


def modifica_tupla(tupla, valor, indice):
    l=list(tupla)
    l[indice]=valor
    t=tuple(l)
    return t

print(modifica_tupla(uno_pero_tupla, 'lo cambieeee', 0))
print(type(modifica_tupla(uno_pero_tupla, 'lo cambieeee', 0)))
