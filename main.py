import streamlit as st
import langchain_helper as lch
import textwrap

st.title("Youtube Assistant")

with st.sidebar:
    with st.form(key='my_form'):
        youtube_url = st.sidebar.text_area(
            label="Youtube URL",
        )
        query = st.sidebar.text_area(
            label = "Ask me about the video",
            key="query"
        )
        submit_button = st.form_submit_button(label="Submit")

if youtube_url:
    db = lch.create_db_from_youtube_video_url(youtube_url)
    response, docs = lch.get_response_from_query
    st.subheader("Answer:")
    st.text(textwrap.fill(response,width=85))