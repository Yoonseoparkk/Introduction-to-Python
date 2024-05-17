from student.getdata import jsonplaceholder
from student.getstudentobj import Student
from student.getteacher import Student
from student.getteacher import Teacher
from mathh.mathm import Mathc

# if __name__ == "__main__":
#     students = jsonplaceholder()
#     # print(type(students))
#     # print(students[0]["name"])
#     # print("id", "name", "username", "email")
#     for s in students:
#         # print(f"{s["id"]} {s["name"]} {s["username"]} {s["email"]}")
#         pass

# s1 = Student("홍길동", 45, 45, 45, 45)
# s2 = Student("김길동", 45, 45, 45, 45)
# s3 = Student("이길동", 45, 45, 45, 45)
# s4 = Student("박길동", 45, 45, 45, 45)


# s1.get_student_info()
# print(s1.to_string())
# print(isinstance(s1, Student))

# classroom = [Student(), Student(), Student(), Student(), Teacher()]

# for person in classroom:
#     if isinstance(person, Student):
#         print("학생이네요")
#         person.study()
#     if isinstance(person, Teacher):
#         print("선생님이네요")
#         person.teach()


# 활용되지 않는 메모리 공간
# 가비지 컬렉터(Garbage Collector) => 도달 가능성
# 적극적으로, 직접적으로 하는 것이 X


# class Test:
#     def __init__(self, name):
#         self.name = name
#         print("{} - 생성되었습니다".format(self.name))

#     def __del__(self):
#         print("{} - 파괴되었습니다".format(self.name))


# # Test("A")
# # Test("B")
# # Test("C")


# @property  # 겟터
# def radius(self):
#     return self.__name


# def __str__(self):
#     return "사용자 테이블입니다."

# set 내포(conprehension) & dictionary 내포
a = {f"{item}:": item * 10 for item in range(0, 10)}
print(a)

# 다음시간 => streamlit 배우기
