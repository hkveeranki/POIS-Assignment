""" Contains Miller rabin primality test"""
import random
from util_functions import ipow, gcd, factorise


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

        r, u = factorise(n - 1)
        pow_needed = []
        s = u
        power = 1

        for i in range(r):
            pow_needed.append(int(s * power))
            power *= 2
        # print('s', s, 'r', r, 'pow_needed', pow_needed)
        for i in range(t):
            a = random.randint(1, n - 1)
            if gcd(a, n) != 1:
                return False
            lis = []
            for j in range(r):
                lis.append(ipow(a, pow_needed[j], n))
            fl = 1
            if lis[0] == 1 or lis[0] == n - 1:
                fl = 0
            for j in range(1, r):
                if lis[j] == n - 1:
                    fl = 0
                    break
            if fl == 1:
                #       print('came false for ', a, ' because ', lis)
                return False
        return True

    def find_next_greatest_prime(self, n, t):
        """
        Given a number outputs a prime greater than equal to n
        :param n:
        :return: an integer p such that p is prime and p >= n
        """
        p = int(n)
        while not self.is_prime(p, t):
            p += 1
        return p

    def find_witness_liars(self):
        """ Find Strong Witnessess and Liars"""
        n = self.n
        r, u = factorise(n - 1)
        pow_needed = []
        s = u
        power = 1

        for i in range(r):
            pow_needed.append(int(s * power))
            power *= 2
        liars = []
        witnesses = []

        for a in range(2, n - 2):
            lis = []
            for j in range(r):
                lis.append(ipow(a, pow_needed[j], n))
            fl = 1
            if lis[0] == 1 or lis[0] == n - 1:
                fl = 0
            for j in range(1, r):
                if lis[j] == n - 1:
                    fl = 0
            if fl == 0 and gcd(a, n) == 1:
                liars.append(a)
                # print("a", a, "list", lis)
            elif fl == 1:
                cnt = 1
                if lis[0] == 1 or lis[0] == n - 1:
                    cnt -= 1
                for j in range(1, r):
                    if lis[j] != n - 1:
                        cnt += 1
                if cnt == r:
                    witnesses.append(a)
        # print('real:O ', sorted(list(set(range(2, n - 1)) - set(witnesses + liars))))
        return liars, witnesses
