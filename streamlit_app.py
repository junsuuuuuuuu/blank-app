
import streamlit as st
st.set_page_config(page_title="문서 작성 예제", layout="centered")

# 제목
st.title("안녕 난 준수")

# 섹션
st.header("1. 기본 텍스트 출력")

st.write("이것은 `st.write()`를 사용한 텍스트입니다.")
st.text("이것은 형식 없는 텍스트입니다.")

# 마크다운 사용
st.markdown("**굵은 글씨**와 *기울임 글씨* 사용하기")
st.markdown("> 인용구 스타일")

# 코드 블록 출력
st.code("""
def hello():
    print("Hello, Streamlit!")
""", language='python')

# 표 출력
st.header("2. 표 출력")
import pandas as pd
df = pd.DataFrame({
    "이름": ["홍길동", "이몽룡"],
    "나이": [29, 34]
})
st.dataframe(df)

# 이미지 출력
st.header("3. 이미지 출력")

st.image("https://i.namu.wiki/i/4El7Omx8MUNbvgPh06rSi50cTR5HI9QF3x8KuRAibfxEj6z-3Yqo19bi7pFUwyo73MaFIyibjmyibkq3Z8yzuXfFpPZ4siVz_OjZhEsyDmlSc6sb4Bq5OFsqW28zfqBWKgg5pVqwTIt4tcB6vjVR_Q.webp", width=300)



import pandas as pd
import folium

# CSV 파일 경로
file_path = '/mnt/data/18cf1d31-cf32-40a4-b495-28c4ebcbd638.csv'

# CSV 파일 불러오기
df = pd.read_csv(file_path)

# 위도, 경도 컬럼명 확인 (예시로 '위도', '경도'라고 가정함. 다르면 수정 필요)
print(df.columns)  # 컬럼 확인용

# 지도의 중심 설정 (진주시청 기준)
map_center = [35.1802, 128.1076]
m = folium.Map(location=map_center, zoom_start=13)

# CCTV 위치 마커로 추가
for idx, row in df.iterrows():
    lat = row['위도']  # 컬럼명 확인 후 수정
    lon = row['경도']
    name = row.get('설치장소', 'CCTV')  # 설치장소 컬럼명도 다를 수 있음
    folium.Marker([lat, lon], popup=name).add_to(m)

# 지도 저장
m.save('jinju_cctv_map.html')
