# 모듈 읽어오기
from urllib import request
from bs4 import BeautifulSoup  # class는 대문자

# urloepn() 함수로 기상청의 전국 날씨 읽어오기
target = request.urlopen(
    "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
)

# BeautifulSoup를 사용해 웹 페이지 분석
soup = BeautifulSoup(
    target, "html.parser"
)  # BeautifulSoup()은 단순한 함수가 아니라 클래스의 생성자

# # location 태그 찾기 => 지역마다 첫번째 정보만 불러옴
# for loc in soup.select("location"):
#     print("날짜:", loc.select_one("tmEf").string)
#     print("도시:", loc.select_one("city").string)
#     print("날씨:", loc.select_one("wf").string)
#     print("최저기온:", loc.select_one("tmn").string)
#     print("최고기온:", loc.select_one("tmx").string)
#     print()


# select() 함수 : 태그를 여러 개 선택할 때
# select_one() 함수 : 하나만 선택할 때


# 지역마다 날짜별 모든 정보 불러오기 코드   *************
for loc in soup.select("location"):
    print(f"{loc.string}".center(20, "*"))
    for data in loc.select("data"):
        print("날짜:", data.tmef.string)
        print("도시:", loc.city.string)
        print("날씨:", data.wf.string)
        print("최저기온:", data.tmn.string)
        print("최고기온:", data.tmx.string)
        print()
