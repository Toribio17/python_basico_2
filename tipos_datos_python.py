#Datos integer: 
"""a = -2  # a es de tipo int y su valor es -1
b = a + 2  # b es de tipo int y su valor es 1
print("Resultado de la operación: ",b)"""

#Flotantes y mostrando unicamente 2 decimales
"""real = 1.3 + 2.2  # real es un float
print("Representación aproximada de 3.3: ", real)
#Esto significa que queremos que el número se redondee a un decimal
print('Real mostrando unicamente 1 cifras decimales')
print("%.1f" % real)"""

#Datos Strings 
# Es importante mencionar que en Python no existen los caracteres, Se puede simular con un string como 'a'
"""hola = 'Hola "Pythonista"'
hola_2 = 'Hola \"Pythonista\"'
hola_3 = "Hola 'Pythonista'"

print(hola)
print(hola_2)
print(hola_3)"""

#simulando caracter
#caracter_a = 'a'
#print("Printing character: ",caracter_a)

#Datos Secuencias 
#list 
list_1 = []
list_2 = list() 
lista = list()

list_1 = [1, 2, 3, 1, 5, 6, 7, 8, 9, 10]
list_2 = [3, 'a', 8, 7.2, 'hola'] 
list_3 = [1, ['a', 'e', 'i', 'o', 'u'], 8.9, 'hola']

#for index,value in enumerate(list_1):
    #print("Values from List_1: ", index, value)
    
#for value in list_2:
#    print("Values from List_2", value)
    
#for value in list_3:
#    print("Values from List_3", value)
    
#tupla
"""tupla_num = (1, 2, 3, 4, 5)
tupla = 'a', 'b', 'd','e'

for index,value, in enumerate(tupla_num):
    print("Values from tupla_3", value,index)
    
for value in tupla:
    print("Values from tupla", value)"""

#hola = (1, 2, 3, 4, 5)
#print(type(hola))

#Funcionamiento interno de for en python (iteradores)
#iterar una tupla
"""tupla = ("A", "B", "C", "D")
i = 0
while i < len(tupla):
    elemento = tupla[i]
    print("Element from tupla: ",elemento, i)  # Cuerpo del bucle "for".
    i += 1"""
    
#this will raise an error because the tuple no longer exists   
"""thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple)"""

#Convert the tuple into a list, remove "apple", and convert it back into a tuple:
"""thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)"""

    
#Dict
d = {1: 'hola', 89: 'Pythonista', 'a': 'b', 'c': 27}
d_2 = {1: 'hola', 89: 'Pythonista', 'a': 'b', 'c': 27}
d_3 = dict({'uno': 1, 'dos': 2, 'tres': 3}) 

# Recorrer los pares clave valor
#for i in d.items():
#    print("items",i)
    
#for k in d.keys():
#    print("Keys: ",k)
    
#for k in d.values():
#    print("Values: ",k)


#Iterar un dictionary (not works)
diccionario = {"a": 1, "b": 2, "c": 3}

"""i = 0
while i < len(diccionario):
    elemento = diccionario[i]
    print("Element from Dict: ",elemento)  # Cuerpo del bucle "for".
    i += 1"""

#iteranto un cojunto set (not works)
"""conjunto = {"A", "B", "C", "D"}
i = 0
while i < len(conjunto):
    elemento = conjunto[i]
    print("Element from set: ",elemento)  # Cuerpo del bucle "for".
    i += 1"""

    
contenedor = ["A", "B", "C", "D"]
# Obtener un iterador para este contenedor.
iterador_contenedor = iter(contenedor)
print(type(iterador_contenedor))
while True:
    try:
        elemento = next(iterador_contenedor)
    except StopIteration:
        break
    print("Element with for next: ",elemento)  # Cuerpo del bucle "for"."""

#el ccodigo anterior es igual a : 
lista = ["A", "B", "C", "D"]
for elemento in lista:
    print("Element with for: ",elemento)
    
#
lista = ["A", "B", "C", "D"]
diccionario = {"a": 1, "b": 2, "c": 3}
conjunto = {"A", "B", "C", "D"}
rango = list(range(1, 13))
print(rango)


#<list_iterator object at 0x000001A0913B9700>
print(iter(diccionario))
#<dict_keyiterator object at 0x000001A091411DB0>
print(iter(conjunto))
#<set_iterator object at 0x000001A091418340>
print(iter(rango))
#<range_iterator object at 0x000001A090A589D0>




