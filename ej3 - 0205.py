def area_circulo(r):
    """Función que calcula el área de un círculo.
Parámetros: 
- r: Un número real con el radio del círculo
Salida:
Un número real con el área de un círculo calculada multiplicando pi y el radio elevado al cuadrado.
"""
    import math
    return math.pi * r**2
area_circulo(3)
print("El área del círculo es", area_circulo(3))
def volumen_cilindro(r, h):
    """Función que calcula el volumen de un cilindro.
Parámetros: 
- r: Un número real con el radio del cilindro
- h: Un número real con la altura del cilindro
Salida:
Un número real con el volumen de un cilindro calculada multiplicando el área del círculo con la altura del cilindro.
"""
    return area_circulo(r) * h
volumen_cilindro(3, 10)
print("El volumen del cilindro es", volumen_cilindro(3, 10))