def getPrime():
    primes = [2, 3]
    i = 0  # i表示下次发射的质数
    while True:
        # 生成一个新的质因数
        if i == len(primes):
            n = primes[-1] + 2
            while True:
                for prime in primes:
                    if n % prime == 0:
                        break
                else:
                    primes.append(n)
                    break
                n += 2
        yield primes[i]
        i += 1


def factor(n):
    res = []
    primeGen = getPrime()
    while n != 1:
        prime = next(primeGen)
        while n % prime == 0:
            res.append(prime)
            n //= prime
    return res


n = int(input())
print("{}={}".format(n, "*".join(map(str, factor(n)))))
