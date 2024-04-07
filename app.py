# Library Imports and Requirements
import base64
import streamlit as st 
import os
import io
from PIL import Image 
import PyPDF2 as pdf
import google.generativeai as genai 
from dotenv import load_dotenv
load_dotenv()

# Gemini API config
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Get response from Gemini API
def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text

# Convert PDF to text
def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text += str(page.extract_text())
    return text
    
# Prompt Templates
input_prompt1 = """ 
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and 
ATS functionality, your task is to evaluate the resume against the provided job description. give me the percentage of 
match if the resume matches the job description. First the output should come as percentage that should be in bold 
or highligheted, then keywords missing and last final thoughts. The total response should not exceed 50 words. 
The resume and the job description are provided below 
resume:{text}
description:{job_desc}
"""

input_prompt2 = """
Consider yourself as a hiring manager in that specific field according to the job description. Now analyze the resume given 
and the job description provided and share your professional evaluationon whether the candidates profile alligns with the role.
Now, in bulletin points suggest the missing skills, potential areas of improvement of the candidates resume in relation 
to the specified job requirements and role. The total response should be in the range of 100 - 250 words.
The resume and the job description are provided below 
resume:{text}
description:{job_desc}
"""

# Frontend and Interface -> Streamlit 
st.image('assets/img.png')
st.title("RESUME GRADER")
st.text("Beat applicant tracking systems (ATS) with our AI-powered resume analyzer.\nGet matched to jobs and optimize your resume for successful recruitment.")
job_desc = st.text_area("Paste the Job Description here")
uploaded_file = st.file_uploader("Upload Your Resume",type="pdf",help="Please upload the Resume in PDF format")

col1, col2 = st.columns(2)
with col1:
    btn1 = st.button("Generate Resume Score for the job")
with col2:
    btn2 = st.button("Analyze resume")

# Send request to Gemini API
if btn1:
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        response = get_gemini_response(input_prompt1.format(text=text, job_desc=job_desc))
        st.subheader(response) 
if btn2:
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        response = get_gemini_response(input_prompt2.format(text=text, job_desc=job_desc))
        st.subheader(response) 