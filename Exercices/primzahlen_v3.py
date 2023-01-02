import time
from math import sqrt

MAX_ZAHL = 100000000

primes = [2]
zeit0 = time.time()
for zahl in range(2, MAX_ZAHL + 1):
    is_prime = True
    tmax = int(sqrt(zahl) + 1)
    for to_test in primes:
        if to_test > tmax:
            break
        if zahl % to_test == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(zahl)

zeit1 = time.time()
print(primes, zeit1 - zeit0)
