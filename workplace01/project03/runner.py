from helpers.debug import *
import time


# 중첩 반복문 피라미드1
def 피라미드1():
    output = ""
    for i in range(0, 9):
        for j in range(0, i + 1):
            output += "*"
        output += "\n"
    print(output)


# 중첩 반복문 피라미드2
def 피라미드2():
    output = ""
    for i in range(1, 15):
        for j in range(14, i, -1):
            output += " "
        for k in range(0, (i * 2) - 1):
            output += "*"
        output += "\n"
    print(output)


피라미드1()
피라미드2()

# [while과 for의 차이]
# for => 시작과 끝을 알고 있을 때
# while => 반복문이 언제 끝날 지 모를 때
# 시작값이 문자 밖에 있는지 안에 있는지의 차이
# while (True인 동안 무한반복) => while True, while 1, while a==a...

# 무한 반복문 강제 종료 단축키 : ctrl + C
# while True:
#     print("안녕하세요")

# 누적합
sum = 0
while True:
    sum += 1
    if sum == 15:
        break
print(sum)

# 상태를 기반으로 반복하기
list1 = [1, 2, 2, 2, 5, 6, 7, 1, 2]
value = 2  # 제거할 값
while value in list1:
    list1.remove(value)
print(list1)

# 문자열 리스트
list2 = list("tawaianakalaea")
value = "a"  # 제거할 값
while value in list2:
    list2.remove(value)
print(list2)

# 세계 표준시(유닉스 타임)
# 1970년 1월 1일 0시 0분 0초 기준으로 몇 초 지났는지 정수로 나타낸 것
print(time.time())
# 5초 동안 반복하기
number = 0
target_tick = time.time() + 5
while time.time() < target_tick:
    number += 1
print(f"5초 동안 {number}회 반복했습니다.")

# break와 continue
# break문 => 자신이 속해있는 그 구문의 반복문을 탈출
# continue => 만나는 즉시 하위 코드를 스킵하고 다음 회차로 진행

# 1~100 누적합
# 몇 회 반복할 지 미리 알기 때문에 while문보다 for문이 적합
sum = 0
for i in range(1, 101):
    sum += i
print(sum)

# while문 사용하는 경우
sum = 0
count = 0
num = list(range(1, 101))
while count < 100:
    sum += num[count]
    count += 1
print(sum)

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
        continue
    sum += i
print(sum)

# 리스트 딕셔너리 복습
keys = ["name", "hp", "mp", "level"]
values = ["기사", 200, 30, 5]

# solution 1
character = {}
for i in range(len(keys)):
    character[keys[i]] = values[i]
print(character)

# solution 2 - 두 리스트의 item 수가 같기 때문에 zip 함수 사용 가능
character = {}
for k, v in zip(keys, values):
    character[k] = v
print(character)

# 1~100의 수 중 최대가 되는 경우는 어떤 숫자를 곱했을 때인지 찾기
max_v = 0
a = 0
b = 0
for i in range(1, 101):
    if i * (100 - i) > max_v:
        max_v = i * (100 - i)
        a = i
        b = 100 - i
print(f"최대가 되는 경우: {a} * {b} = {max_v}")

# reverse 함수의 결과는 generator
# iterable = 반복할 수 있는 것
# iterable 객체 => 반복 가능한 객체

# generic type
# 이터러블객체 = []
# for i in range(0, len(이터러블객체)):
# for idx, item in enumerate(items):
리스트 = ["ads", "asff", "qweqt"]
print(enumerate(리스트))
print(type(enumerate(리스트)))
print(list(enumerate(리스트)))
for idx, val in enumerate(리스트):
    print(f"{idx}번째 요소는 {val}입니다.")

# dictionary의 items() 함수
딕셔너리 = {"키": "밸류", "과일": "딸기", "동물": "고양이"}
for k, v in 딕셔너리.items():
    print(f"딕셔너리[{k}] = {v}")

# 조건문을 가진 list comprehension
변수 = [i for i in range(0, 10) if i % 2 == 1]
print(변수)

list = [i * i for i in range(0, 20, 2)]
print(list)

