import random

import miller_rabin

x = miller_rabin.MillerRabin(221)
inp = random.randint(2, 10 ** 100)
sinp = str(inp)
print "N =", sinp
print "Next greatest prime:", x.find_next_greatest_prime(inp, len(sinp))
print "Liars and witesses", x.find_witness_liars()
