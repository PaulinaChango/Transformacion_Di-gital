"""
Módulo para calcular promedios de listas numéricas.
Este script forma parte del repositorio Transformacion_Digital.
"""

def calcular_promedio(numeros):
    """
    Calcula el promedio de una lista de números.

    Parámetros:
    numeros (list of float/int): Lista con valores numéricos.

    Retorna:
    float: Promedio de los números. Si la lista está vacía, retorna 0.0.

    Ejemplo:
    >>> calcular_promedio([4, 8, 6])
    6.0

    >>> calcular_promedio([])
    0.0
    """
    if not numeros:
        return 0.0
    return sum(numeros) / len(numeros)


# Ejemplo de uso (esto solo se ejecuta si corres el script directamente)
if __name__ == "__main__":
    prueba = [10, 20, 30, 40, 50]
    resultado = calcular_promedio(prueba)
    print(f"Lista: {prueba}")
    print(f"Promedio: {resultado}")