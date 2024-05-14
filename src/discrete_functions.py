import math
from helpers import comb


def bernoulli(p: float):
    if p > 1:
        raise ValueError("Probability must be >= 0 and <= 1")
    values = {}
    for x in range(2):
        values[x] = (p**x) * (1 - p) ** (1 - x)
    return values

def binomial(p: float, x: int):
    if p > 1:
        raise ValueError("Probability must be >= 0 and <= 1")
    values = {}
    for i in range(x+1):
        values[i] = comb(x, i) * (p**i) * (1 - p) ** (x - i)
    return values

def geometric(p: float, k: int):
    if p > 1:
        raise ValueError("Probability must be >= 0 and <= 1")
    values = {}
    for i in range(k+1):
        values[i] = p * (1-p) ** i
    return values

def poisson(lbda: float, x: int):
    values = {}
    for i in range(x+1):
        values[i] = (((lbda ** i) * math.exp(lbda * -1))/math.factorial(i))
    return values

