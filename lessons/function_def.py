"""An example function definition."""


def my_max(a: int, b: int) -> int:
    """Returns the largest argument."""
    if a >= b:
        return a
    else:
        return b


print(my_max(100, 500))
print(my_max(300 + 10000, 9 ** 6))