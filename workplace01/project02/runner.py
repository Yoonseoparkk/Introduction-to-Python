from helpers.debug import *
import datetime

# 조건문의 기본 사용
if __name__ == "__main__":
    입력받은값 = int(input("숫자를 입력하세요"))
    if 입력받은값 > 0:  # T or F
        print(입력받은값, "은(는) 양수입니다.")

    elif 입력받은값 < 0:
        print(입력받은값, "은(는) 음수입니다.")

    else:
        pp("0 입니다.")

# 날짜/시간 출력하기
now = datetime.datetime.now()  # 현재 날짜/시간
print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")

print(
    "{}년 {}월 {}일 {}시 {}분 {}초".format(
        now.year, now.month, now.day, now.hour, now.minute, now.second
    )
)

if now.hour < 12:
    print("현재 시각은 {}시로 오전입니다!".format(now.hour))
elif now.hour >= 12:
    print("현재 시각은 {}시로 오후입니다!".format(now.hour))

# 학점 구하기
score = int(input("0~100 사이 점수를 입력하세요: "))
if 0 <= score <= 100:
    if 90 <= score <= 100:
        print("당신의 학점은 A 입니다.")
    elif 80 <= score < 90:
        print("당신의 학점은 B 입니다.")
    elif 70 <= score < 80:
        print("당신의 학점은 C 입니다.")
    elif 60 <= score < 70:
        print("당신의 학점은 B 입니다.")
    else:
        print("당신의 학점은 F 입니다.")
else:
    print("0~100 사이 점수를 입력하세요.")


# 짝수와 홀수 구분하기
# 문자열 1
number = input("정수를 입력하세요: ")
last_character = number[-1]  # 마지막 자리 숫자 추출

if last_character in "02468":
    print("{}은(는) 짝수입니다.".format(number))
else:
    print("{}은(는) 홀수입니다.".format(number))

# 문자열 2
if (
    last_character == "0"
    or last_character == "2"
    or last_character == "4"
    or last_character == "6"
    or last_character == "8"
):
    print("{}은(는) 짝수입니다.".format(number))
else:
    print("{}은(는) 홀수입니다.".format(number))


# 짝수와 홀수 구분하기 - 숫자
if int(number) % 2 == 0:
    print("{}은(는) 짝수입니다.".format(number))
else:
    print("{}은(는) 홀수입니다.".format(number))

# pass 키워드
# 빈칸 대신 입력해 두고 추후 코드를 작성하거나 할 때 사용

if 1:
    pass
elif 0:
    pass
elif 0:
    pass


def func():
    pass


class Passss:
    def __init__(self):  # 기본값 설정하기 initialize
        pass

    def asd(self):
        pass

    def asdasd(self):
        pass

    def asdasdasd(self):
        pass


# 자료구조와 결합된 반복문 = 중요
# 배열 Array => 처음 만들어질 때부터 크기가 정해져 있음. 아이템의 추가 및 삭제
# 컨테이너 객체 Container => 성격이 비슷한 것들이 담겨져 있는 타입
# 이터러블 객체 Iterable => 반복시킬 수 있음
# 리스트 List => 반복문과 결합

리스트 = []
리스트 = list()
리스트 = ["a", "a", "a"]
리스트 = [1, 2, 3, 4, 5]
리스트[0]  # 1 => 첫번째 요소
리스트[0] = 100  # 리스트의 0번째 요소를 100으로 변경
print(리스트)

과일들 = ["사과", "배", "딸기", "포도", "망고"]
과일들[0] = "apple"
print(과일들)
print(len(과일들))
과일들.append("키위")
print(과일들)
과일들.insert(0, "바나나")
과일들.extend([0, "바나나", "asdasd"])

# 리스트 요소 제거
del 과일들[1:7]  # del 연산자
과일들.pop(2)  # pop 메소드
과일들.clear()  # 모두 제거
리스트 = [1, 2, 3, 1]
리스트.remove(1)
# => [2, 3, 1] => 앞에 있는 요소 제거. 여러 값 제거하려면 반복문과 조합해야 함

# 리스트 역순
과일들.reverse()
과일들[0:6:-1]  # 리스트 슬라이싱 리스트[시작_인덱스:끝_인덱스:step(=1)]
과일들[::-1]  # 전부

