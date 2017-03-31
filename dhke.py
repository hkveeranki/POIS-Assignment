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
            # print "private-key", a
        key = ipow(self.g, self.__a, self.p)
        return key

    def caluclate_session_key(self, pk):
        return ipow(pk, self.__a, self.p)


class Eve:
    """ Adversary Class to deal with hacking"""

    def __init__(self, p, g):
        """
        Default constructor
        :param p: prime used for key generation
        :param g: generator used for key generation
        """
        self.p = p
        self.g = g

    def calc_key(self, m1, m2):
        """
        Adversary functions
        :param m1: message sent by A
        :param m2: message sent by B
        :return: returns caluclated session key
        """
        prib = hack(self.p, self.g, m2)
        adv_key = ipow(m1, prib, self.p)
        print "hack(pkb) =", prib, "adv_key =", adv_key
        return adv_key


def tester(p, g):
    """
    Performs Diffie Heilman key exchange and tries to hack it
    :param p: prime for DHKE
    :param g: Generator of the Zp*
    """
    p = long(p)
    g = long(g)
    recA = DiffieHeilman(p, g)
    recB = DiffieHeilman(p, g)
    eve = Eve(p, g)
    print "Generating keys for A"
    pka = recA.generate_key()
    print "public key", pka, "\nDone"
    print "Generating keys for B"
    pkb = recB.generate_key()
    print "public key", pkb, "\nDone"
    sk1 = recA.caluclate_session_key(pkb)
    sk2 = recB.caluclate_session_key(pka)
    print "Is session key same: sk1 =", sk1, "sk2 =", sk2, " so ", sk1 == sk2  # 7b

    print "Trying to hack..."

    print "hacked =", sk1 == eve.calc_key(pka, pkb)


if __name__ == "__main__":
    tester(37, 5)
