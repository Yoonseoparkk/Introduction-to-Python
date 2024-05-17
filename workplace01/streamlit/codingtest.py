# t = int(input())  # 입력받을 문자열 갯수

# for i in range(t):
#     a = list(map(str, input().split(" ")))

#     n = int(a[0])  # 몇 회 반복할 것인지
#     s = a[1]  # 반복할 문자열

#     for i in range(len(s)):
#         print(n * s[i], end="")
#     print()

#   -----------------------------------

# s = str(input())
# newList = s.split()
# print(len(newList))

# # split()과 split(" ")는 결과가 다름
# # split( )을 사용하면 길이에 상관없이 공백을 모두 제거여 분리하고
# # split(' ')을 사용하면 공백 한 개마다 분리

#   -----------------------------------

# numbers = list(map(str, input().split(" ")))

# a = list(numbers[0])
# b = list(numbers[1])

# num_a = int(a[2]) * 100 + int(a[1]) * 10 + int(a[0])
# num_b = int(b[2]) * 100 + int(b[1]) * 10 + int(b[0])

# if num_a > num_b:
#     print(num_a)
# else:
#     print(num_b)

#   -----------------------------------

# a = list(str(input()))
# for i in range(len(a)):
#     if a[i] in "ABC":
#         a[i] = "2"
#     if a[i] in "DEF":
#         a[i] = "3"
#     if a[i] in "GHI":
#         a[i] = "4"
#     if a[i] in "JKL":
#         a[i] = "5"
#     if a[i] in "MNO":
#         a[i] = "6"
#     if a[i] in "PQRS":
#         a[i] = "7"
#     if a[i] in "TUV":
#         a[i] = "8"
#     if a[i] in "WXYZ":
#         a[i] = "9"

# sum = 0
# for i in range(len(a)):
#     sum += int(a[i])
# print(sum + len(a))

#   -----------------------------------

# while True:
#     try:
#         print(input())
#     except EOFError:
#         break

#   -----------------------------------

# print("         ,r'\"7")
# print("r`-_   ,'  ,/")
# print(" \. \". L_r'")
# print("   `~\\/")
# print("      |")
# print("      |")

#   -----------------------------------

# a = list(map(int, input().split(" ")))
# print(f"{1-a[0]} {1-a[1]} {2-a[2]} {2-a[3]} {2-a[4]} {8-a[5]}")

#   -----------------------------------

# n = int(input())
# for i in range(1, n):
#     print(" " * (n - i) + "*" * (2 * i - 1))
# for i in range(n, 0, -1):
#     print(" " * (n - i) + "*" * (2 * i - 1))

# n = 5
#     *     " " 4 i=1 1
#    ***    " " 3 i=2 3
#   *****   " " 2 i=3 5
#  *******  " " 1 i=4 7
# ********* " " 0 i=5 9
#  *******  " " 1 i=1 7
#   *****   " " 2 i=2 5
#    ***    " " 3 i=3 3
#     *     " " 4 i=4 1

#   -----------------------------------

# word = list(str(input()))

# if word == word[::-1]:
#     print(1)
# else:
#     print(0)

#   -----------------------------------

s = str(input())
croatia = ["c-", "dz=", "d-", "lj", "nj", "s=", "z="]
count = 0
for c in croatia:  # 크로아티아 알파벳 갯수만 세기
    if c in s:
        count += 1
        s = s.replace(c, "")  # 이미 카운트한 알파벳 제거
for si in s:  # 나머지 알파벳 갯수 세기
    count += 1
print(count)
