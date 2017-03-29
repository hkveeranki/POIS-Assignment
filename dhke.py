""" Contains Diffie Heilman code"""
import random

from util_functions import ipow


class DiffieHeilman:
    """ Class to deal with DiffieHeilman """

    def __init__(self, p, g):
        """
        Default Constructor
        :param p: prime used for cyclic group
        :param g: genertor of the group
        """
        self.p = p
        self.g = g
        self.__a = None

    def generate_key(self):
        """ Generates public key for the recipient"""
        if self.__a is None:
            a = random.randint(0, self.p - 1)
            self.__a = a
            print("private-key", a)
        key = ipow(self.g, self.__a, self.p)
        return key

    def caluclate_session_key(self, pk):
        return ipow(pk, self.__a, self.p)


def tester(A, B):
    print("Generating keys for A")
    pka = A.generate_key()
    print("public key", pka, "\nDone")
    print("Generating keys for B")
    pkb = B.generate_key()
    print("public key", pkb, "\nDone")
    sk1 = A.caluclate_session_key(pkb)
    sk2 = B.caluclate_session_key(pka)
    print("Is session key same?", sk1 == sk2)


if __name__ == "__main__":
    A = DiffieHeilman(37, 5)
    B = DiffieHeilman(37, 5)
    tester(A, B)
