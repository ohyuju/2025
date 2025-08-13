import streamlit as st
import pandas as pd
import pydeck as pdk

# 예시 영화 데이터 (영화명, 장르, 위도, 경도)
data = [
    {"title": "La La Land", "genre": "Musical", "lat": 34.0522, "lon": -118.2437},  # LA
    {"title": "Midnight in Paris", "genre": "Romance", "lat": 48.8566, "lon": 2.3522},  # Paris
    {"title": "Inception", "genre": "Sci-Fi", "lat": 37.7749, "lon": -122.4194},  # San Francisco
    {"title": "Amélie", "genre": "Romance", "lat": 48.8566, "lon": 2.3522},  # Paris
    {"title": "The Dark Knight", "genre": "Action", "lat": 41.8781, "lon": -87.6298},  # Chicago
    {"title": "Lost in Translation", "genre": "Drama", "lat": 35.6895, "lon": 139.6917},  # Tokyo
]

df = pd.DataFrame(data)

st.title("🎬 영화 추천 맵")

# 장르 선택
genres = df['genre'].unique()
selected_genre = st.selectbox("원하는 장르를 선택하세요", genres)

# 선택한 장르 영화만 필터링
filtered_df = df[df['genre'] == selected_genre]

st.write(f"### {selected_genre} 장르 영화들 위치")

if filtered_df.empty:
    st.write("해당 장르의 영화가 없습니다.")
else:
    # 지도 표시
    st.map(filtered_df.rename(columns={"lat": "latitude", "lon": "longitude"}))

    # 영화 리스트 보여주기
    for idx, row in filtered_df.iterrows():
        st.write(f"- {row['title']} (위치: {row['lat']}, {row['lon']})")
