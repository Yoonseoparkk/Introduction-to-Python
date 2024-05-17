# 쉬운 모듈 만들기 - 원주율
PI = 3.141592  # 상수


def number_input():
    output = input("숫자 입력:")
    return float(output)


def get_circumference(radius):
    return 2 * PI * radius


def get_circle_area(radius):
    return PI * radius * radius


if __name__ == "__main__":  # 모듈이 메인(엔트리포인트)일 때만 작동
    print(get_circumference(5))
    print(get_circle_area(5))


# 모듈 이름을 출력하는 모듈 만들기
print("# 모듈의 __name__ 출력하기")
print(__name__)  # ==> test_module (모듈 이름 출력)
print()
