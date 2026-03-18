"""
Archivo: calcular_promedio.py
Descripción: Calcula el promedio de una lista de números.
Autor: Angelly Rincón
Fecha: 2026
"""


def calcular_promedio(numeros):
    """
    Calcula el promedio de una lista de números.

    Args:
        numeros (list): Lista de números.

    Returns:
        float: Promedio de la lista. Retorna 0 si está vacía.
    """

    if not numeros:
        return 0

    suma_total = sum(numeros)
    cantidad = len(numeros)

    return suma_total / cantidad


if __name__ == "__main__":
    lista_numeros = [10, 20, 30, 40, 50]

    resultado = calcular_promedio(lista_numeros)

    print(f"El promedio es: {resultado}")