def add(a, b):
    """Thats the beauty of DOC STRINGS."""
    return a + b


print(add.__doc__)  # Output: Returns the sum of two numbers.


def add(a, b):
    """
    Returns the sum of two numbers.

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The sum of the two numbers.
    """
    return a + b
print(add.__doc__) 
