def cuadrado(lista):
    """Función que recibe una muestra de números en una lista y devuelve otra lista con sus valores al cuadrado.
Parámetros: 
- lista: Una lista de números que introducirá el usuario
- float: función que transforma la cadena en un valor numérico de tipo flotante
- a: Variable que recorre cada valor de la lista y lo eleva al cuadrado
- split: función que separa el carácter guión de la cadena de texto de la variable numeros
Salida:
Una lista con los valores elevados al cuadrado de la anterior lista.
"""
    return [a ** 2 for a in lista]
numeros = input("Introduce una lista de números separados por guiones: ")
lista = [float(a) for a in numeros.split("-")]
cuadrado(lista)
print(cuadrado(lista))