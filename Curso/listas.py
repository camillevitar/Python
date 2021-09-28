#lista almacenada en una variable
nombres = ['Juan', 'Maria', 'Karla', 'Ricardo']
print(nombres)
#conocer el largo de la lista
print(len(nombres))
#acceder solo a un elemento de la lista dando el indice
print(nombres[0])
print(nombres[1])
#Navegacion inversa utilizando indices negativos (ultimos valores)
print(nombres[-1])
print(nombres[-2])
#imprimir rango sin incluir el indice 2
print(nombres[0:2])
#imprimir los elementos de inicio hasta el indice proporcionado sin incluir el 3
print(nombres[:3])
#imprimir los elementos hasta el final desde el indice proporcionado 
print(nombres[1:])
#Cambiar los elementos de una lista
nombres[3] = 'Maria'
#iterar la lista
for nombre in nombres:
    print(nombre)
#revisar si existe un elemento dentro de la lista
if 'Maria' in nombres:
    print('Maria si existe en la lista')
else:
    print('El elemento buscado no existe en la lista')
#Agregar un nuevo elemento a la lista con la funcion append
nombres.append('Camille')
print(nombres)
#Insertar nuevo elelemnto en el indice proporcionado
nombres.insert(1, 'Octavio')
print(nombres)
#remover elemento de nuestra lista
nombres.remove('Octavio')
print(nombres)
#Remover el ultimo elemento de la lista
nombres.pop()
print(nombres)
#remover el indice indicado de la lista
del nombres[0]
print(nombres)
#limpiar todos los elementos de nuestra lista
nombres.clear()
print(nombres)
#eliminar la lista y la variable
del nombres
print(nombres)