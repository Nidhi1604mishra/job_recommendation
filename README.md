# job_recommendation
A BERT-based Smart Job Recommendation System that matches user resumes to real-time job listings using NLP and cosine similarity.


Upload your resume in PDF or DOCX format, and get the best job matches based on your skills and experience.

## 🚀 Features

- 📄 Upload resume file (PDF/DOCX)
- 🤖 NLP-based resume parsing using SpaCy
- 🧠 Job matching using Sentence-BERT (all-MiniLM-L6-v2)
- 💼 Job data fetched from RapidAPI
- 🗃️ MongoDB for job storage
- 📊 Resume upload history saved and displayed
- 🌐 Gradio-based interactive UI

## 🛠️ Tech Stack

- Python 🐍
- Gradio for frontend
- MongoDB for database
- RapidAPI for job data
- SentenceTransformers for BERT
- SpaCy for text cleaning
