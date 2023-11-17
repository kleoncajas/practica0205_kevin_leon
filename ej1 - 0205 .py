nombre = input("¿Cuál es tu nombre? ")
def saludo(nombre):
    """Función que hace referencia a la variable nombre para posteriormente imprimir un saludo con ese nombre.
Parámetros:
- nombre: La variable que se pregunta anteriormente al usuario
Salida:
Muestra por pantalla un saludo con la variable nombre.
"""
    print("¡hola", nombre + "!")
    return
saludo(nombre)