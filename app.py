import streamlit as st

import chatter

chat = chatter.Chatter()

st.title("✉️ emailGPT")
st.subheader("a quick and easy interface to generate emails with ChatGPT")

theme = st.text_input(label="テーマ", value="")
subject = st.text_input(label="件名", value="")
language = st.selectbox(label="言語", options=('日本語', '英語'))
sender_attr= st.selectbox(label="送りて属性", options=('30代女性', '40代女性', '50代女性'))
receiver_attr= st.selectbox(label="受け手属性", options=('30代女性', '40代女性', '50代女性'))
max_length = st.selectbox(label="制限文字数",options=('800', '1600', '2400'))
tone = st.selectbox("文体のテイスト", ("excited", "happy", "neutral", "sad", "angry"), index=2)
no_emails = st.selectbox(label="制限文字数",options=('1', '2', '3'))

generate_email = st.button("Generate Email")

if generate_email:
    job = {
        "subject": subject,
        "theme": theme,
        "language": language,
        "sender_attr": sender_attr,
        "receiver_attr": receiver_attr,
        "max_length": max_length,
        "tone": tone,
        "no_emails": no_emails
    }
    message = chat.email_from_job(job=job)
    st.write(message)


with st.sidebar:
    st.markdown(
        "[About ChatGPT](https://openai.com/blog/chatgpt/)", unsafe_allow_html=True
    )
    st.markdown(
        "[This app on GitHub](https://github.com/lucasmccabe/emailGPT)",
        unsafe_allow_html=True,
    )
    st.markdown(
        "[Lucas H. McCabe](https://lucasmccabe.github.io/)", unsafe_allow_html=True
    )
