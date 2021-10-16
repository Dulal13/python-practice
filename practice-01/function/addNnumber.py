def addNumber(n):
    if(n == 1):
        return 1
    else:
        return n+addNumber(n-1)

print(addNumber(5))