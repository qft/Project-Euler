primes = [2,3,5,7,11,13]
n = 15

def isPrime(x):
    for p in primes:
        if p > x**0.5 + 1:
            return True
        if x%p == 0:
            return False

while n < 2000000:
    if isPrime(n):
        primes.append(n)
        n += 2
    else:
        n += 2

print sum(primes)
