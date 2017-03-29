import miller_rabin

x = miller_rabin.MillerRabin()
print(x.find_next_greatest_prime(2522544, 5))
print(x.find_witness_liars())
