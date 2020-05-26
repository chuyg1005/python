def Nicoqish(x):
    if x == 1:
        return (1, 1)
    for i in range(1, x):
        if x % i == 0:
            n = x // i
            if i - n >= 0:
                return i - n + 1, i + n - 1


n = int(input())
for i in range(1, n+1):
    # print(Nicoqish(i**3))
    res = Nicoqish(i**3)
    print("{}^3={}".format(i, "+".join(map(str, range(res[0], res[1]+1, 2)))))
