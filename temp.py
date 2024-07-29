import streamlit as st
import time


st.write("# **Applicant Tracking System (ATS)📑**")
uploaded_resume=st.file_uploader("Upload CV/Resume",['pdf','docx','txt'])
job_description=st.text_area('Enter Job Description')

# d1=[]
# d1.append(['NAME','MITESH GUPTA'])
# d1.append(['EMAIL_ADDRESS','miteshgupta2711@gmail.com'])
# d1.append(['DEGREE','B.Tech'])
# d1.append(['SKILLS','Data Science, AI, Machine Learning, Deep Learning, Computer Vision, NLP, Python'])
# d1.append(['COLLEGE_NAME','Parul University'])
# d1.append(['GRADUATION_YEAR','2025'])

# d2=[]
# d2.append(['DESIGNATION','Data Science Intern'])
# d2.append(['DEGREE','B.E./B.Tech, M.Tech,'])
# d2.append(['GRADUATION_YEAR','2025'])
# d2.append(['SKILLS','Data Science, Machine Learning, Deep Learning, Statistical Modelling, Python/R'])

# d1=[]
# d1.append(['NAME','Abhishek Pawar'])
# d1.append(['SKILLS','Flutter, Dart, UI/UX, Firebase, State Management'])
# d1.append(['COLLEGE_NAME','Parul University'])
# d1.append(['GRADUATION_YEAR','2025'])

# d2=[]
# d2.append(['DESIGNATION','Flutter Developer Intern'])
# d2.append(['DEGREE','B.E./B.Tech'])
# d2.append(['GRADUATION_YEAR','2025'])
# d2.append(['SKILLS','Flutter, Dart, Firebase, UI Designing'])

d1=[]
d1.append(['NAME','Saurabh Sandhikar'])
d1.append(['EMAIL_ADDRESS','abc@gmail.com'])
d1.append(['DEGREE','B.Tech'])

d2=[]
d2.append(['DESIGNATION','Web Developer Intern'])
d2.append(['DEGREE','B.E./B.Tech, M.Tech,'])
d2.append(['GRADUATION_YEAR','2025'])
d2.append(['SKILLS', 'HTML/CSS, Javascript, React, MongoDB'])

if uploaded_resume and job_description:
    # time.sleep(2)
    progress_bar = st.progress(0)

    for i in range(100):
        time.sleep(0.01)  
        progress_bar.progress(i + 1) 
    time.sleep(1)
    st.error("Your ATS Score is 37 out of 100")
    st.write("Your score is Low")
    time.sleep(1)
    st.write('### Suggestion Based on your Resume')
    st.write('''
#### You can add the following details to improve your score:
- **Email Address:** Including an email address ensures recruiters can easily reach you.
- **Graduation Year:** Including helps recruiters understand your experience level.
- **Skills:** Highlighting your skills shows your expertise an can make your resume stand out.
''')

    # st.write('#### • You can add some more keywords to improve ATS score for example Address, Graduation Year, ')
    if st.checkbox('# **Show Found Keywords**'):
        c1,c2=st.columns(2)
        with c1:
            st.write("#### Resume Keywords")
            st.table(d1)
        with c2:
            st.write("#### Job Description Keywords")
            st.table(d2)