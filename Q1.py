""" Deals with breaking the Scheme of Q1"""
import hashlib
import random

import time

DATA_FILE = "english.data"
lis = []
ind_lis = []
DEF_LEN = 160


def hash_short(message, length=16):
    """ Given Hash Function"""
    return hashlib.sha1(message).hexdigest()[:length / 4]


def make_replication():
    """ Replicate the sample data and"""
    f = open(DATA_FILE, 'r')
    global lis, ind_lis
    lis = f.readlines()
    ind_lis = range(len(lis))
    f.close()


def hack_hash(length):
    """ Tries to hack the sha1"""
    cnt = 0
    h = {}
    n = len(lis)
    taken = {}
    while True:
        ind = random.randint(0, n - 1)
        ind = ind_lis[ind]
        i = lis[ind]
        cnt += 1
        val = hash_short(i, length)
        if val not in h:
            h[val] = i
        elif i != h[val]:
            print "Broke at ", cnt
            print i, hash_short(i, DEF_LEN)
            print h[val], hash_short(h[val], DEF_LEN)
            break


if __name__ == "__main__":
    length = input("Enter length parameter: ")
    start_time = time.time()
    print("Reading Data")
    make_replication()
    random.shuffle(ind_lis)
    print("Done.. took %s seconds to process data" % (time.time() - start_time))
    start_time = time.time()
    hack_hash(length)
    print("took %s seconds to hack" % (time.time() - start_time))
