""" Code for Question 4a Commitment API"""
import hashlib
import string
from random import shuffle, randint

import sys


def commit(msg, key):
    """ returns hash of the msg"""
    return hashlib.sha256(str(msg + key)).hexdigest()


def verify(committed, msg, key):
    return hashlib.sha256(msg + key).hexdigest() == committed


def gen_str(length):
    """ creates a random string of length len"""
    ran_str = ""
    lis = string.letters
    n = len(lis)
    for _ in range(length):
        i = randint(0, n - 1)
        ran_str += lis[i]
    return ran_str


def gen_key(key_leng):
    key = ""
    for j in xrange(key_leng):
        rb = randint(0, 10 ** 5) % 2
        key += str(rb)
    return key


def a_4(str_len, key_len):
    m = gen_str(str_len)
    key = gen_key(key_len)
    print "Message", m
    com = commit(key, m)
    print "Commit ", com
    print verify(com, key, m)
    dum = list(m)
    while dum == list(m):
        shuffle(dum)
    dum = ''.join(dum)
    print "dum", dum
    print verify(com, key, dum)


def b_4(str_len, key_len):
    """ We also take the hash of the persons key
    and then make a tuple with this hash and message
    and generate the hash of it 
    """
    pass


if __name__ == "__main__":
    part = sys.argv[1]
    string_length = randint(32, 10 ** 2)
    key_length = int(pow(2, randint(6, 10)))
    if part == 'a':
        a_4(string_length, key_length)
    elif part == 'b':

        b_4(string_length, key_length)
    else:
        sys.stderr.write('only accepted inputs are a and b')
