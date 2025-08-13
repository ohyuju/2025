import streamlit as st
import random

# 예시 단어장 (단어: 뜻)
word_dict = {
    "apple": "사과",
    "book": "책",
    "cat": "고양이",
    "dog": "개",
    "elephant": "코끼리",
    "flower": "꽃",
    "guitar": "기타",
    "house": "집",
    "ice": "얼음",
    "jungle": "정글"
}

# 단어 리스트 만들기
words = list(word_dict.keys())

st.title("📚 영어 단어 암기 앱")

if "current_word" not in st.session_state:
    st.session_state.current_word = random.choice(words)
    st.session_state.show_answer = False

def next_word():
    st.session_state.current_word = random.choice(words)
    st.session_state.show_answer = False
    st.session_state.user_input = ""

# 현재 단어 보여주기
st.write(f"### 단어: **{st.session_state.current_word}**")

# 사용자 뜻 입력
user_answer = st.text_input("뜻을 입력하세요", key="user_input")

# 정답 확인 버튼
if st.button("정답 확인"):
    st.session_state.show_answer = True

if st.session_state.show_answer:
    correct_meaning = word_dict[st.session_state.current_word]
    if user_answer.strip().lower() == correct_meaning:
        st.success("정답입니다! 🎉")
    else:
        st.error(f"틀렸어요... 정답은 '{correct_meaning}' 입니다.")

    # 다음 단어 버튼
    if st.button("다음 단어"):
        next_word()
