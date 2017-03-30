import miller_rabin

x = miller_rabin.MillerRabin(221)
print(x.is_prime(252601, 5))
print(x.find_witness_liars())
