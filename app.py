import streamlit as st
import pdfplumber
from docx import Document
import spacy
import re
import pandas as pd
import time

st.write("# **Applicant Tracking System (ATS)📑**")

uploaded_resume=st.file_uploader("Upload CV/Resume",['pdf','docx','txt'])
job_description=st.text_area('Enter Job Description')

def extract_text_from_pdf(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:

        for page in pdf.pages:
            text += page.extract_text()
    return text

def extract_text_from_txt(text_file):
    with open(text_file,'r') as txt_file:
        text=txt_file.read()
    return text

def extract_text_from_docx(word_file):
    doc = Document(word_file)
    text = ""
    for para in doc.paragraphs:
        text += para.text
    return text

def preprocess_text(text):
    replacements = {
        'â€“': '–',    # en dash
        'â€”': '—',    # em dash
        'â€˜': '‘',    # left single quotation mark
        'â€™': '’',    # right single quotation mark
        'â€œ': '“',    # left double quotation mark
        'â€�': '”',    # right double quotation mark
        'â€¢': '•',    # bullet point
        'â€¦': '…',    # ellipsis
        'Ã©': 'é',     # é
        'Ã¨': 'è',     # è
        'Ã¢': 'â',     # â
        'Ã´': 'ô',     # ô
        'Ã¼': 'ü',     # ü
        'Ã±': 'ñ',     # ñ
        'Ã‹': 'Ë',     # Ë
        'Ã¡': 'á',     # á
        'Ãº': 'ú',     # ú
        'Ã®': 'î',     # î
        'Ã€': 'À',     # À
        'Ã¬': 'ì',     # ì
        'Ã™': 'Ù',     # Ù
        'Ã': 'Í',     # Í
        'Ã–': 'Ö',     # Ö
        'Ã': 'Á',     # Á
        'ÃŒ': 'Ì',     # Ì
        'Ã‰': 'É',     # É
        'Ã': 'Ï',     # Ï
        'Ã«': 'ë',     # ë
        'Ã³': 'ó',     # ó
        'Ãž': 'Þ',     # Þ
        'Ãš': 'Ú',     # Ú
        'Ã¦': 'æ',     # æ
        'Ã˜': 'Ø',     # Ø
        'ÃŸ': 'ß',     # ß
        'Ã°': 'ð',     # ð
        'Ã­': 'í',     # í
        'Ãµ': 'õ',     # õ
        'Ã¥': 'å',     # å
        'Ã¯': 'ï',     # ï
        'Ã£': 'ã',     # ã
        'Ã¤': 'ä',     # ä
        'Ã¶': 'ö',     # ö
        'Ã¼': 'ü',     # ü
        'â‚¬': '€',    # Euro sign
        'â„¢': '™',    # Trademark sign
        'âˆ‚': '∂',    # Partial differential
        'âˆ€': '∀',    # For all
        'âˆˆ': '∈',    # Element of
        'âˆƒ': '∃',    # There exists
        'âˆ…': '∅',    # Empty set
        'âˆ†': '∆',    # Increment
        'âˆ‡': '∇',    # Nabla
        'âˆ‘': '∑',    # N-ary summation
        'âˆ—': '∗',    # Asterisk operator
        'âˆ˜': '∘',    # Ring operator
        'âˆ™': '∙',    # Bullet operator
        'âˆš': '√',    # Square root
        'âˆ›': '∧',    # Logical and
        'âˆ¥': '∥',    # Parallel to
        'âˆ¼': '∼',    # Tilde operator
        'âˆ¾': '≀',    # Wreath product
        'âˆ¿': '≁',    # Not tilde
        'âˆ‹': '⊂',    # Subset of
        'âˆ›': '⊃',    # Superset of
        'â‰': '≠',     # Not equal to
        'â‰¤': '≤',    # Less-than or equal to
        'â‰¥': '≥',    # Greater-than or equal to
        'â‰¤': '≤',    # Less-than or equal to
        'â‰≥': '≥',    # Greater-than or equal to
        'â‰²': '²',    # Superscript two
        'â‰³': '³',    # Superscript three
        'â‰®': '≡',    # Identical to
        'â‰³': '≥',    # Greater-than or equal to
        'â‰¯': '≣',    # Equivalent to
        'â‰¤': '≤',    # Less-than or equal to
        'â‰³': '≥',    # Greater-than or equal to
        'â‰®': '≡',    # Identical to
    }
    
    # Replace the characters in the text
    for wrong_char, correct_char in replacements.items():
        text = text.replace(wrong_char, correct_char)
    
    # Remove newline characters and any extraneous whitespace
    text = re.sub(r'\n+', ' ', text)  # Replace multiple newlines with a single space
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
    processed_text = text.strip()  # Remove leading and trailing whitespace
    
    return processed_text

def extract_entities(text):
    nlp=spacy.load('./ner_model')
    doc=nlp(text)
    data = []
    for ent in doc.ents:
        data.append([ent.label_, ent.text])

    return data

def find_not_found_keywords(resume_keywords,job_keywords):
    nf_keywords=[]

    for keywords in resume_keywords:
        if keywords[0] not in job_keywords:
            nf_keywords.append(keywords[0])
    return nf_keywords

def show_ATS_score(text,job_description):
    resume_keywords=extract_entities(text)
    job_keywords=extract_entities(job_description)
    resumek_count=len(resume_keywords)
    jobk_count=len(job_keywords)
    if jobk_count!=0:
        score=(resumek_count/jobk_count)*100
        score=round(score,2)
    else:
        score=-1
    not_found_keywords=find_not_found_keywords(resume_keywords,job_keywords)
    return score,not_found_keywords

def show_entities(text):
    data=extract_entities(text)
    df = pd.DataFrame(data, columns=["Label", "Entity"])
    st.table(df)

def show_suggestion(keywords):
    improvement_suggestions = {
        "NAME": "• **Name:** Including your full name helps recruiters easily identify you.",
        "EMAIL_ADDRESS": "• **Email Address:** Providing an email address makes it easier for recruiters to contact you.",
        "LOCATION": "• **Location:** Including your location helps recruiters find candidates in specific geographic areas.",
        "DEGREE": "• **Degree:** Listing your degree demonstrates your educational qualifications.",
        "GRADUATION_YEAR": "• **Graduation Year:** Including your graduation year helps recruiters understand your experience level.",
        "COLLEGE_NAME": "• **College/University Name:** Mentioning your college or university name adds credibility and context to your educational background.",
        "SKILLS": "• **Skills:** Highlighting your skills shows your expertise and can make your resume stand out.",
        "WORK_EXPERIENCE": "• **Work Experience:** Detailing your previous job roles and responsibilities provides insight into your professional background.",
        "CERTIFICATIONS": "• **Certifications:** Adding relevant certifications can showcase your additional qualifications and specialized knowledge.",
        "PROJECTS": "• **Projects:** Describing significant projects you have worked on can demonstrate your practical experience and problem-solving abilities.",
        "LANGUAGES": "• **Languages:** Including languages you are proficient in can be advantageous, especially for roles requiring multilingual skills.",
        "LINKEDIN_PROFILE": "• **LinkedIn Profile:** Providing a link to your LinkedIn profile can give recruiters a more comprehensive view of your professional network and endorsements.",
        "PROFESSIONAL_SUMMARY": "• **Professional Summary:** Writing a concise professional summary at the top of your resume can quickly convey your key strengths and career objectives.",
        "DESIGNATION": "• **Designation:** Specifying your current or desired job title helps recruiters understand your career level and aspirations."
        }
    
    st.write("#### You can add the following details to improve your score:")
    for i in keywords:
        st.write(improvement_suggestions[i])

def main(uploaded_resume,job_description):
    if uploaded_resume is not None:
        doc_type=uploaded_resume.type
        if doc_type=='invalid':
            st.error("CV/Resume should be in PDF/DOCX/TXT format")
        else:
            if doc_type=='application/pdf':
                text=extract_text_from_pdf(uploaded_resume)
            elif doc_type=='text/plain':
                text=extract_text_from_docx(uploaded_resume)
            else:
                text=extract_text_from_docx(uploaded_resume)

        if text and not job_description:
            if st.checkbox('Show Entities'):
                st.write("### Resume Keywords")
                show_entities(text)

        if text and job_description:
            text=preprocess_text(text)
            job_description=preprocess_text(job_description)

            progress_bar=st.progress(0)
            for i in range(100):
                time.sleep(0.01)  
                progress_bar.progress(i + 1) 
            time.sleep(1)

            ats_score,not_found_keywords=show_ATS_score(text,job_description)

            if ats_score==-1:
                st.warning("No Keywords Found in Job Description")
            else:
                if 0<ats_score<=50:
                    st.error(f"Your ATS Score is{ats_score} out of 100")
                    st.write("Your score is Low")

                elif 50<ats_score<=75:
                    st.warning(f"Your ATS Score is {ats_score} out of 100")
                    st.write("Your score is Average")

                else:
                    st.success(f"Your ATS Score is {ats_score} out of 100")
                    st.write("Your score is Good")

            
            if len(not_found_keywords)!=0:
                st.write('## *Suggestion Based on your Resume*')
                show_suggestion(not_found_keywords)

            if st.checkbox('Show All Entities'):
                col1,col2=st.columns(2)
                with col1:
                    st.write("### Resume Keywords")
                    show_entities(text)
                with col2:
                    st.write("### Job Description Keywords")
                    show_entities(job_description)

main(uploaded_resume,job_description) 