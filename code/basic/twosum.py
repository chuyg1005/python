def twosum(n: int, lst: list):
    '''lst is sorted'''
    i, j = 0, len(lst)-1
    while i < j:
        sum = lst[i] + lst[j]
        if sum == n:
            return i, j
        elif sum < n:
            i += 1
        else:
            j -= 1
    return "not found"


lst = [1, 4, 5,6,7,8,9,10,11,12,13,15,18,19,20,21,29,34,54,65]
print(twosum(int(input()), lst))
