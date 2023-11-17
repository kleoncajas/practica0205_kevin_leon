def decimal_binario(decimal):
    """Función que convierte un número decimal en un número binario.
Parámetros: 
- decimal: Un número decimal
- bin: Función que transforma el número decimal en un número binario
- replace: Función con la que quito el prefijo 0b que tiene la función bin
Salida:
El número binario transformado del decimal.
"""
    return bin(decimal).replace("0b", "")
def binario_decimal(binario):
    """Función que convierte un número binario en un número decimal.
Parámetros: 
- binario: Un número binario
- int: Función que transforma el decimal a binario, poniendo entre paréntesis que la base sea 2
Salida:
El número decimal transformado del binario.
"""
    return int(binario, 2)
decimal = 10
print(decimal_binario(decimal))
print(binario_decimal(decimal_binario(decimal)))