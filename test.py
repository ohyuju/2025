import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="약물 복용 및 정보 앱", layout="wide")

st.title("💊 약물 복용 및 정보 관리 앱")

# 📌 샘플 약물 데이터 (실제라면 약학 데이터베이스 API 연결 가능)
drug_info = {
    "타이레놀": {"효능": "진통·해열제", "주의사항": "간 손상 위험, 과다 복용 금지"},
    "부루펜": {"효능": "소염·진통·해열제", "주의사항": "위장 장애 주의, 공복 복용 피하기"},
    "판콜": {"효능": "감기 증상 완화", "주의사항": "다른 감기약과 중복 복용 주의"},
    "지르텍": {"효능": "알레르기 치료제", "주의사항": "졸음 유발 가능, 운전 주의"},
}

# -------------------
# 1. 약물 검색 기능
# -------------------
st.subheader("🔎 약물 정보 검색")
search_drug = st.text_input("찾고 싶은 약물 이름을 입력하세요")

if search_drug:
    if search_drug in drug_info:
        st.success(f"**{search_drug}**")
        st.write(f"효능: {drug_info[search_drug]['효능']}")
        st.write(f"주의사항: {drug_info[search_drug]['주의사항']}")
    else:
        st.error("❌ 데이터베이스에 없는 약물입니다.")

# -------------------
# 2. 복용 기록 관리
# -------------------
st.subheader("📝 오늘의 약물 복용 기록")
if "log" not in st.session_state:
    st.session_state["log"] = []

drug_taken = st.selectbox("복용한 약물을 선택하세요", ["선택 안 함"] + list(drug_info.keys()))
if st.button("복용 기록 추가"):
    if drug_taken != "선택 안 함":
        st.session_state["log"].append({"약물": drug_taken, "시간": datetime.now().strftime("%Y-%m-%d %H:%M")})
        st.success(f"{drug_taken} 복용 기록이 저장되었습니다.")

# -------------------
# 3. 기록 보기
# -------------------
st.subheader("📊 복용 기록 보기")
if st.session_state["log"]:
    df = pd.DataFrame(st.session_state["log"])
    st.table(df)
else:
    st.info("아직 복용 기록이 없습니다.")

