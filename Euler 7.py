primes = [2,3,5,7,11,13]
i = 7
n = 15

def isPrime(x):
    for p in primes:
        if p > x**0.5 + 1:
            return True
        if x%p == 0:
            return False

while i < 10002:
    if isPrime(n):
        primes.append(n)
        n += 2
        i += 1
    else:
        n += 2

print primes[len(primes)-1]
