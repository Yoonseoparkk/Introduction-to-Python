from flask import Flask

app = Flask(__name__)
app = Flask("__main__")
print(type(app))
print(dir)


# 공유기 라우터 - 경로 처리
@app.route("/")  # 루트 경로
def hello():
    return "<h1>안녕하세요</h1>"


@app.route("/a")  # 루트 경로
def hello2():
    return "<h1>안녕하세요2</h1>"


# localhost = 127.0.0.1

# @어노테이션 (annotaion) : 상황에 따라 생략 가능. 컴파일러를 명시적으로 알려줌.

# @데코레이터 (decorator)
# 미리 만들어둔 데코레이터 & 내가 만들어쓰는 데코레이터
# 함수를 감싸줘서 기능을 추가해준다 => 함수를 변경해준다
