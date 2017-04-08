""" Contains utility functions to help us with computations"""
import string
from random import randint


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
    while v:
        u, v = v, u % v
    return abs(u)


def egcd(a, b):
    """ Extended GCD Algorithm"""
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def modinv(a, m):
    """ Find a^-1 mod m"""
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def generate_primes():
    """ Generates primes from 10**5 to 10**7 and returns the array """
    N = 10 ** 7 + 1
    isP = [True for i in range(N)]
    isP[0] = isP[1] = False
    primes = []
    for i in range(2, N):
        if isP[i]:
            for j in range(2 * i, N, i):
                isP[j] = False

    for j in range(10 ** 5, N):
        if isP[j]:
            primes.append(j)
    return primes


def gen_str(length):
    """ creates a random string of length len"""
    ran_str = ""
    lis = string.letters
    n = len(lis)
    for _ in range(length):
        i = randint(0, n - 1)
        ran_str += lis[i]
    return ran_str


def gen_key(key_leng):
    """ Generate a random key_leng bit string"""
    key = ""
    for j in xrange(key_leng):
        rb = randint(0, 10 ** 5) % 2
        key += str(rb)
    return key