array = ["사과", "자두", "귤", "포도"]
output = [fruit for fruit in array if fruit != "귤"]
print(output)

# tuple은 콤마(,)로 구분되므로 괄호 안 문자열 단순 나열은 하나의 문자열로 인식한다
test = ()
print(type(test))  # tuple 타입

# 문자열 join() 함수 => 특정 문자열을 문자열로 구성된 리스트 요소 사이에 넣어줌
문자열리스트 = "안녕하세요"
print(".".join(문자열리스트))

# 이터레이터(iterater)와 next()함수
numbers = [1, 2, 3, 4, 5]
r_num = reversed(numbers)

print("reversed numbers: ", r_num)
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))

# 염기 서열 내 DNA 분류하기
dna_list = input("염기 서열을 입력해주세요: ")
dna_dic = {"a": 0, "g": 0, "t": 0, "c": 0}
for dna in dna_list:
    dna_dic[dna] += 1

for k in dna_dic:
    print(f"{k}의 개수: {dna_dic[k]}")


# 선언 => 가인수 파라미터
# 호출 => 실인수 아규먼트
# 선언할 때 (*args, **kwargs)


def print_n_times(v, 횟수):
    for i in range(횟수):
        print(v)


print_n_times("반복될 내용", 2)


# 매개변수의 타입을 지정해주고
# 추가로 return할 값도 지정해준다면 더욱 명시적인 함수를 선언할 수 있음
def print_n_times2(v: str, 횟수: int) -> None:
    for i in range(횟수):
        print(v)


print_n_times2("타입 지정 버전", 3)


# 가변위치매개변수 * 리스트 => 가변 : 갯수가 변한다
# 가변키워드매개변수 ** 딕셔너리
# 가변 매개변수 : print() 함수처럼 매개변수를 원하는 만큼 받을 수 있는 함수
# (앞쪽 가변위치매개변수 가변키워드매개변수 뒤쪽) => 함수에서 선언할 수 있는 순서에 제약이 있음


def print_n_times(n, *values):
    for i in range(n):
        for value in values:
            print(value)
        print()
        return  # 그냥 return하면 0이 리턴된다


print_n_times(3, "안녕하세요", "반갑습니다", "안녕히계세요")


# 범위 내부의 정수를 모두 더하는 함수
def sum_all(start: int, end: int):  # 함수 선언
    output = 0  # 변수 선언
    for i in range(start, end + 1):  # 반복문을 통해 정수 더하기
        output += i
    return output  # 결과값 리턴


# 함수 호출 및 출력
print("0 to 100:", sum_all(0, 100))
print("0 to 1000:", sum_all(0, 1000))
print("50 to 100:", sum_all(50, 100))
print("500 to 1000:", sum_all(500, 1000))


# 기본 매개변수 - 매개변수를 입력하지 않았을 경우 매개변수에 들어가는 기본 값
# ex) def print_val(start=100, end=200) => start, end
# 키워드 매개변수 - 매개변수 이름을 지정해서 입력하는 매개변수
# ex) def print_val(end="", n=1) => end, n


# 기본 매개변수와 키워드 매개변수를 활용해 범위의 정수 더하는 함수
def sum_all2(start=0, end=100, step=1):
    output = 0
    for i in range(start, end + 1, step):
        output += i
    return output


print("A.", sum_all2(0, 100, 10))
print("B.", sum_all2(end=100))
print("C.", sum_all2(end=100, step=2))


# 반복문으로 팩토리얼 구하기
def factorial(n):
    output = 1
    for i in range(1, n + 1):
        output *= i
    return output


# 재귀함수 : 내부에서 자기 자신을 호출하는 함수
# 재귀함수 - 팩토리얼
def factorial2(n):
    if n == 0:  # n이 0이라면
        return 1  # 1을 리턴
    else:
        return n * factorial(n - 1)  # def factorial(n)을 참조


print("1!:", factorial2(1))
print("2!:", factorial2(2))
print("3!:", factorial2(3))
print("4!:", factorial2(4))
print("5!:", factorial2(5))


