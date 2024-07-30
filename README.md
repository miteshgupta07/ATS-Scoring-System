<div align='center'>
  <h1>📑ATS Scoring System📑</h1>
  </div>

## 🌟 Project Overview
The ATS Scoring System is designed to parse resumes, extract entities and keywords, and score resumes based on the found keywords. The system utilizes a spaCy model trained on a [Kaggle dataset](https://www.kaggle.com/datasets/dataturks/resume-entities-for-ner) to identify and score important keywords in resumes. Additionally, it provides suggestions for improvement and displays extracted entities. The entire application is built using Streamlit, allowing users to interact with the system through a web interface.

## ✨ Features
- 📄 **Resume Parsing**: Extract text from various formats (PDF, DOCX, TXT).
- 🔍 **Entity Extraction**: Identify and extract entities from resumes using a spaCy model.
- 💯 **Keyword Scoring**: Evaluate the resume based on the presence of relevant keywords and provide a score.
- 💡 **Suggestions**: Offer suggestions to improve the resume based on the extracted entities and keywords.
- 📊 **Visualization**: Display the extracted entities and keywords in a user-friendly format.

## 🛠️ Technologies Used
- 🧠 **spaCy**: For natural language processing and entity recognition.
- 🐼 **pandas**: For handling and processing data.
- 📚 **pdfplumber**: To extract text from PDF files.
- 📝 **docx**: To extract text from DOCX files.
- 🌐 **Streamlit**: To create a web-based interface for interacting with the ATS scoring system.

## 🚀 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/miteshgupta07/ATS-Scoring-System.git
 
2. Navigate to the project directory:

    ```bash
   cd ats-scoring-system

3. Install the required packages:
   ```bash
   pip install -r requirements.txt

## 🖥️Usage
1. Run the Streamlit app:

  ```bash
  streamlit run app.py
```

2. Upload your resume in PDF, DOCX, or TXT format.

3. Enter the job description for comparison.

4. View the ATS score, Suggestions, and extracted entities.

## 📜License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/miteshgupta07/ATS-Scoring-System/blob/main/LICENSE) file for details.
