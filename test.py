import streamlit as st
import random

# 카테고리별 메뉴 (10개씩)
menu_dict = {
    "한식": [
        "김치찌개", "된장찌개", "부대찌개", "비빔밥", "불고기",
        "삼겹살", "제육볶음", "순대국밥", "칼국수", "냉면"
    ],
    "중식": [
        "짜장면", "짬뽕", "탕수육", "마파두부", "마라탕",
        "깐풍기", "고추잡채", "유린기", "볶음밥", "군만두"
    ],
    "양식": [
        "피자", "햄버거", "스테이크", "파스타", "리조또",
        "샐러드", "라자냐", "치즈오븐스파게티", "바베큐립", "치킨텐더"
    ],
    "일식": [
        "초밥", "라멘", "우동", "가츠동", "오코노미야키",
        "규동", "사시미", "타코야키", "야끼소바", "가라아게"
    ]
}

# 메뉴별 이미지 (Pixabay 무료 이미지 예시)
menu_images = {
    # 한식
    "김치찌개": "https://cdn.pixabay.com/photo/2020/03/19/17/50/kimchi-stew-4949903_1280.jpg",
    "된장찌개": "https://cdn.pixabay.com/photo/2021/11/17/07/57/soybean-paste-stew-6800886_1280.jpg",
    "부대찌개": "https://cdn.pixabay.com/photo/2022/02/21/02/09/budae-jjigae-7025155_1280.jpg",
    "비빔밥": "https://cdn.pixabay.com/photo/2017/04/11/05/46/bibimbap-2222631_1280.jpg",
    "불고기": "https://cdn.pixabay.com/photo/2016/11/18/15/07/barbecue-1835390_1280.jpg",
    "삼겹살": "https://cdn.pixabay.com/photo/2016/03/05/19/02/samgyeopsal-1238390_1280.jpg",
    "제육볶음": "https://cdn.pixabay.com/photo/2020/06/16/09/43/pork-5305499_1280.jpg",
    "순대국밥": "https://cdn.pixabay.com/photo/2017/09/02/17/10/soup-2703112_1280.jpg",
    "칼국수": "https://cdn.pixabay.com/photo/2020/10/22/12/37/kalguksu-5675733_1280.jpg",
    "냉면": "https://cdn.pixabay.com/photo/2017/01/10/14/01/naengmyeon-1962310_1280.jpg",

    # 중식
    "짜장면": "https://cdn.pixabay.com/photo/2018/04/13/23/06/noodles-3315967_1280.jpg",
    "짬뽕": "https://cdn.pixabay.com/photo/2021/11/13/19/17/chinese-food-6782458_1280.jpg",
    "탕수육": "https://cdn.pixabay.com/photo/2018/11/29/20/09/food-3845255_1280.jpg",
    "마파두부": "https://cdn.pixabay.com/photo/2021/08/03/13/09/mapo-tofu-6518596_1280.jpg",
    "마라탕": "https://cdn.pixabay.com/photo/2022/01/27/07/04/malatang-6974400_1280.jpg",
    "깐풍기": "https://cdn.pixabay.com/photo/2021/07/28/19/28/chinese-food-6503835_1280.jpg",
    "고추잡채": "https://cdn.pixabay.com/photo/2021/08/04/11/59/chinese-food-6521119_1280.jpg",
    "유린기": "https://cdn.pixabay.com/photo/2021/09/08/04/29/fried-chicken-6605639_1280.jpg",
    "볶음밥": "https://cdn.pixabay.com/photo/2017/06/02/18/24/fried-rice-2367880_1280.jpg",
    "군만두": "https://cdn.pixabay.com/photo/2020/03/02/18/32/dumplings-4894032_1280.jpg",

    # 양식
    "피자": "https://cdn.pixabay.com/photo/2017/12/09/08/18/pizza-3007395_1280.jpg",
    "햄버거": "https://cdn.pixabay.com/photo/2014/10/23/18/05/burger-500054_1280.jpg",
    "스테이크": "https://cdn.pixabay.com/photo/2015/03/26/09/41/steak-690128_1280.jpg",
    "파스타": "https://cdn.pixabay.com/photo/2017/08/07/07/44/pasta-2605561_1280.jpg",
    "리조또": "https://cdn.pixabay.com/photo/2016/02/11/18/14/risotto-1190444_1280.jpg",
    "샐러드": "https://cdn.pixabay.com/photo/2017/01/03/19/54/salad-1957534_1280.jpg",
    "라자냐": "https://cdn.pixabay.com/photo/2018/01/25/10/14/lasagna-3107481_1280.jpg",
    "치즈오븐스파게티": "https://cdn.pixabay.com/photo/2016/03/05/22/46/spaghetti-1238431_1280.jpg",
    "바베큐립": "https://cdn.pixabay.com/photo/2017/06/02/17/48/barbecue-2367832_1280.jpg",
    "치킨텐더": "https://cdn.pixabay.com/photo/2015/04/08/13/13/chicken-71275_1280.jpg",

    # 일식
    "초밥": "https://cdn.pixabay.com/photo/2016/03/05/19/02/sushi-1238390_1280.jpg",
    "라멘": "https://cdn.pixabay.com/photo/2018/10/12/16/33/ramen-3742816_1280.jpg",
    "우동": "https://cdn.pixabay.com/photo/2017/05/06/02/12/udon-2295623_1280.jpg",
    "가츠동": "https://cdn.pixabay.com/photo/2021/05/27/07/35/katsudon-6289140_1280.jpg",
    "오코노미야키": "https://cdn.pixabay.com/photo/2020/10/23/05/31/okonomiyaki-5677656_1280.jpg",
    "규동": "https://cdn.pixabay.com/photo/2020/12/06/13/46/gyudon-5808502_1280.jpg",
    "사시미": "https://cdn.pixabay.com/photo/2016/03/05/19/02/sashimi-1238389_1280.jpg",
    "타코야키": "https://cdn.pixabay.com/photo/2017/09/05/20/28/takoyaki-2717993_1280.jpg",
    "야끼소바": "https://cdn.pixabay.com/photo/2020/04/17/16/06/yakisoba-5055020_1280.jpg",
    "가라아게": "https://cdn.pixabay.com/photo/2021/02/23/10/07/japanese-food-6044366_1280.jpg",
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
    img_url = menu_images.get(st.session_state.current_menu)
    if img_url:
        st.image(img_url, width=350, caption=st.session_state.current_menu)
    else:
        st.info("해당 메뉴의 이미지는 준비되지 않았습니다.")
