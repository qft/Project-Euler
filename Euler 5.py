def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def lcm(a, b):
    return a*b / gcd(a,b)

ans = 1

for x in range(1,21):
    ans = lcm(ans, x)

print ans