# 재귀함수 - 피보나치 수열 1
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print("fibonacci(5):", fibonacci(5))
print("fibonacci(50):", fibonacci(30))

# 재귀함수 - 피보나치 수열 2
counter = 0


def fibonacci2(n):
    print(f"fibonacci({n})을(를) 구합니다.")
    global counter  # python에서는 함수 내부에서 함수 외부에 있는 변수를 참조할 수 없기 때문에 global 선언이 필요하다 => 그러나 지양해야 함
    counter += 1

    # 피보나치 수 구하기
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci2(n - 1) + fibonacci2(n - 2)


fibonacci2(10)
print("---")
print(f"fibonacci(10) 계산에 활용된 덧셈 횟수는 {counter}번입니다.")

# 메모화 : 한 번 계산한 값을 저장해 놓은 후, 이후에 다시 계산하지 않고 저장된 값을 활용하는 것
# 재귀함수 - 피보나치 수열 3
dictionary = {1: 1, 2: 1}


def fibonacci_memo(n):
    if n in dictionary:  # 메모가 되어 있으면 메모된 값을 리턴
        return dictionary[n]
    else:
        output = fibonacci_memo(n - 1) + fibonacci_memo(n - 2)
        dictionary[n] = output
        return output


print("fibonacci(10):", fibonacci_memo(1))
print("fibonacci(10):", fibonacci_memo(2))
print("fibonacci(10):", fibonacci_memo(10))
print(dictionary)  # dictionary에 기존에 없던 피보나치 수열값이 추가됨


# 리스트 평탄화 - 1 => 3중 중첩된 리스트 평탄화 가능
def flatten(data):
    output = []
    for item in data:
        if type(item) == list:
            output += item
        else:
            output.append(item)
    return output


print(flatten([[[1], 2, 3], 2, 3, 5, [1]]))


# 리스트 평탄화 - 2 => 재귀함수 활용하여 3중 이상의 다중 중첩된 리스트 평탄화 가능
def flatten2(data):
    output = []
    for item in data:
        if type(item) == list:
            output += flatten2(item)
        else:
            output.append(item)
    return output


print(flatten2([[[1, [2, 3, 4, 5]], 2, 3], 2, 3, 5, [1]]))  # => 5중 중첩된 리스트 data


# 함수는 단일값을 리턴한다
튜플1, 튜플2 = (1, 2)
print(튜플1)
print(튜플2)


# lambda (익명함수, 무명함수) => 이름이 없는 함수. 함수명이 있어야 호출을 하지만,
# 호출할 일이 없을 때 그 위치에서 한번만 쓰는 용도로 씀
# => 만들자마자 바로 쓰는 것 (다시 호출할 일 X)
# => 함수가 함수를 인자로 사용하는 경우. 함수의 값 자체를 인자로 사용

리스트 = [1, 2, 3, 4]


def 일반함수(x):
    return x * x


# 람다함수
lambda x: x * x


def 필터함수(x):
    if x > 2:
        return x


# map() & filter() 함수 => 첫번째 인자로 함수를 받는 함수. 함수를 인자로 사용할 때에는 '함수명'만 입력한다
# map() 함수 :  => 넣은 요소 수 그대로 리턴
print(map(일반함수, 리스트))  # 메모리 주소 리턴
print(list(map(일반함수, 리스트)))  # return->list
print(map(lambda x: x * x, 리스트))
print(list(map(lambda x: x * x, 리스트)))


# filter() 함수 : 리스트의 요소를 함수에 넣고 리턴된 값이 True인 값으로 새로운 리스트 생성 => 리턴된 요소의 수 달라질 수 있음
print(filter(필터함수, 리스트))
print(list(filter(필터함수, 리스트)))
print(filter(lambda x: x > 2, 리스트))
print(list(filter(lambda x: x > 2, 리스트)))


# 파일 처리
# open() 함수 => 첫번째 매개변수로 파일 경로를, 두번쨰 매개변수로 모드 지정
# 모드 : w(write 모드), a(append 모드), r(read 모드)

