# problem1
# for i in range(1, 5):
#     for j in range(1, 5):
#         if j != i:
#             for k in range(1, 5):
#                 if k not in (i, j):
#                     print(i*100 + j * 10 + k)

# problem2：并行赋值的好处
# n = int(input())
# a, b, res = 2, 1, 0
# for i in range(n):
#     res += a / b
#     a, b = a+b, a
# print("{:.2f}".format(res))

# problem3：字符串的拼接（使用+），除此之外字符串还支持%, *（格式化和重复）
# N = 5
# encrypt_text = input()
# decrypt_text = ""
# for ch in encrypt_text:
#     if ch.isupper():
#         decrypt_text += chr(ord('A') + (ord(ch)-ord('A')-N) % 26)
#     else:
#         decrypt_text += ch
# print(decrypt_text)

# problem4: 序列的手动解包


# def factor(n):
#     factors = []
#     for i in range(1, n):
#         if not n % i:
#             factors.append(i)
#     return factors


# for i in range(1, 1000):
#     factors = factor(i)
#     if sum(factors) == i:
#         print("{} its factors are".format(i), *factors, end=" \n")

# problem5: 使用列表的重复运算符创建指定长度的列表
# counter = [0] * 26
# s = input().lower()
# for ch in s:
#     if ch.islower():
#         counter[ord(ch) - ord('a')] += 1
# print(counter)

# problem6: 使用tri[:]生成副本
# tri = []
# n = int(input())
# for k in range(n):
#     tri_copy = tri[:]
#     for i in range(1, len(tri_copy)):
#         tri[i] = tri_copy[i-1] + tri_copy[i]
#     tri.append(1)
#     print(tri)

# problem7：数字和字符串之间的转换以及序列的解包
# n = int(input())
# lst = []
# for i in range(1, 101):
#     if i % n and str(n) not in str(i):
#         lst.append(i)
# for i in range(0, len(lst), 10):
#     print(*lst[i:i+10], sep=",")
