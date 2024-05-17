import test_module as test

# 쉬운 모듈 만들기 - 원주율
radius = test.number_input()
print(test.get_circumference(radius))
print(test.get_circle_area(radius))

# 모듈 이름을 출력하는 모듈 만들기
print("# 메인의 __name__ 출력하기")
print(__name__)  # ==> __main__
print()


# ----------------------------------------


# 패키지 내부의 모듈 읽어오기
import test_package.module_a as a
import test_package.module_b as b

# 모듈 내부의 변수 출력
print(a.variable_a)
print(b.variable_b)


# ----------------------------------------


# 패키지 내부의 모듈 모두 읽어오기
from test_package import *

# 모듈 내부 변수 출력
print(module_a.variable_a)
print(module_b.variable_b)


# ----------------------------------------

# 이미지 읽어 들이고 저장하기
from urllib import request

# urlopen() 함수로 웹페이지를 읽음
target = request.urlopen("https://www.hanbit.co.kr/images/common/logo_hanbit.png")
output = target.read()
# print(output)

# write binary[바이너리 쓰기] 모드로
file = open("output.png", "wb")  # => 바이너리 형식으로 씀 "wb"
file.write(output)
file.close()
