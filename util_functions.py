""" Contains utility functions to help us with computations"""


def ipow(a, b, N):
    """ Returns a raised to the power b modulo N by squaring exponentiation """
    res = 1
    b = int(b)
    while b > 0:
        if b % 2 == 1:
            res = (res * a) % N
        a = (a * a) % N
        b >>= 1
    return res % N


def gcd(u, v):
    """ Returns gcd of two numbers """
    while v:
        u, v = v, u % v
    return abs(u)
