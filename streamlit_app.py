import pandas as pd
import folium
import streamlit as st
from streamlit_folium import st_folium

st.title("진주시 CCTV 지도")

# 수정된 경로!
df = pd.read_csv("jinju_cctv.csv")

# 진주시 중심 좌표
m = folium.Map(location=[35.1802, 128.1076], zoom_start=13)

# 위도, 경도 컬럼 이름이 실제 CSV에 맞는지 확인해
for _, row in df.iterrows():
    folium.Marker(
        location=[row['위도'], row['경도']],
        popup=row.get('설치장소', 'CCTV')
    ).add_to(m)

st_folium(m, width=700, height=500)
