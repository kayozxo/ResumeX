import streamlit as st
import PyPDF2
import io
import re
from pathlib import Path
import tempfile

def extract_text_from_pdf(pdf_file):
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()
        return text
    except Exception as e:
        st.error(f"Error extracting text from PDF: {e}")
        return None

def extract_resume_sections(text):
    sections = {
        "contact_info": r"(?:CONTACT|PERSONAL|PROFILE)",
        "summary": r"(?:SUMMARY|PROFESSIONAL SUMMARY|PROFILE|ABOUT ME)",
        "experience": r"(?:EXPERIENCE|WORK EXPERIENCE|EMPLOYMENT|PROFESSIONAL EXPERIENCE)",
        "education": r"(?:EDUCATION|ACADEMIC|QUALIFICATIONS)",
        "skills": r"(?:SKILLS|TECHNICAL SKILLS|CORE COMPETENCIES|EXPERTISE)",
        "projects": r"(?:PROJECTS|PROJECT EXPERIENCE)",
        "certifications": r"(?:CERTIFICATIONS|CERTIFICATES|ACCREDITATIONS)",
        "languages": r"(?:LANGUAGES|LANGUAGE PROFICIENCY)",
        "interests": r"(?:INTERESTS|HOBBIES)"
    }

    extracted_sections = {}

    current_section = "unsorted"
    extracted_sections[current_section] = []

    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        if not line:
            continue

        is_header = False
        for section_name, pattern in sections.items():
            if re.search(pattern, line.upper()):
                current_section = section_name
                extracted_sections[current_section] = []
                is_header = True
                break

        if not is_header:
            extracted_sections[current_section].append(line)

    for section in extracted_sections:
        extracted_sections[section] = '\n'.join(extracted_sections[section])

    return extracted_sections

def extract_bullet_points(text):
    bullet_patterns = [
        r'• (.+?)(?=• |\n\n|$)',
        r'· (.+?)(?=· |\n\n|$)',
        r'- (.+?)(?=- |\n\n|$)',
        r'▪ (.+?)(?=▪ |\n\n|$)',
        r'○ (.+?)(?=○ |\n\n|$)',
        r'➢ (.+?)(?=➢ |\n\n|$)',
        r'★ (.+?)(?=★ |\n\n|$)',
        r'\* (.+?)(?=\* |\n\n|$)',
        r'\d+\.\s*(.+?)(?=\d+\.\s*|\n\n|$)',
    ]

    bullet_points = []
    for pattern in bullet_patterns:
        matches = re.findall(pattern, text, re.DOTALL)
        for match in matches:
            cleaned_match = match.strip().replace('\n', ' ')
            if cleaned_match and len(cleaned_match) > 5:
                bullet_points.append(cleaned_match)

    if not bullet_points:
        sentences = re.split(r'(?<=[.!?])\s+', text)
        for sentence in sentences:
            cleaned = sentence.strip()
            if cleaned and len(cleaned) > 10 and len(cleaned) < 500:
                bullet_points.append(cleaned)

    return bullet_points

st.title("Resume Points Extractor")
st.write("Upload your resume PDF to extract key points that can be compared with job descriptions.")

uploaded_file = st.file_uploader("Choose your resume PDF file", type="pdf")

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_path = tmp_file.name

    st.subheader("Uploaded Resume")
    with open(tmp_path, "rb") as f:
        base64_pdf = io.BytesIO(f.read()).getvalue()
        st.download_button(
            label="Download PDF",
            data=base64_pdf,
            file_name=uploaded_file.name,
            mime="application/pdf"
        )

    uploaded_file.seek(0)

    resume_text = extract_text_from_pdf(uploaded_file)

    if resume_text:
        st.subheader("Extracted Text")
        with st.expander("Show Raw Text"):
            st.text_area("Raw Text", resume_text, height=300)

        sections = extract_resume_sections(resume_text)

        experience_points = []
        if "experience" in sections:
            experience_points = extract_bullet_points(sections["experience"])

        project_points = []
        if "projects" in sections:
            project_points = extract_bullet_points(sections["projects"])

        st.subheader("Extracted Resume Points")

        if experience_points:
            st.write("**Work Experience Points:**")
            for i, point in enumerate(experience_points, 1):
                st.write(f"{i}. {point}")

            all_exp_points = "\n".join(experience_points)
            st.text_area("All Experience Points (Copy from here)", all_exp_points, height=200)

        if project_points:
            st.write("**Project Points:**")
            for i, point in enumerate(project_points, 1):
                st.write(f"{i}. {point}")

            all_proj_points = "\n".join(project_points)
            st.text_area("All Project Points (Copy from here)", all_proj_points, height=150)

        if experience_points or project_points:
            all_points = "# Experience Points\n\n"
            all_points += "\n".join(experience_points)
            all_points += "\n\n# Project Points\n\n"
            all_points += "\n".join(project_points)

            st.download_button(
                label="Download All Points as Text",
                data=all_points,
                file_name="resume_points.txt",
                mime="text/plain",
            )

        if not experience_points and not project_points:
            st.warning("No clear bullet points were extracted. The PDF might be scanned or formatted in a way that makes extraction difficult.")
            st.info("You can still use the raw text extracted from the PDF.")
