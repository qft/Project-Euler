fib = [1,2]
fibLength = 2
while 1:
    toAppend = fib[fibLength-1] + fib[fibLength-2]
    if toAppend > 4000000:
        break
    fib.append(toAppend)
    fibLength += 1

print sum([x for x in fib if x%2==0])
