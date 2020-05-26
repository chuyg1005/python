def find_charfrineds(*args: str):
    friends = {}
    for arg in args:
        s = "".join(sorted(arg))
        lst = friends.get(s, [])
        lst.append(arg)
        friends[s] = lst
    lst = sorted(friends.items(), key=lambda item: len(item[1]))
    for _, v in lst:
        v.sort()
    return lst


lst = find_charfrineds(*input().split(','))
print(*map(lambda item: item[1], lst), sep='\n')
