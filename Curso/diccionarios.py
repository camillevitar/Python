#Vamos a tener dos elementos para trabajar con una coleccion
#de diccionarios, por un lado vamos a tener una llave y por
#otro lado vamos a tener un valor asociado a esa llave
#De esta forma podremos tener multiples elementos de llave/valor

#Vamos a ver como construir un diccionario en python
#Esta compuesto por llave, valor (key, value)

diccionario = {
    'IDE': 'Integrated Development Enviroment',
    'OOP': 'Objenct Oriented Programming',
    'DBMS': 'Database Managment System'
}
print(diccionario)
#largo
print(len(diccionario))
#accediendo a un elemento 
print(diccionario['IDE'])
#otra forma, mismo resultado
print(diccionario.get('IDE'))
#modificando valores
diccionario['IDE'] = 'Integrated development enviroment'
print(diccionario)
#iterar
for termino in diccionario:
    print(termino)
for termino in diccionario:
    print(diccionario[termino])
#Recuperar valores sin necesidad de utilizar la llave
for valor in diccionario.values():
    print(valor)

#Comprobar si un elemento existe
print('IDE' in diccionario)

#agregar nuevos elementos
diccionario['PK'] = 'Primary Key'
print(diccionario)

#remover elementos
diccionario.pop('DBMS')
print(diccionario)

#limpiar el diccionario
diccionario.clear()
print(diccionario)

#eliminar diccionario
del diccionario