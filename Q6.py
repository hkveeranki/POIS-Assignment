""" Contains Diffie Heilman code and tests on it"""
import random
from Q3 import MillerRabin
from util_functions import ipow

global p, g


class DiffieHeilman:
    """ Class to deal with DiffieHeilman """

    def __init__(self, prime, gen):
        """
        Default Constructor
        :param prime: prime used for cyclic group
        :param gen: genertor of the group
        """
        self.p = prime
        self.g = gen
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


def correctness_tester():
    """
    Performs Diffie Heilman key exchange and tries to hack it
    """
    print "--- Verifying the correctness ---"
    alice = DiffieHeilman(p, g)
    bob = DiffieHeilman(p, g)
    print "Generating keys for A"
    pka = alice.generate_key()
    print "public key", pka, "\nDone"
    print "Generating keys for B"
    pkb = bob.generate_key()
    print "public key", pkb, "\nDone"
    sk1 = alice.caluclate_session_key(pkb)
    sk2 = bob.caluclate_session_key(pka)
    print "Is session key same: sk1 =", sk1, "sk2 =", sk2, " so ", sk1 == sk2  # 7b
    print "--- Done testing ---"


def man_in_the_middle():
    """ Trying to perform man in the middle attack"""
    print "--- Performing Man in the middle attack ---"
    print "Caluclating the keys..."
    alice = DiffieHeilman(p, g)
    bob = DiffieHeilman(p, g)
    eve = DiffieHeilman(p, g)
    pka = alice.generate_key()
    pkb = bob.generate_key()
    pke = eve.generate_key()
    print "Done....\nGenerating Session keys"
    ska = alice.caluclate_session_key(pke)
    skb = bob.caluclate_session_key(pke)
    ske1 = eve.caluclate_session_key(pka)
    ske2 = eve.caluclate_session_key(pkb)
    print "Session keys are..."
    print "Alice :", ska
    print "Bob :", skb
    print "Eve :", ske1, ske2

    print "Can Eve read messages sent by Alice? :", ske1 == ska
    print "Can Eve read messages sent by Bob? :", ske2 == skb
    print "Can Bob read messages sent by Alice? :", skb == ska
    print "--- Done ---"


valid_gens = [2, 3, 5, 6, 7, 11]


def check_gen(n, gen):
    val = gen
    ind = 1
    while ind < n:
        ind += 1
        val = (val * gen) % n
        if val == 1 and ind != n - 1:
            return False
    return True


def generate_prime():
    """ Generates primes from 10**5 to 10**7 and returns the array """
    tester = MillerRabin(221)
    while True:
        tmp_p = random.randint(10 ** 6, 10 ** 7)
        if tester.is_prime(tmp_p, 10):
            return tmp_p


if __name__ == "__main__":
    global p, g
    p = generate_prime()
    print "Prime is", p
    g = 2
    for i in range(len(valid_gens)):
        if check_gen(p, valid_gens[i]):
            g = valid_gens[i]
            break
    print "g is", g
    correctness_tester()
    man_in_the_middle()
