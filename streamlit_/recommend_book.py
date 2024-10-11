import streamlit as st
import pymysql
import pandas as pd

def app():
    st.header("📖 추천 도서", divider="rainbow")
    st.caption("기존에 등록한 책을 기반으로 추천을 받으세요.")
    
    selected_books = st.session_state.get('selected_books', [])

    if selected_books:
        st.write("선택한 책 목록:")
        for book in selected_books:
            st.write(f"- {book}")
    else:
        st.write("선택한 책이 없습니다.")
  
    # 데이터베이스 연결
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

    # 샘플 추천 도서 쿼리 (추천 로직 나중에 추가 예정)
    query = "SELECT title, author FROM sample_user LIMIT 10"
    cursor.execute(query)
    rows = cursor.fetchall()

    df = pd.DataFrame(rows, columns=['Title', 'Author'])

    # 추천 도서 표시
    st.dataframe(df)

    # 샘플 데이터로 책 두께 비교 그래프
    st.subheader("책 두께 비교")
    thickness_data = [10, 20, 30, 40, 50]  # 실제 두께 데이터로 교체 필요
    st.bar_chart(thickness_data)

    if st.button('메인 페이지로 돌아가기', type="primary"):
        st.session_state.page = 'my_book'
        st.experimental_rerun()  # 메인 페이지로 이동

    cursor.close()
    connection.close()
