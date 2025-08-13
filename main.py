import streamlit as st

st.title("✨ MBTI & 혈액형별 특이한 직업 추천 앱 ✨")

# MBTI 선택지
mbti_options =
   ["INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"]
# 혈액형 선택지
blood_types = ["A", "B", "AB", "O"]

# 직업 추천 데이터 예시 (조합별 간단 예)
recommendations = {
    ("INTJ", "A"): "연구원, 데이터 과학자",
    ("INTJ", "B"): "프로그래머, 전략 컨설턴트",
    ("INTJ", "AB"): "과학 작가, 시스템 분석가",
    ("INTJ", "O"): "기업가, 금융 애널리스트",

    ("ENFP", "A"): "마케팅 전문가, 방송인",
    ("ENFP", "B"): "여행 가이드, 이벤트 기획자",
    ("ENFP", "AB"): "연예인, 광고 기획자",
    ("ENFP", "O"): "강사, 사회 운동가",

    # 기본값 (없는 조합일 때)
    "default": "프리랜서, 창업가, 컨텐츠 크리에이터"}

# 사용자 입력
selected_mbti = st.selectbox("MBTI를 선택하세요", mbti_options)
selected_blood = st.selectbox("혈액형을 선택하세요", blood_types)

if st.button("추천 직업 보기"):
    key = (selected_mbti, selected_blood)
    job = recommendations.get(key, recommendations["default"])
    st.write(f"### 당신에게 어울리는 특이한 직업 추천:")
    st.write(job)
