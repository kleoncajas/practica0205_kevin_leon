def media(lista):
    """Función que recibe una muestra de números en una lista y muestra su media.
Parámetros: 
- lista: Una lista de números que introducirá el usuario
- sum: función que suma en este caso los valores de la lista
- len: función que muestra los valores o el número de números que hay dentro de la lista
- float: función que transforma la cadena en un valor numérico de tipo flotante
- a: Es la variable que recorre el bucle y asigna cada número a la función float
- split: función que separa el carácter guión de la cadena de texto de la variable numeros
Salida:
La media de la lista de números introducida.
"""
    return sum(lista) / len(lista)
numeros = input("Introduce una lista de números separados por guiones: ")
lista = [float(a) for a in numeros.split("-")]
media(lista)
print(media(lista))