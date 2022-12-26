import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 출생률 데이터 읽기
df = pd.read_csv("https://raw.githubusercontent.com/datasets/baby-names/master/data/south-korea/2016/2016-baby-names-Korea.csv")

# 출생률 시각화
plt.plot(df["year"], df["ratio"])
plt.xlabel("년도")
plt.ylabel("출생률")

# 시각화 결과 출력
st.pyplot()
