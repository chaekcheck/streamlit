import streamlit as st

def app():
    st.header("📷 책 사진 업로드", divider="rainbow")
    st.caption("보유한 책을 온라인 서재에 등록하세요.")

    uploaded_pic = st.file_uploader("책 사진을 업로드하세요", type=["jpg", "png", "jpeg"])

    if uploaded_pic is not None:
        st.image(uploaded_pic, caption="업로드한 책 사진", use_column_width=True)
    st.divider()

    with st.expander("이미지 업로드 가이드"):
        st.text("흔들리지 않은 선명한 이미지를 \n한 장 업로드 해주세요. \n첨부 이미지 내 책은 5권이 넘어가지 \n않게 해주세요.")

    # OCR 결과 여기에 넣어야 됨! (임시 데이터)
    detected_books = [
        {"title": "The Little Prince", "author": "Antoine de Saint-Exupéry"},
        {"title": "1984", "author": "George Orwell"}
    ]

    # OCR 결과를 session_state에 저장하여 다음 페이지에서 사용할 수 있도록 함
    if 'detected_books' not in st.session_state:
        st.session_state.detected_books = detected_books

    if st.button('책 등록하기', type="primary", use_container_width=True):
        st.session_state.page = 'enroll_book'
