# continue문 이용하여 1~1001 사이 홀수 합
# solution 1
sum = 0
count = 0
num = list(range(1, 1002, 2))
while count < 501:
    count += 1
    if num[count - 1] % 2 == 0:
        continue  # 짝수일때는 다음 반복문으로 넘어감 => continue 밑에 코드 실행 X
    sum += num[count - 1]
print(sum)

# solution 2
sum = 0
i = 0
while i < 1001:
    i += 1  # i는 1부터, 1001까지
    if i % 2 == 0:
        continue  # 짝수일때는 다음 반복문으로 넘어감 => continue 밑에 코드 실행 X
    sum += i
print(sum)
