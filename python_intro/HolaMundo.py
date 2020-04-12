#!/usr/bin/env python
#_*_ coding: utf8 _*_


## Lo básico de Python

"""

print("Hola, Mundo")

### Strings
saludo = "Hola, ¿Cómo estás?"
print(type(saludo))

### Enteros
entero = 10
print(type(entero))

### Flotantes
flotante = 2.0
print(type(flotante))

### Bool
# Implica que son argumentos vacíos, por lo tanto son False
bool(0)
bool(None)
bool("")
bool([])
# Los True
bool(1)
bool("Hola")
bool([1,5,3,8])
60 < 70

### Solicitar cosas al usuario
sol = int(input("Número: "))
op = 5 * sol
print(op)

### Miniprograma
Nombre    = input("¿Cuál es tu nombre?")
Edad      = int(input("¿Cuál es su edad?"))

Edad_amor = (Edad//2)+7

if Edad_amor >= 18 and Edad < 100:
    print("La edad mínima de tu pareja debe ser: {}".format(Edad_amor))
elif Edad_amor < 18:
    print("Espera a los 21, amigo")
else:
    print("¿Ora?")

### While = bucle

Número  = int(input("Número: "))
Mensaje = input("Mensaje: ")
i = 1

while i <= Número:
    print(Mensaje)
    i = i+1

### Listas

lista = [1,2,3,7,4,0,True,False,"q","a","z"]

print(lista[0:5])

lista.pop() #Elimina el último dato
print(lista)

for l in lista: #Imprime en vertical
    print(l)

for n in range(90,100):
    lista.append(n) #.append -- añade datos a la lista

del lista[1] #Elimina el valor 2 (porque va desde 0)
print(lista)

listaa = ["h", "o", "l", "a"] #hace que se vuelva cadena de texto
lista = "".join(listaa)

### Tuplas
a = ("A", 1, 2, 3, 4, 5, "b") # Una TUPLA es como una lista pero es inmutable
print(a)

### Diccionarios
diccionario = dict(nombre="Alumno", plataforma="Pydokoro", edad=18)
#nombre sería la key y alumno el value
print(diccionario)
print(diccionario['nombre'])

a = diccionario.items()
print(a) #imprime en lista el diccionario

b = diccionario.copy()
print(b) #copia el diccionario

keys = diccionario.keys() #regresa las llaves

values = diccionario.values() #regresa los valores

#### ---- LOS DICCIONARIOS SON IMPORTANTES PARA HACKING ---- ####

for n in diccionario.keys():
    print("{} Su valor es: {}".format(n, diccionario[n]))

### List comprehesion

## %/2 == 0 --- Para saber si es par

lista = [i for i in range(0, 10000) if i%2 == 0]
print(lista)

## Así nos ahorramos a escribir cada par existente en 0 a 10000

### Crear y escribir en archivos
#w = write
archivo = open("archivo1.txt", "w")
nombre = input("Nombre: ")
pais = input("País: ")

archivo.write(nombre)
archivo.write("\n") #Salto de línea
archivo.write(pais)

archivo.close()

### Leer archivos
#r = read
archivo = open("archivo1.txt", "r")

print(archivo.readlines()) #Lo abre pero se veo feo

for l in archivo.readlines():
    print(l) #Nice :3

## Para quitar el salto de línea se usa '.split('\n')' --- se quita el "readlines" y se pone sólo "read"

### Añadir contenido a un fichero
a = append
archivo = open("archivo1.txt", "a")
ocupación = input("¿A qué te dedicas? : ")

archivo.write(ocupación)
archivo.close()
"""