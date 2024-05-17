import streamlit as st
import numpy as np
import pandas as pd
import datetime
from datetime import datetime as dt


class View:
    def __init__(self, appname):
        st.title(appname)
        st.title(":sunglasses:")
        st.header("데이터를 보여드릴게요! :sparkles:")
        st.caption("이미지입니다. :sparkles:")
        sample_code = """
def func01():
    print("조회됨")
"""
        st.code(sample_code, language="python")
        st.text("제가 만들 모델은 ~~~~ 입니다.")
        st.html("<h1>html</h1>")
        st.markdown("# MarkDown")
        st.markdown(
            "텍스트의 색상을 :green[초록색]으로, 그리고 :blue[파란색] 볼트체로 설정할 수 있습니다."
        )
        st.markdown(
            ":green[$\sqrt{x^2+y^2}=1$] 와 같이 latex 문법의 수식 표현도 가능합니다."
        )
        st.latex(r"\sqrt{x^2+y^2}=1")
        st.html("<hr>")

        # 판다스가 제공하는 자료구조 Series, DataFrame
        # pd == DataFrame
        # 넘파이의 nd.array 자료구조 Series
        # 엑셀처럼 행과 열로 되어있다

        st.title("데이터 프레임")

        dataframe = {"first column": [1, 2, 3, 4], "second column": [10, 20, 30, 40]}
        df = pd.DataFrame(dataframe)

        st.dataframe(dataframe, use_container_width=False)
        st.table(dataframe)

        # 벡터 메트릭스 텐서
        # st.metric(label="온도", value="10'C", delta="1.2'C")
        # st.metric(label="삼성전자", value="61,000 원", delta="-1,200 원")

        col1, col2, col3 = st.columns(3)
        col1.metric(label="삼성전자", value="61,000 원", delta="-1,200 원")
        col2.metric(label="LG전자", value="42,000 원", delta="8,000 원")
        col3.metric(label="대우전자", value="38,000 원", delta="-400 원")

        # -------------------------------

        button = st.button("눌러주세요")
        button2 = st.button("되돌리기")
        if button:
            st.write(":blue[버튼]이 눌렸습니다 :sparkles:")
        if button2:
            pass

        # 파일 다운로드
        # 샘플 데이터

        st.download_button(
            label="csv로 다운로드",
            data=df.to_csv(),
            file_name="sample.csv",
            mime="text/csv",
        )

        agree = st.checkbox("동의?")

        if agree:
            st.write("감사합니다.:100:")

        mbti = st.radio("ISTJ", ("asd", "sss"), index=1)
        mbti2 = st.selectbox("mbti?", ("ISTJ", "ISTP", "ESTJ", "ESTP"), index=0)
        mbti3 = st.multiselect("mbti?", ("ISTJ", "ISTP", "ESTJ", "ESTP"))
        print(mbti3)

        values = st.slider("선택해주세요", 0.0, 100.0)

        start_time = st.slider(
            "언제 약속을 잡는 것이 좋을까요?",
            min_value=dt(2020, 1, 1, 0, 0),
            max_value=dt(2020, 1, 7, 23, 0),
            value=dt(2020, 1, 3, 12, 0),
            step=(datetime.timedelta(hours=1)),
            format="MM/DD/YY - HH:mm",
        )
        st.write("선택한 약속 시간:", start_time)

        title = st.text_input(label="나이 입력", placeholder=20)
        title = st.number_input(
            label="나이 입력", min_value=0, max_value=100, placeholder=20, step=1
        )
