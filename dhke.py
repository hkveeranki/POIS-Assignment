""" Contains Diffie Heilman code and tests on it"""
import random

from bsgs import hack
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


def tester(p, g):
    """
    Performs Diffie Heilman key exchange and tries to hack it
    :param p: prime for DHKE
    :param g: Generator of the Zp*
    """
    p = int(p)
    g = int(g)
    recA = DiffieHeilman(p, g)
    recB = DiffieHeilman(p, g)
    print("Generating keys for A")
    pka = recA.generate_key()
    print("public key", pka, "\nDone")
    print("Generating keys for B")
    pkb = recB.generate_key()
    print("public key", pkb, "\nDone")
    sk1 = recA.caluclate_session_key(pkb)
    sk2 = recB.caluclate_session_key(pka)
    print("Is session key same: sk1 =", sk1, "sk2 =", sk2, " so ", sk1 == sk2)  # 7a
    prib = hack(g, pkb, p)
    adv_key = ipow(pka, prib, p)
    print("Trying to hack...")
    print("hack(pkb) =", prib, "adv_key =", adv_key, "hacked =", sk1 == adv_key)


if __name__ == "__main__":
    tester(37, 5)
