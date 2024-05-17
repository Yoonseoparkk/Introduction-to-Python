class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_student_info(self):
        print(f"{self.name}{self.korean}{self.math}{self.english}{self.science}")

    def sum(self):
        sum = self.korean + self.math + self.english + self.science
        return sum

    def average(self):
        avg = self.korean + self.math + self.english + self.science / 4
        return avg

    def to_string(self):
        결과 = f"{self.name} 학생의 성적 총합은 {self.sum()}, 평균은 {self.average()}입니다."
        return 결과
