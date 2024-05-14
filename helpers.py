import math


def comb(x: int, k: int) -> float:
    """Returns the binomial coefficient of x and k"""
    return math.factorial(x) / (math.factorial(k) * math.factorial(x - k))
