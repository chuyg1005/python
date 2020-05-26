from collections import Counter


def count_str(s: str):
    counter = Counter(s.split())
    lst1 = sorted(counter.items(), key=lambda item: item[0])
    lst2 = sorted(counter.items(), key=lambda item: [item[1], item[0]])
    return lst1, lst2


lst1, lst2 = count_str(input())
print("Sorting by the key:")
for k, v in lst1:
    print(k, v)
print("Sorting by the value:")
for k, v in lst2:
    print(k, v)
