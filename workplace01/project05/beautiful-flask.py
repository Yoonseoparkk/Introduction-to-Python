from flask import Flask
from urllib import request
from bs4 import BeautifulSoup

# 웹 서버 생성
app = Flask(__name__)


@app.route("/") # 데코레이션
def hello():
    # urlopen() 함수로 기상청의 전국 날씨 읽어오기
    target = request.urlopen(
        "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
    )

    # BeautifulSoup 사용해 웹 페이지 분석
    soup = BeautifulSoup(target, "html.parser")

    # location 태그 찾기
    output = ""
    for loc in soup.select("location"):
        output += f"<h3>{loc.select_one("city").string}</h3>"
        output += f"날씨: {loc.select_one("wf").string}<br/>"
        output += f"최저/최고 기온: {loc.select_one("tmn").string}/{loc.select_one("tmx").string}"
        output += "<hr/>"
    return output
