import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np


# ---------- 폰트 파일 경로 ----------
# font_path = "/Library/Fonts/YourFont.ttf"
font_path = r"C:\Windows\Fonts\malgun.ttf"
font_name = plt.matplotlib.font_manager.FontProperties(fname=font_path).get_name()

plt.rcParams["font.family"] = font_name
plt.rc("font", family=font_name)
plt.rcParams["axes.unicode_minus"] = False
# -----------------------------------

# DataFrame 생성
data = pd.DataFrame(
    {
        "이름": ["홍길동", "김길동", "이길동", "박길동"],
        "나이": [25, 26, 30, 27],
        "몸무게": [50.5, 68.7, 66.9, 75.0],
    }
)

st.dataframe(data, use_container_width=True)

fig, ax = plt.subplots()
ax.bar(data["이름"], data["나이"])
st.pyplot(fig)

barplot = sb.barplot(
    x="이름", y="나이", data=data, ax=ax, palette="Set2", legend="auto"
)
# legend=전설, 범례

fig = barplot.get_figure()
st.pyplot(fig)
