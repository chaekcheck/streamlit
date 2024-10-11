import streamlit as st
import pandas as pd
import pymysql

def app():
    st.header("📚책쳌(Chaek Check)", divider="rainbow")
    st.subheader("나의 서재")

    # 데이터베이스 연결 함수
    def get_db_connection():
        return pymysql.connect(
            host='13.124.235.119',
            port=3307,
            user='root',
            passwd='cheakcheck',
            database='CKCKDB',
            charset='utf8mb4'
        )

    connection = get_db_connection()
    cursor = connection.cursor()

    # 책 목록 쿼리 실행
    query = "SELECT title, author FROM sample_user"
    cursor.execute(query)
    rows = cursor.fetchall()

    df = pd.DataFrame(rows, columns=['Title', 'Author'])

    # 체크박스 상태를 저장할 세션 스테이트 초기화
    if 'selected_books' not in st.session_state:
        st.session_state.selected_books = []

    # 데이터프레임과 체크박스 표시
    st.write("보유한 책을 선택하세요:")
    for index, row in df.iterrows():
        # 각 책에 대해 체크박스 생성
        if st.checkbox(f"{row['Title']} - {row['Author']}", key=f"book_{index}"):
            if row['Title'] not in st.session_state.selected_books:
                st.session_state.selected_books.append(row['Title'])
        else:
            if row['Title'] in st.session_state.selected_books:
                st.session_state.selected_books.remove(row['Title'])

    st.subheader("선택한 책 목록")
    st.write(st.session_state.selected_books)

    # 책 추가 로직: 더보기 버튼
    if 'book_limit' not in st.session_state:
        st.session_state.book_limit = 10  # 초기에 10권만 표시

    # 현재 보여줄 데이터의 최대 수 계산
    max_display = min(st.session_state.book_limit, len(df))
    st.dataframe(df[:max_display])  # 현재 책 수에 따라 데이터프레임 표시

    if st.session_state.book_limit < len(df):
        if st.button('더보기', use_container_width=True):
            st.session_state.book_limit += 5  # 5권씩 더 보기

    st.caption("어떤 작업을 원하시나요?")

    # 추천받기 버튼 클릭 시 추천 페이지로 이동
    if st.button('추천받기', use_container_width=True):
        st.session_state.page = 'recommend_book'
        st.experimental_rerun()  # 페이지 이동

    cursor.close()
    connection.close()
