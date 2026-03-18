def filter_even_numbers(numbers):
    """
    Filtra y devuelve solo los numeros pares de una lista.

    Args:
        numbers (list): Lista de numeros enteros.

    Returns:
        list: Lista con los numeros pares.
    """
    even_numbers = []

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)

    return even_numbers


# Prueba de la funcion
example_list = [1, 2, 3, 4, 5, 6]
result = filter_even_numbers(example_list)

print("Números pares:", result)