import streamlit as st
import random

# 카테고리별 메뉴
menu_dict = {
    "한식": ["김치찌개","된장찌개","부대찌개","비빔밥","불고기","삼겹살","제육볶음","순대국밥","칼국수","냉면"],
    "중식": ["짜장면","짬뽕","탕수육","마파두부","마라탕","깐풍기","고추잡채","유린기","볶음밥","군만두"],
    "양식": ["피자","햄버거","스테이크","파스타","리조또","샐러드","라자냐","치즈오븐스파게티","바베큐립","치킨텐더"],
    "일식": ["초밥","라멘","우동","가츠동","오코노미야키","규동","사시미","타코야키","야끼소바","가라아게"]
}

# 난이도를 별점 5개로 변환
difficulty_dict = {
    "김치찌개":2, "된장찌개":2, "부대찌개":3, "비빔밥":2, "불고기":3,
    "삼겹살":2, "제육볶음":3, "순대국밥":3, "칼국수":2, "냉면":2,
    "짜장면":3, "짬뽕":3, "탕수육":5, "마파두부":3, "마라탕":5,
    "깐풍기":5, "고추잡채":3, "유린기":5, "볶음밥":2, "군만두":3,
    "피자":3, "햄버거":2, "스테이크":3, "파스타":3, "리조또":5,
    "샐러드":2, "라자냐":5, "치즈오븐스파게티":3, "바베큐립":5, "치킨텐더":2,
    "초밥":5, "라멘":3, "우동":2, "가츠동":3, "오코노미야키":3,
    "규동":2, "사시미":5, "타코야키":3, "야끼소바":2, "가라아게":3
}

# 난이도 이름
difficulty_name = {2:"쉬움",3:"보통",5:"어려움"}

# 별점으로 변환 함수
def stars(n):
    return "★"*n + "☆"*(5-n)

st.title("🍚 오늘 뭐 먹지? - 랜덤 밥 메뉴 추천기 🍴")
st.write("카테고리와 난이도를 선택한 뒤 메뉴를 추천받아보세요!")

# 세션 상태 초기화
if "current_menu" not in st.session_state:
    st.session_state.current_menu = None
if "selected_category" not in st.session_state:
    st.session_state.selected_category = None
if "selected_difficulty" not in st.session_state:
    st.session_state.selected_difficulty = None

# 카테고리 선택
category = st.selectbox("🍴 카테고리를 선택하세요:", list(menu_dict.keys()))

# 난이도 필터
difficulty_options = ["전체", "쉬움", "보통", "어려움"]
selected_difficulty = st.selectbox("⚡ 요리 난이도를 선택하세요:", difficulty_options)

# 버튼 배치
col1, col2 = st.columns(2)

with col1:
    if st.button("✅ 메뉴 추천받기"):
        st.session_state.selected_category = category
        st.session_state.selected_difficulty = selected_difficulty
        # 필터 적용
        menus = menu_dict[category]
        if selected_difficulty != "전체":
            menus = [m for m in menus if difficulty_name.get(difficulty_dict[m]) == selected_difficulty]
        if menus:
            st.session_state.current_menu = random.choice(menus)
        else:
            st.warning("선택한 난이도에 맞는 메뉴가 없습니다!")
            st.session_state.current_menu = None

with col2:
    if st.button("❌ 싫어요 (다시 뽑기)"):
        if st.session_state.current_menu and st.session_state.selected_category:
            menus = menu_dict[st.session_state.selected_category]
            if st.session_state.selected_difficulty != "전체":
                menus = [m for m in menus if difficulty_name.get(difficulty_dict[m]) == st.session_state.selected_difficulty]
            if menus:
                choices = [m for m in menus if m != st.session_state.current_menu]
                if choices:
                    st.session_state.current_menu = random.choice(choices)
                else:
                    st.warning("더 이상 새로운 메뉴가 없습니다!")
            else:
                st.warning("선택한 난이도에 맞는 메뉴가 없습니다!")
                st.session_state.current_menu = None
        else:
            st.warning("먼저 메뉴 추천부터 받아주세요!")

# 현재 메뉴 + 별점 보여주기
if st.session_state.current_menu:
    score = difficulty_dict.get(st.session_state.current_menu, 0)
    st.success(f"오늘의 추천 메뉴는 👉 **{st.session_state.current_menu}** 🍽️")
    st.info(f"🔹 요리 난이도: {stars(score)}")
