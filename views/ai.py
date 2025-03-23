import streamlit as st
import PyPDF2
import io
import re
import google.generativeai as genai

# Initialize Streamlit page
st.title("AI Resume Optimizer")
st.write("Upload your resume and paste a job description to get AI-powered suggestions.")

# Sidebar for API Key
api_key = st.sidebar.text_input("Enter Google Gemini API Key", type="password")
st.sidebar.caption("Get an API key from [Google AI Studio](https://aistudio.google.com/)")

# Configure Gemini AI
if api_key:
    genai.configure(api_key=api_key)
else:
    st.warning("Enter your Google Gemini API Key to enable AI features.")

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    """Extract text from a PDF file."""
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = "\n".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])
        return text
    except Exception as e:
        st.error(f"Error extracting text from PDF: {e}")
        return None

# Function to extract sections from resume text
def extract_resume_sections(text):
    """Extract sections like Experience, Skills, etc., from resume."""
    sections = {
        "experience": r"(?i)(?:EXPERIENCE|WORK EXPERIENCE|EMPLOYMENT|PROFESSIONAL EXPERIENCE|RELEVANT EXPERIENCE)",
        "education": r"(?i)(?:EDUCATION|ACADEMIC QUALIFICATIONS|EDUCATIONAL BACKGROUND)",
        "skills": r"(?i)(?:SKILLS|TECHNICAL SKILLS|COMPETENCIES|AREAS OF EXPERTISE)",
        "projects": r"(?i)(?:PROJECTS|PROJECT EXPERIENCE|PERSONAL PROJECTS)",
        "certifications": r"(?i)(?:CERTIFICATIONS|CERTIFICATES|LICENSES)",
        "summary": r"(?i)(?:SUMMARY|OBJECTIVE|PROFILE)",
    }
    extracted_sections = {"unsorted": []}

    lines = text.split('\n')
    current_section = "unsorted"

    for line in lines:
        line = line.strip()
        if not line:
            continue
        for section, pattern in sections.items():
            if re.search(pattern, line.upper()):
                current_section = section
                extracted_sections[current_section] = []
                break
        extracted_sections.setdefault(current_section, []).append(line)

    return {k: '\n'.join(v) for k, v in extracted_sections.items()}

# Function to extract bullet points
def extract_bullet_points(text):
    """Extract bullet points from resume."""
    bullet_patterns = [
        r'•\s*(.+?)(?=\n|$)',  # Bullet point with Unicode character
        r'-\s*(.+?)(?=\n|$)',  # Bullet point with hyphen
        r'\d+\.\s*(.+?)(?=\n|$)',  # Numbered list
        r'\u2022\s*(.+?)(?=\n|$)', # Bullet point with another Unicode character
        r'\*\s*(.+?)(?=\n|$)', # Bullet point with asterisk
        r'◦\s*(.+?)(?=\n|$)' # Bullet point with circle
    ]
    bullet_points = []

    for pattern in bullet_patterns:
        bullet_points.extend(re.findall(pattern, text))

    return [bp.strip() for bp in bullet_points if len(bp.strip()) > 5]

# Function to analyze resume against job description using Gemini API
def analyze_resume_with_job(resume_points, job_description):
    """Compare resume with job description using Gemini API."""
    if not api_key:
        return "API key is missing. Enter it in the sidebar."

    prompt = f"""
    You are a resume enhancer AI, you aim to help and enhance job seekers' resumes.
    Analyze the following resume points of seekers' against the job description  and rewrite the resume points to be more impactful and tailored to the job description but dont only make use of the skills or methods used in the pdf dont try to add points just to please job description.

    **Job Description:**
    {job_description}

    **Resume Points:**
    {resume_points}

    refine resumes based on job descriptions, suggesting improvements and rewriting bullet points for better impact.

    Do not add extra points or words that are not there in the resume points, and do not hallucinate.
    
    Return the rewritten resume points in a clear, well-formatted list.
    """

    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content(prompt)
    return response.text if response and response.text else "Failed to analyze resume."

# Function to extract key skills from job description
def keywords_extraction(job_description):
    """Extract key skills from job description using Gemini API."""
    if not api_key:
        return "API key is missing. Enter it in the sidebar."

    prompt = f"Extract the top 10 key skills and requirements from this job description:\n\n{job_description}"
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content(prompt)
    return response.text if response and response.text else "Failed to extract key skills."

# Create Streamlit tabs
tab1, tab2, tab3 = st.tabs(["Upload Resume", "Job Description", "AI Recommendations"])

# Tab 1: Resume Upload
with tab1:
    st.header("Upload Your Resume (PDF)")
    uploaded_file = st.file_uploader("Choose your resume PDF", type="pdf")

    if uploaded_file:
        resume_text = extract_text_from_pdf(uploaded_file)
        if resume_text:
            st.success("Resume uploaded and processed successfully!")
            with st.expander("Extracted Resume Text"):
                st.text_area("Resume Text", resume_text, height=200)

            sections = extract_resume_sections(resume_text)
            experience_points = extract_bullet_points(sections.get("experience", ""))
            project_points = extract_bullet_points(sections.get("projects", ""))

            with st.expander("Extracted Work Experience"):
                for i, point in enumerate(experience_points, 1):
                    st.write(f"{i}. {point}")

            with st.expander("Extracted Projects"):
                for i, point in enumerate(project_points, 1):
                    st.write(f"{i}. {point}")

            st.session_state['resume_text'] = resume_text
            st.session_state['experience_points'] = experience_points
            st.session_state['project_points'] = project_points

# Tab 2: Job Description Input
with tab2:
    st.header("Enter Job Description")
    job_description = st.text_area("Paste the job description here", height=250)

    if job_description:
        st.session_state['job_description'] = job_description
        st.success("Job description saved!")

        if api_key and st.button("Extract Key Skills"):
            skills = keywords_extraction(job_description)
            st.subheader("Key Skills from Job Description")
            st.write(skills)

# Tab 3: AI Resume Recommendations
with tab3:
    st.header("AI Resume Recommendations")

    if 'resume_text' not in st.session_state:
        st.warning("Please upload your resume in the first tab.")
    elif 'job_description' not in st.session_state:
        st.warning("Please enter a job description in the second tab.")
    elif not api_key:
        st.warning("An API key is required. Enter your Google Gemini API key in the sidebar.")
    else:
        resume_points_text = "\n".join(st.session_state.get('experience_points', []) + st.session_state.get('project_points', []))
        
        if st.button("Generate Recommendations"):
            analysis = analyze_resume_with_job(resume_points_text, st.session_state['job_description'])
            st.subheader("AI Recommendations")
            st.markdown(analysis)
