""" Contains utility functions to help us with computations"""


def ipow(a, b, N):
    """ Returns a raised to the power b modulo N by squaring exponentiation """
    res = 1
    while b > 0:
        if b % 2 == 1:
            res = (res * a) % N
        a = (a * a) % N
        b >>= 1
    return res % N
