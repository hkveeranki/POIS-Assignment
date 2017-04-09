import random

import miller_rabin

x = miller_rabin.MillerRabin(221)
inp = random.randint(10 ** 6, 10 ** 8)
sinp = str(inp)
print "N =", sinp, "is_prime", x.is_prime(inp, len(sinp))
print "Next greatest prime:", x.find_next_greatest_prime(inp, len(sinp))
print "Liars and witesses of 221:", x.find_witness_liars()
