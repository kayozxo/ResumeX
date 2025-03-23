import streamlit as st
import PyPDF2
import io
import re
import google.generativeai as genai
from collections import Counter

# Initialize Streamlit page
st.title("AI Resume Optimizer")
st.write("Upload your resume and paste a job description to get AI-powered suggestions and ATS score.")

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
You are an expert resume optimization AI focused on helping job seekers get past ATS systems while impressing human recruiters.

TASK: Analyze the resume points against the job description and rewrite them to be more impactful, achievement-oriented, and tailored to this specific role.

JOB DESCRIPTION:
{job_description}

CURRENT RESUME POINTS:
{resume_points}

INSTRUCTIONS:
1. Maintain absolute factual accuracy - never add skills, experiences, or qualifications that aren't in the original points
2. Transform each point to highlight RELEVANT accomplishments using the STAR or PAR format (Situation/Task, Action, Result)
3. Incorporate appropriate keywords and terminology from the job description naturally
4. Quantify achievements where possible (%, $, time saved, efficiency gained)
5. Use strong action verbs at the beginning of each point
6. Remove generic, vague, or irrelevant information
7. Ensure each point clearly demonstrates value and impact
8. Optimize for both ATS readability and human engagement

OUTPUT FORMAT:
- Provide rewritten bullet points in a clear, numbered list
- Use concise, professional language
- Maintain appropriate tense (past tense for past roles)
- Keep each bullet point to 1-2 lines for readability

Remember: Your goal is to truthfully showcase the candidate's relevant experience and skills in the most compelling way possible for THIS SPECIFIC JOB.
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

# New function to calculate ATS score
def calculate_ats_score(resume_text, job_description):
    """Calculate ATS score by comparing resume with job description."""
    if not api_key:
        return {"score": 0, "feedback": "API key is missing. Enter it in the sidebar."}

    prompt = f"""
    You are an ATS (Applicant Tracking System) expert. Analyze the resume text against the job description and provide:
    
    1. A numeric ATS compatibility score from 0-100
    2. Detailed feedback on why the resume would or wouldn't pass an ATS
    3. Identify any missing keywords from the job description
    4. Check for proper formatting issues that might affect ATS parsing
    5. Suggestions for improvement
    
    **Job Description:**
    {job_description}
    
    **Resume Text:**
    {resume_text}
    
    Return the response in a structured format with clear sections for Score, Feedback, Missing Keywords, Formatting Issues, and Suggestions.
    """

    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content(prompt)
    return response.text if response and response.text else "Failed to analyze ATS score."

# Function to create a simplified ATS score visualization
def create_ats_visualization(score):
    """Create a visual representation of the ATS score."""
    try:
        # Extract the score if it's in the text
        score_match = re.search(r'(?i)score:?\s*(\d+)', score)
        if score_match:
            numeric_score = int(score_match.group(1))
        else:
            # If no score found, estimate from text sentiment
            if "excellent" in score.lower() or "strong" in score.lower():
                numeric_score = 85
            elif "good" in score.lower():
                numeric_score = 70
            elif "average" in score.lower():
                numeric_score = 50
            elif "poor" in score.lower():
                numeric_score = 30
            else:
                numeric_score = 50  # Default score
            
        # Create visualization
        color = "green" if numeric_score >= 70 else "orange" if numeric_score >= 50 else "red"
        return numeric_score, color
    except:
        return 50, "gray"  # Default fallback

# Create Streamlit tabs
tab1, tab2, tab3, tab4 = st.tabs(["Upload Resume", "Job Description", "ATS Score", "AI Recommendations"])

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

# Tab 3: ATS Score Checker (New Tab)
with tab3:
    st.header("ATS Score Checker")
    
    if 'resume_text' not in st.session_state:
        st.warning("Please upload your resume in the first tab.")
    elif 'job_description' not in st.session_state:
        st.warning("Please enter a job description in the second tab.")
    elif not api_key:
        st.warning("An API key is required. Enter your Google Gemini API key in the sidebar.")
    else:
        if st.button("Check ATS Score"):
            with st.spinner("Analyzing your resume against ATS requirements..."):
                ats_analysis = calculate_ats_score(st.session_state['resume_text'], st.session_state['job_description'])
                st.session_state['ats_analysis'] = ats_analysis
                
                # Extract numeric score and color for visualization
                numeric_score, color = create_ats_visualization(ats_analysis)
                
                # Display score with a progress bar
                st.subheader(f"ATS Compatibility Score: {numeric_score}/100")
                st.progress(numeric_score/100)
                
                # Display colored indicator
                st.markdown(f"""
                <div style="background-color: {color}; padding: 10px; border-radius: 5px; margin-bottom: 20px;">
                    <h3 style="color: white; margin: 0;">
                        {'Excellent Match' if numeric_score >= 80 else 
                         'Good Match' if numeric_score >= 70 else
                         'Average Match' if numeric_score >= 50 else
                         'Poor Match'}
                    </h3>
                </div>
                """, unsafe_allow_html=True)
                
                # Display the detailed analysis
                st.subheader("Detailed ATS Analysis")
                st.markdown(ats_analysis)
                
                # Add a keyword match visualization
                st.subheader("Key Recommendations")
                st.info("⚠️ Make sure your resume includes all the required keywords from the job description.")
                st.info("📄 Avoid complex formatting, tables, or headers/footers that can confuse ATS systems.")
                st.info("🔍 Use standard section headings (Experience, Education, Skills) for better parsing.")

# Tab 4: AI Resume Recommendations
with tab4:
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
            with st.spinner("Generating optimized resume points... This may take a moment"):
                analysis = analyze_resume_with_job(resume_points_text, st.session_state['job_description'])
            st.subheader("AI Recommendations")
            st.markdown(analysis)
            
            # If ATS analysis is available, show a summary here too
            if 'ats_analysis' in st.session_state:
                st.subheader("ATS Optimization Tips")
                st.info("Implement the recommendations above and then recheck your ATS score to see improvement.")