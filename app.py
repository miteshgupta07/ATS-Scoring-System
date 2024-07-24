import streamlit as st

st.title("Resume Parsing App")

resume=st.file_uploader("Upload CV/Resume",['pdf','docx','txt'])

print(resume)