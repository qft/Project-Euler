def isPalindrome(n):
    return str(n) == str(n)[::-1]

print (max([n1*n2 for n1 in range(100,1000) for n2 in range(100,1000) if isPalindrome(n1*n2)]))
