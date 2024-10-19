from ocrMain import get_titles

import streamlit as st
import asyncio
from PIL import Image


async def long_running_task():
    for i in range(100):
        st.write(f"Working on step {i+1}...")
        await asyncio.sleep(1)  # 비동기적으로 대기


def app():
    st.header("📷 책 사진 업로드", divider="rainbow")
    st.caption("보유한 책을 온라인 서재에 등록하세요.")

    # Image input box
    uploaded_pic = st.file_uploader("책 사진을 업로드하세요", type=["jpg", "png", "jpeg"])

    # 업로드한 책 목록
    # if uploaded_pic is not None:
    if uploaded_pic:
        # st.write(type(uploaded_pic))
        st.image(uploaded_pic, caption="업로드한 책 사진", use_column_width=True)
    st.divider()

    # 이미지 업로드 가이드
    with st.expander("이미지 업로드 가이드"):
        st.text("책장 한 칸의 이미지를 \n흔들리지 않게 찍어주세요. \n글자가 크고 선명할수록 좋아요.\n*10권 이내 권장")

    # OCR 결과 여기에 넣어야 됨! (임시 데이터)


    # OCR 결과를 session_state에 저장하여 다음 페이지에서 사용할 수 있도록 함
    # if 'detected_books' not in st.session_state:
    #     st.session_state.detected_books = detected_books

    if st.button('책 등록하기', type="primary", use_container_width=True):
        if uploaded_pic:
            # detected_books = [
            #     {"title": "The Little Prince", "author": "Antoine de Saint-Exupéry"},
            #     {"title": "1984", "author": "George Orwell"}
            # ]
            detected_books = get_titles(Image.open(uploaded_pic))
            st.session_state.detected_books = detected_books
            # st.session_state.page = 'enroll_book'
            # st.write(detected_books)
        else:
            st.warning('이미지를 업로드하세요!')

    if st.button('Run task'):
        asyncio.run(long_running_task())
        # asyncio.create_task(long_running_task())

