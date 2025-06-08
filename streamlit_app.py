import pandas as pd
import folium
import streamlit as st
from streamlit_folium import st_folium

# 제목
st.title("진주시 CCTV 지도")

# CSV 파일 불러오기
df = pd.read_csv("data/jinju_cctv.csv")  # 경로는 GitHub에 올린 위치랑 동일해야 함

# 위도, 경도 컬럼명 확인해서 수정해야 할 수도 있음
st.write("데이터 미리보기:")
st.dataframe(df.head())

# 지도 중심 (진주시청 기준)
map_center = [35.1802, 128.1076]
m = folium.Map(location=map_center, zoom_start=13)

# 마커 추가
for _, row in df.iterrows():
    lat = row['위도']
    lon = row['경도']
    name = row.get('설치장소', 'CCTV')
    folium.Marker([lat, lon], popup=name).add_to(m)

# 지도 보여주기
st_folium(m, width=700, height=500)