읽어들일파일경로 = r"C:\Users\USER\Desktop\workplace01\project03\2024-05-10.txt"
열린파일 = open(읽어들일파일경로, encoding="utf-8")
내용 = 열린파일.read()
내용2 = 열린파일.readline()
내용3 = 열린파일.readlines()

열린파일.close()


# write로 새로운 파일 생성 & 쓰기
with open("내가만든파일.txt", encoding="utf-8", mode="w") as file:
    for i in range(10):
        file.write("추가문자열\n")


# (참고) python fake => 가짜 이름, 주소 등 자연스럽게 생성하는 사이트

# 랜덤하게 1000명의 키와 몸무게 만들기
import random

한글 = list("가나다라마바사아자차카타파하")
with open("info.txt", encoding="utf-8", mode="w") as file:
    for i in range(1000):
        이름 = random.choice(한글) + random.choice(한글) + random.choice(한글)
        키 = random.randrange(140, 200)
        몸무게 = random.randrange(40, 120)

        file.write(f"{이름}, {키}, {몸무게}\n")

# 위에서 만든 데이터 반복문으로 한줄씩 읽기
with open("info.txt", encoding="utf-8", mode="r") as file:
    for l in file:
        (이름, 키, 몸무게) = l.strip().split(",")  # 변수선언

        # 데이터 문제 없는지 확인
        if (not 이름) or (not 키) or (not 몸무게):
            continue

        # 결과 계산
        bmi = int(몸무게) / ((int(키)) / 100) ** 2
        result = ""
        if 25 <= bmi:
            result = "과체중"
        elif 18.5 <= bmi:
            result = "정상체중"
        else:
            result = "저체중"

        print(
            "\n".join(
                [
                    f"이름: {이름}",
                    f"몸무게: {몸무게}",
                    f"키: {키}",
                    f"BMI: {bmi}",
                    f"결과: {result}",
                ]
            )
        )


# 제너레이터(generator) => 이터레이터(iterater)를 직접 만들 때 사용
# yield 키워드 사용 => 함수를 호출해도 함수 내부의 코드가 실행되지 않음
# next() 함수를 사용해 함수 내부 코드 실행 => return 값으로 yield 키워드 뒤에 입력한 값이 출력됨
def test():
    print("호출되었습니다.")
    yield "test"


# print(dir(test()))
print(test())
next(test())

리스트안에딕셔너리 = [{"이름": "홍길동"}, {"이름": "강길동"}]
리스트안에딕셔너리.sort(key=lambda 리스트안에딕셔너리: 리스트안에딕셔너리["이름"])

for 리스트 in 리스트안에딕셔너리:
    print(리스트)


#   스택    : 순서 O     더 빠름     원시자료형(기본자료형. 숫자, 문자, 불)     주소
#   힙      : 순서 X     더 느림     참조자료형(객체자료형. 리스트, 딕셔너리)   값
# => 실제 값은 힙에 저장하고 저장한 주소(레퍼런스) 값을 스택에 기록한다


# 제너레이터(generator) => 이터레이터(iterater)를 직접 만들 때 사용
# yield 키워드 사용 => 함수를 호출해도 함수 내부의 코드가 실행되지 않음
# next() 함수를 사용해 함수 내부 코드 실행 => return 값으로 yield 키워드 뒤에 입력한 값이 출력됨
def test():
    print("호출되었습니다.")
    yield "test"


# print(dir(test()))
print(test())
next(test())

리스트안에딕셔너리 = [{"이름": "홍길동"}, {"이름": "강길동"}]
리스트안에딕셔너리.sort(key=lambda 리스트안에딕셔너리: 리스트안에딕셔너리["이름"])

for 리스트 in 리스트안에딕셔너리:
    print(리스트)


#   스택    : 순서 O     더 빠름     원시자료형(기본자료형. 숫자, 문자, 불)     주소
#   힙      : 순서 X     더 느림     참조자료형(객체자료형. 리스트, 딕셔너리)   값
# => 실제 값은 힙에 저장하고 저장한 주소(레퍼런스) 값을 스택에 기록한다
