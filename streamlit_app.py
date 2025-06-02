
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

