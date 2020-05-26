from functools import reduce


def find_maxprod(s, n):
    lst = list(map(int, s))
    idx, prod = 0, reduce(lambda x, y: x*y, lst[:n])
    cur_prod = prod
    for i in range(n, len(lst)):
        cur_prod = cur_prod * lst[i] // lst[i-n]
        # print(prod, lst[i], lst[i-n], cur_prod)
        if cur_prod > prod:
            prod = cur_prod
            idx = i-n+1

    return idx, prod


s = input()
n = int(input())
idx, prod = find_maxprod(s, n)
print("{}={}".format("*".join(s[idx:idx+n]), prod))
