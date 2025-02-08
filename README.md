# Resume Grader

[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Latest-red.svg)](https://streamlit.io/)
[![Google Gemini](https://img.shields.io/badge/Gemini_API-Latest-green.svg)](https://ai.google.dev/)

An AI-powered resume analysis tool that helps candidates optimize their resumes for Applicant Tracking Systems (ATS) using Google's Gemini API.

## Features

- Resume-Job Description matching score
- Detailed resume analysis
- Missing keywords identification
- Professional evaluation
- PDF resume processing
- Interactive web interface

## Tech Stack

- **Frontend**: Streamlit
- **AI Model**: Google Gemini Pro
- **PDF Processing**: PyPDF2
- **Image Processing**: PIL
- **Environment Management**: python-dotenv

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/resume-grader.git
cd resume-grader
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
# Create .env file
touch .env

# Add your Google API key
echo "GOOGLE_API_KEY=your_api_key_here" >> .env
```

## Project Structure
```
resume-grader/
├── app.py              # Main application file
├── assets/
│   └── img.png        # Application images
├── requirements.txt
└── README.md
```

## Usage

1. Run the Streamlit application:
```bash
streamlit run app.py
```

2. Access the web interface:
   - Paste the job description
   - Upload your resume (PDF format)
   - Choose analysis type:
     - Generate Resume Score
     - Analyze Resume

## Features in Detail

### Resume Score Generation
- Calculates match percentage with job description
- Identifies missing keywords
- Provides concise feedback (under 50 words)

### Detailed Analysis
- Professional evaluation from hiring manager perspective
- Bullet-point suggestions for improvement
- Skills gap analysis
- Comprehensive feedback (100-250 words)


## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Future Improvements

- [ ] Add support for more resume formats (DOCX, TXT)
- [ ] Implement resume improvement suggestions
- [ ] Add visual analytics dashboard
- [ ] Include industry-specific analysis
- [ ] Add batch processing capability

## Acknowledgments

- Google Gemini API
- Streamlit team
- PyPDF2 developers
- All contributors
