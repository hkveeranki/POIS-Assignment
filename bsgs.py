""" Contains Baby step Giant step algorithm to solve discrete log problem"""
import random
from math import ceil, sqrt

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

    m = ceil(sqrt(p))
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


if __name__ == "__main__":
    p = 37
    g = 5
    x = random.randint(1, 2 ** 40) % p - 1
    print("x =", x, "hack =", hack(g, ipow(g, x, p), p))
