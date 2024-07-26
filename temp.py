import streamlit as st
import time
uploaded_resume=st.file_uploader("Upload CV/Resume",['pdf','docx','txt'])
job_description=st.text_area('Enter Job Description')

d1=[]
d1.append(['NAME','MITESH GUPTA'])
d1.append(['EMAIL_ADDRESS','miteshgupta2711@gmail.com'])
d1.append(['DEGREE','B.Tech'])
d1.append(['SKILLS','Data Science, AI, Machine Learning, Deep Learning, Computer Vision, NLP, Python'])
d1.append(['COLLEGE_NAME','Parul University'])
d1.append(['GRADUATION_YEAR','2025'])

d2=[]
d2.append(['DESIGNATION','Data Science Intern'])
d2.append(['DEGREE','B.E./B.Tech, M.Tech,'])
d2.append(['GRADUATION_YEAR','2025'])
d2.append(['SKILLS','Data Science, Machine Learning, Deep Learning, LLM, Python'])


if uploaded_resume:
    time.sleep(2)
    st.success(f"Your ATS Score is 93 out of 100")
    time.sleep(1.5)
    st.write('## *Suggestion Based on your Resume*')
    st.write('#### • You should add some more keywords like your Address, Graduation Year')
    if st.checkbox('Show Keywords'):
        c1,c2=st.columns(2)
        with c1:
            st.write("### Resume Keywords")
            st.table(d1)
        with c2:
            st.write("### Job Description Keywords")
            st.table(d2)