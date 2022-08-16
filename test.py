# This is a test file for the project.

# function to swap two numbers without using a temporary variable
def swap(a, b) -> int:
    """
    Swap two numbers without using a temporary variable.
    :param a: first number
    :param b: second number
    """
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b

