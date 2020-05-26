def minnum(*args):
    s = "".join(map(str, sorted(args)))
    n = 0
    for ch in s:
        if ch != '0':
            break
        n += 1
    s = s[n] + '0' * n + s[n+1:]
    return int(s)


print(minnum(*map(int, input().split(','))))
