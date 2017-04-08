""" Code for Question 4a Commitment API"""
import hashlib
from random import shuffle, randint, sample

import sys

from util_functions import generate_primes, \
    modinv, ipow, gen_key, gen_str


def Hash(inp):
    return hashlib.sha256(inp).hexdigest()


def commit(msg):
    """ returns hash of the msg"""
    key_length = int(pow(2, randint(8, 12)))
    key = gen_key(key_length)
    return Hash(str(msg + key)), key


def verify(committed, msg, key):
    return Hash(str(msg + key)) == committed


def a_4(str_len):
    m = gen_str(str_len)
    print "Message", m
    com, key = commit(m)
    print "Commit", com
    print verify(com, m, key)
    dum = list(m)
    while dum == list(m):
        shuffle(dum)
    dum = ''.join(dum)
    print "dum", dum
    print verify(com, key, dum)


def generate_rsa_keypair():
    global primes
    len_p = len(primes)
    pi, qi = sample(range(1, len_p + 1), 2)
    p, q = primes[pi], primes[qi]
    gen_n = p * q
    phin = (p - 1) * (q - 1)
    e = 65537
    d = modinv(e, phin)
    return gen_n, e, d


def commit1(message, rans, sig):
    com, key = commit(message)
    return com, key, rans, sig


def verify1(com, message):
    global n, pubk
    message_v = (com[0] == Hash(str(message + com[1])))
    person_v = (ipow(com[3], pubk, n) == com[2])
    if message_v:
        print "Message match with hash"
    else:
        print "Message match with hash"
    if person_v:
        print "Same person did it"
    else:
        print "different person did it"


def b_4(str_len):
    """ We also take the hash of the persons key
    and then make a tuple with this hash and message
    and generate the hash of it 
    """
    print "Generating RSA Key Pair"
    global n, pubk
    n, pubk, prik = generate_rsa_keypair()
    print "Done..Publishing Info"
    print "n:", n, "public key:", pubk
    m = gen_str(str_len)
    rans = randint(2, 10 ** 7)
    sig = ipow(rans, prik, n)
    comTupple = commit1(m, rans, sig)
    verify1(comTupple, m)
    pass


if __name__ == "__main__":
    part = sys.argv[1]
    string_length = randint(32, 10 ** 2)
    if part == 'a':
        a_4(string_length)
    elif part == 'b':
        print("Generating Primes...")
        global primes
        primes = generate_primes()
        print("Done")
        b_4(string_length)
    else:
        sys.stderr.write('only accepted inputs are a and b')
