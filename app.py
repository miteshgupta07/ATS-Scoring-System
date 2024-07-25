import streamlit as st
import pdfplumber

st.title("Resume Parsing App")

uploaded_resume=st.file_uploader("Upload CV/Resume",['pdf','docx','txt'])

def check_document_type(doc):
    pass

def extract_text_from_pdf(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        print("Hello")
        for page in pdf.pages:
            text += page.extract_text()
        formated_text=text.replace('\n',' ')
    return formated_text

def extract_text_from_txt(text_file):
    pass

def extract_text_from_docx(word_file):
    pass

def preprocess_text():
    pass

def extract_entities():
    pass

if uploaded_resume is not None:
    doc_type=check_document_type(uploaded_resume)
    if doc_type=='invalid':
        st.error("CV/Resume should be in PDF/DOCX/TXT format")
    else:
        if doc_type=='application/pdf':
            text=extract_text_from_pdf(uploaded_resume)
        elif doc_type=='text/plain':
            text=extract_text_from_docx(uploaded_resume)
        else:
            text=extract_text_from_docx(uploaded_resume)
    if text:
        preprocessed_text=preprocess_text(text)
        entities=extract_entities(preprocessed_text)
        