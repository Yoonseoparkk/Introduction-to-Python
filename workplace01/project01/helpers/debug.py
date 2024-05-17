# 사용자 함수


def pp(a):
    print(a)


def ppt(a):
    print("타입은 ", type(a))
    print("값은 ", a)


def pt(a):
    print("==> ", type(a))


def plen(a):
    print(len(a))


def inch_to_cm(raw_data):
    # inch = float(input("inch 단위의 숫자를 입력해주세요: "))
    inch = float(raw_data)
    cm = inch * 2.54  # float
    return cm


def cm_to_inch(raw_data):
    inch = float(raw_data) / 2.54
    cm = inch * 2.54  # float
    return inch


def plen2(a):
    print(len(a))


def plen3(a):
    print(len(a))
