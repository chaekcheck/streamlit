import streamlit as st

def app():
    st.header("📕 책 등록하기", divider="rainbow")
    st.caption("책의 제목과 저자가 맞는지 확인해주세요.")

    # OCR로 인식된 책 정보가 있는지 확인하고 없으면 경고 메시지 표시
    if 'detected_books' not in st.session_state:
        st.warning("책 정보가 없습니다. 먼저 책 사진을 업로드하세요.")
        return

    detected_books = st.session_state.detected_books  # 이전 페이지에서 가져온 책 정보

    # 유저가 수정할 수 있는 책 정보 표시
    edited_books = []
    st.subheader("인식된 책 정보")
    for idx, book in enumerate(detected_books):
        # with st.expander(f"책 {idx + 1}: {book['title']}"):
            # new_title = st.text_input(f"책 제목 {idx + 1}", value=book["title"])
            # new_author = st.text_input(f"저자 {idx + 1}", value=book["author"])
            # edited_books.append({"title": new_title, "author": new_author})
        with st.expander(f"책 {idx + 1}: {book}"):
            st.text_input(f"책 제목 {idx + 1}", value=book)

    # 책 등록 버튼 - 수정된 데이터를 데이터베이스에 저장
    if st.button('책 등록하기', type="primary", use_container_width=True):
        # 데이터베이스에 저장하는 로직 추가 해야됨!!!!!!!!!!!!!!!!!!!
        st.success("책이 성공적으로 등록되었습니다!")
        del st.session_state['detected_books']
        # 수정된 데이터를 세션에 저장
        st.session_state.edited_books = edited_books

    # '책 등록 완료' 버튼을 누르면 메인 페이지로 이동
    if st.button('나의 서재 확인하기', use_container_width=True):
        st.session_state.page = 'my_book'
