import random


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


class MillerRabin:
    """ The class that provides functionality of Miller Rabin testing"""

    def __init__(self):
        """ Default Constructor"""
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

        r, u = self.__factor(n - 1)
        pow_needed = []
        s = u
        power = 1

        for i in range(r):
            pow_needed.append(int(s * power))
            power *= 2

        for i in range(t):
            a = random.randint(1, n - 1)
            lis = []
            for j in range(r):
                lis.append(ipow(a, pow_needed[j], n))
            fl = 1
            if lis[0] == 1 or lis[0] == n - 1:
                fl = 0
            for j in range(1, r):
                if lis[j] == n - 1:
                    fl = 0
            if fl == 1:
                print('Came false for ', a)
                return False
        return True

    def find_next_greatest_prime(self, n):
        """
        Given a number outputs a prime greater than equal to n
        :param n:
        :return: an integer p such that p is prime and p >= n
        """
        p = n
        return p

    def find_witness_liars(self):
        """ Find Strong Witnessess and Liar"""
        pass

    def __factor(self, n):
        """
        Given an N factorise into u*2^r
        :param n:
        :return: return r,u
        """
        u = n
        r = 0
        while u % 2 == 0:
            u /= 2
            r += 1
        return r, int(u)
