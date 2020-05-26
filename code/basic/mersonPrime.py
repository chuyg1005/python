# print中有变长参数，因此可以使用*args的方式进行参数传递
import math


def isprime(x):
    if x == 1:
        return False
    if x % 2 == 0:
        return x == 2
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True


def findPrime(n):
    res = []
    x = 2
    while len(res) < n:
        if isprime(x) and isprime(2**x-1):
            res.append((x, 2**x-1))
        x += 1 if x == 2 else 2
    return res


res = findPrime(int(input()))
for p, m in res:
    print(p, m)
