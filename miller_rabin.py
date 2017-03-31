""" Contains Miller rabin primality test"""
import random
from util_functions import ipow


class MillerRabin:
    """ The class that provides functionality of Miller Rabin testing"""

    def __init__(self, n):
        """ Default Constructor"""
        self.n = n
        pass

    def is_prime(self, n, t):
        """
        Outputs whether given number is miller rabin prime or not
        :param n: Number to be tested
        :param t: Number of iterations
        :return: True if n is probably prime else False
        """
        if n < 2 or (n > 2 and n % 2 == 0):
            return False
        for i in range(t):
            a = random.randint(2, n - 2)
            if is_witness(a, n): return False
        return True

    def find_next_greatest_prime(self, n, t):
        """
        Given a number outputs a prime greater than equal to n
        :param n:
        :return: an integer p such that p is prime and p >= n
        """
        if n % 2 == 0:
            n += 1
        while not self.is_prime(n, t):
            n += 2
        return n

    def find_witness_liars(self):
        """ Find Strong Witnessess and Liars of the given n"""
        n = self.n
        liars = []
        witnesses = []
        for a in range(2, n - 2):
            if is_liar(a, n):
                liars.append(a)
            elif is_witness(a, n):
                witnesses.append(a)
        return liars, witnesses


# Auxillary Functions to Assist

def is_witness(a, n):
    q = n - 1
    k = 0
    while q % 2 == 0:
        q /= 2
        k += 1
    b = ipow(long(a), long(q), n)
    if b == 1: return False
    for i in range(k):
        if b == n - 1: return False
        b = (b * b) % n
    return True


def is_liar(a, n):
    q = n - 1
    k = 0
    while q % 2 == 0:
        q /= 2
        k += 1
    b = ipow(long(a), long(q), n)
    for i in range(k):
        if i != 0 and b != n - 1: return False
        b = (b * b) % n
    return True
