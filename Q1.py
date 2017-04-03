""" Deals with breaking the Scheme of Q1"""
import hashlib


def hash_short(message, length=16):
    """ Given Hash Function"""
    return hashlib.sha1(message).hexdigest()[:length / 4]


def hack_hash(message):
    pass


if __name__ == "__main__":
    hack_hash("hello")
