import pandas as pd
import folium
import streamlit as st
from streamlit_folium import st_folium

st.title("진주시 CCTV 지도")

# CSV 파일 읽기 (인코딩 주의)
df = pd.read_csv("jinju_cctv.csv", encoding='cp949')

# 지도 생성 (진주시 중심)
m = folium.Map(location=[35.1802, 128.1076], zoom_start=13)

# CSV 파일에서 위도, 경도, 설치장소를 기반으로 마커 표시
for _, row in df.iterrows():
    folium.Marker(
        location=[row['위도'], row['경도']],     # 열 이름이 실제와 다르면 오류나니까 정확히 확인!
        popup=row.get('설치장소', 'CCTV')       # 설치장소 없으면 기본값 'CCTV'
    ).add_to(m)

# Streamlit 앱에 folium 지도 보여주기
st_folium(m, width=700, height=500)
