import streamlit as st
import random

# 카테고리별 메뉴
menu_dict = {
    "한식": ["김치찌개", "된장찌개", "부대찌개", "비빔밥", "불고기", "삼겹살", "제육볶음", "순대국밥", "칼국수", "냉면"],
    "중식": ["짜장면", "짬뽕", "탕수육", "마파두부", "마라탕"],
    "양식": ["피자", "햄버거", "스테이크", "파스타", "리조또"],
    "일식": ["초밥", "라멘", "우동", "가츠동", "오코노미야키"]
}

st.title("🍚 오늘 뭐 먹지? - 랜덤 밥 메뉴 추천기 🍴")
st.write("카테고리를 먼저 선택한 뒤 메뉴를 추천받아보세요!")

# 세션 상태 초기화
if "current_menu" not in st.session_state:
    st.session_state.current_menu = None
if "selected_category" not in st.session_state:
    st.session_state.selected_category = None

# 카테고리 선택
category = st.selectbox("🍴 카테고리를 선택하세요:", list(menu_dict.keys()))

# 버튼 배치
col1, col2 = st.columns(2)

# 추천받기 버튼
with col1:
    if st.button("✅ 메뉴 추천받기"):
        st.session_state.selected_category = category
        st.session_state.current_menu = random.choice(menu_dict[category])

# 싫어요 버튼
with col2:
    if st.button("❌ 싫어요 (다시 뽑기)"):
        if st.session_state.current_menu and st.session_state.selected_category:
            category_menus = menu_dict[st.session_state.selected_category]
            new_choice = random.choice([m for m in category_menus if m != st.session_state.current_menu])
            st.session_state.current_menu = new_choice
        else:
            st.warning("먼저 메뉴 추천부터 받아주세요!")

# 현재 메뉴 보여주기
if st.session_state.current_menu:
    st.success(f"오늘의 추천 메뉴는 👉 **{st.session_state.current_menu}** 🍽️")
