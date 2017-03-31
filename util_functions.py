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


def gcd(u, v):
    """ Returns gcd of two numbers """
    while v:
        u, v = v, u % v
    return abs(u)


def factorise(n):
    """ Factorises N in to s*2^r"""
    s = n
    r = 0
    while s % 2 == 0:
        r += 1
        s /= 2
    return long(s), int(r)
