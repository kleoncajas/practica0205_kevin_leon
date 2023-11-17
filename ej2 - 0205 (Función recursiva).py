numero = int(input("Introduce un número entero positivo: "))
def factorial(numero):
    """Función que recibe un número entero y muestra por pantalla su factorial
Parámetros:
- numero: La variable del número que se pregunta anteriormente al usuario
Salida:
Muestra por pantalla el factorial del número escrito.
"""
    while numero == 0:
        return 1 
    else:
        return numero * factorial(numero-1)
print(factorial(numero))