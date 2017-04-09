""" Deals with breaking the Scheme of Q1"""
import hashlib
import random

import time

DATA_FILE = "english.data"
lis = []
DEF_LEN = 160


def hash_short(message, length=16):
    """ Given Hash Function"""
    return hashlib.sha1(message).hexdigest()[:length / 4]


def make_replication():
    """ Replicate the sample data and"""
    f = open(DATA_FILE, 'r')
    global lis
    lis = f.readlines()
    f.close()


def hack_hash(length):
    """ Tries to hack the sha1"""
    cnt = 0
    h = {}
    for i in lis:
        val = hash_short(i, length)
        if val not in h:
            h[val] = i
        elif i != h[val]:
            print i, hash_short(i, DEF_LEN)
            print h[val], hash_short(h[val], DEF_LEN)
            return True
    return False


if __name__ == "__main__":
    length = input("Enter length parameter: ")
    taken = {}
    start_time = time.time() * 1000
    print("Reading Data")
    make_replication()
    print("Done.. took %s milli seconds to process data" % (time.time() - start_time))
    for i in xrange(4, length + 1, 4):
        print "\n--- Length ---\n", i
        start_time = time.time()
        fl = hack_hash(i)
        if fl:
            taken[i] = (time.time() - start_time) * 1000
            print("took %s milli seconds to hack" % taken[i])
        else:
            taken[i] = -1
            print "Cannot hack with given data for length = ", i
        print "\n--- Done ---\n"
    for i in range(4, length + 1, 4):
        if taken[i] != -1:
            print "length:", i, "time to hack", taken[i], "milli seconds"
        else:
            print "length:", i, "Could Not hack"
