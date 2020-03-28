import math
def sieveOfAtkins(n):
    primes = []
    root = int(math.sqrt(n))
    sieve = [0]*n
    for x in range(1, root+1):
        for y in range(1, root+1):
            p = 4*x*x + y*y
            if p <= n and (p%12 == 1 or p % 12 ==5):
                sieve[p] ^= 1
            p = 3*x*x + y*y
            if p <= n and p % 12 == 7:
                sieve[p] ^= 1
            p = 3*x*x - y*y
            if x >y and p <= n and p % 12 == 11:
                sieve[p] ^= 1
    sieve[3] = 1
    primes.append(3)
    for a in range(5, root+1,2):
        if sieve[a]==1:
            for i in range(a*a, n, a*a):
                sieve[i] = 0
            primes.append(a)
    for a in range(n,2):
        if sieve[a]==1:
            primes.append(a)
    print(primes)
sieveOfAtkins(10)