# 리스트 정렬
리스트 = [1, 2, 3]
리스트.sort()  # 오름차순
리스트.sort(reverse=False)  # 오름차순
리스트.sort(reverse=True)  # 내림차순
print(리스트)

# C 스타일 for 반복문
리스트 = [1, 2, 3, 4, 5]
# for (i=0; i<len(리스트); i++) {
#     print(리스트[i])
# }

# 파이썬 for 반복문
# item in items
for i in range(0, len(리스트), 1):
    print(f"{i+1}번째 요소는 {리스트[i]}")

for 숫자 in 리스트:
    print(숫자)

# enumerate => index와 함께 표시. 객체는 tuple
for idx, 숫자 in enumerate(리스트):
    print(idx, 숫자)

for idx, 과일 in zip(["빨간", "하얀"], ["사과", "배"]):
    print(idx, 과일)

# -------------------------------------------------------

빈리스트 = []
for i in range(1, 101):
    빈리스트.append(i)
print(빈리스트)


array = [123, 245, 56, 1, 49]
array.sort()
for i in array:
    print(i)

for character in "안녕하세요":
    print(character)

# 구구단 출력하기
for i in range(2, 10):
    print("<< {} 단 >>".format(i))
    print(f"{i}단".center(20, "="))
    for j in range(1, 10):
        print(i, "*", j, "=", i * j)
    print("")

# List Comprehension --> 축약문
# (+ tuple, set, dictionary..)
빈리스트 = [x for x in range(0, 10) if x >= 4]
print(빈리스트)


# list 인덱스 - 중복 허용
# tuple 인덱스 - 값의 불변성, immutable 순서 보장
# set 인덱스 - 중복을 허용하지 않음, 순서 보장하지 않음
# dictionary (key:value) - 순서 보장하지 않음

리스트 = ["사과", "사과", "딸기"]
중복제거된리스트 = list(set(리스트))
print(중복제거된리스트)

딕셔너리 = {"이름": "홍길동", "나이": 23}
나이 = 딕셔너리["나이"]
print(나이)
print(딕셔너리.keys())

# dictionary in list
리스트속딕셔너리 = [
    {
        "postId": 1,
        "id": 1,
        "name": "id labore ex et quam laborum",  # 로렘입숨, 로렘픽숨
        "email": "Eliseo@gardner.biz",
        "body": "laudantium enim quasi est quidem magnam voluptate ipsam eos",
    },
    {
        "postId": 1,
        "id": 2,
        "name": "quo vero reiciendis velit similique earum",
        "email": "Jayne_Kuhic@sydney.com",
        "body": "est natus enim nihil est dolore omnis voluptatem numquam",
    },
]

# 두번째 사람 이메일 주소 출력하기
address = 리스트속딕셔너리[1]["email"]
print(address)

# 첫번째 사람 id를 30으로 변경
리스트속딕셔너리[0]["id"] = 30
print(리스트속딕셔너리[0]["id"])

# 변경된 리스트속딕셔너리 출력
print(리스트속딕셔너리)

# 딕셔너리에 값 추가/제거
dic = {"name": "홍길동", "age": 23, "gender": "남"}
dic["height"] = 170
print(dic)
del dic["name"]
print(dic)

# 딕셔너리 key 확인 및 value 구하기
딕셔너리 = {
    "postId": 1,
    "id": 1,
    "name": "id labore ex et quam laborum",
    "email": "Eliseo@gardner.biz",
    "body": "laudantium",
}
ads = 딕셔너리.get("id")
print(ads)
ads = 딕셔너리.get("abc")
print(ads)

print(딕셔너리.keys())
print(딕셔너리.values())
print(딕셔너리.items())  # dict_items([(k,v), (k,v), ...])

# 딕셔너리 반복문
for k in 딕셔너리:
    print(딕셔너리[k])
    print(딕셔너리.get(k))

for k, v in 딕셔너리.items():
    print(f"키는 {k}이고 값은 {v}입니다.")

# ****************** 숫자 몇 번 등장하는지 출력하기 예제 ******************
numbers = [1, 2, 1, 2, 4, 6]
counter = {}  # 딕셔너리

# solution 1
for num in numbers:
    if num in counter:
        counter[num] += 1
    else:
        counter[num] = 1
print(counter)
counter.clear()

# solution 2
for num in numbers:
    counter[num] = numbers.count(num)
print(counter)

# 범위 자료형 range
#            시작값 끝값 스텝
# for i in range(0, len(), 1):
