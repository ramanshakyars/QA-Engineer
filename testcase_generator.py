import streamlit as st
from utils.llm import run_local_model

#  python -m streamlit run testcase_generator.py

st.set_page_config(page_title="QA Engineer", layout="centered")
st.title("QA Engineer Here!")

prompt = st.text_area("Describe Your Usecase Here", height=100)

if st.button("Generate Test Cases"):
    if prompt:
        with st.spinner("Generating test cases..."):
            result = run_local_model(prompt)
        st.subheader("Generated Test Cases")
        st.code(result)
    else:
        st.error("Please enter a feature description to generate test cases.")
