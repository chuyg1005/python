# problem1
# strings = input().split()
# max = strings[0]
# for s in strings:
#     if len(s) > len(max):
#         max = s
# print(max)

# problem2
# total = 100
# for rooster in range(1, total // 5 + 1):
#     for hen in range(1, total // 3 + 1):
#         if 7 * rooster + 4 * hen == 100:
#             print("rooster={},hen={},chick={}".format(
#                 rooster, hen, 300 - 15*rooster - 9*hen))

# problem3
# pi, n, sign = 1., 3, -1
# while 1 / n > 1e-6:
#     pi += sign / n
#     sign = -sign
#     n += 2
# print("pi = {:.10f}".format(pi*4))

# problem4
# n = int(input())
# for red in range(4):
#     for yellow in range(4):
#         green = n - red - yellow
#         if 0 <= green <= 6:
#             print(red, yellow, green)

# problem5 需要注意/返回的是浮点数，无论结果是否为整数，使用//返回整数
# n = int(input())
# while True:
#     if n == 1:
#         break
#     if not n % 2:  # 偶数
#         print("{}/2={}".format(n, n // 2))
#         n //= 2
#     else:
#         print("{}*3+1={}".format(n, n*3+1))
#         n = 3 * n + 1

# problem6
# n = int(input())
# for i in range(1, n+1):
#     if not n % i:
#         print("{} * {}".format(i, n//i))

# problem7
s = input()
n, grade = 0, 0
for ch in s:
    if ch == "A":
        n += 1
    else:
        n = 0
    grade += n
print(grade)
