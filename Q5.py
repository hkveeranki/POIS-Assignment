""" Contains Baby step Giant step algorithm to solve discrete log problem"""
import random
from math import ceil, sqrt

from Q3 import MillerRabin
from util_functions import ipow


def hack(p, g, h):
    """
    tries to solve discrete log problem
    :param h: value need to be hacked
    :param g: generator of the group
    :param p: prime
    :return: x such that g^x mod p = h
    """
    if h > p - 1 or h < 1:
        raise ValueError('h doesnt belong to the group')

    m = int(ceil(sqrt(p)))
    vals = {}
    s = 1
    for i in range(m):
        vals[i] = s
        s = (s * g) % p
    invg = ipow(g, p - 2, p)
    invm = ipow(invg, m, p)
    beta = h
    for i in range(m):
        if beta in vals.values():
            j = 0
            for key in vals.keys():
                if vals[key] == beta:
                    j = key
                    break
            return i * m + j
        beta = (beta * invm) % p


valid_gens = [2, 3, 5, 6, 7, 11]


def check_gen(n, g):
    val = g
    ind = 1
    thresh = pow(10, len(str(n)) - 1)
    while ind < n:
        ind += 1
        val = (val * g) % n
        if val == 1 and ind != n - 1:
            return False
    return True


def generate_prime():
    """ Generates primes from 10**5 to 10**7 and returns the array """
    tester = MillerRabin(221)
    while True:
        p = random.randint(10 ** 6, 10 ** 7)
        if tester.is_prime(p, 10):
            return p


if __name__ == "__main__":
    p = generate_prime()
    print "Prime is", p
    g = 2
    for i in range(len(valid_gens)):
        if check_gen(p, valid_gens[i]):
            g = valid_gens[i]
            break
    print "g is", g
    x = random.randint(1, 2 ** 40) % p
    print "x =", x, "hack =", hack(p, g, ipow(g, x, p))
