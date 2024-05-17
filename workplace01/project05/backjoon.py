n = int(input("시험 본 과목의 개수 (N) : "))


grade = []
for i in range(0, n):
    g = int(input("점수 입력 : "))
    if 0 <= g <= 100:
        grade.append(g)
print(grade)

sum = 0
for i in range(len(grade)):
    sum += grade[i]
print(sum)

print("새로운 평균 : ", round(sum / n, 3))
