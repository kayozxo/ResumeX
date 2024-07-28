import streamlit as st
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from reportlab.lib.units import inch
from io import BytesIO

def generate_pdf(data):
    buffer = BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        leftMargin=0.5*inch,
        rightMargin=0.5*inch,
        topMargin=0.5*inch,
        bottomMargin=0.5*inch
    )
    styles = getSampleStyleSheet()
    story = []

    # Title
    title_style = ParagraphStyle(name="Title", parent=styles['Heading1'], alignment=TA_CENTER)
    story.append(Paragraph(f"{data['name']}", title_style))

    # Contact Info
    contact_style = ParagraphStyle(name="Contact", parent=styles['Normal'], alignment=TA_CENTER)

    contact_info = (
        f"{data['email']} | {data['phone']} | "
        f"<link href='{data['linkedin']}'><font color='blue'><u>{data['linkedin']}</u></font></link> | "
        f"<link href='{data['github']}'><font color='blue'><u>{data['github']}</u></font></link>"
    )
    story.append(Paragraph(contact_info, contact_style))
    story.append(Spacer(1, 12))

    # Sections
    for section in ['summary', 'education', 'experience', 'skills']:
        story.append(Paragraph(section.capitalize(), styles['Heading2']))
        story.append(Paragraph(data[section], styles['Normal']))
        story.append(Spacer(1, 6))
        story.append(HRFlowable(width="100%", thickness=1, color=colors.black, spaceBefore=1, spaceAfter=1))
        story.append(Spacer(1, 12))

    doc.build(story)
    buffer.seek(0)
    return buffer

def main():
    st.title("Resume Builder")

    # Collect user information
    with st.form("basic_info_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            name = st.text_input("Full Name")
        with col2:
            email = st.text_input("Email")
        with col3:
            phone = st.text_input("Phone")
        col4, col5 = st.columns(2)
        with col4:
            linkedin = st.text_input("LinkedIn Link")
        with col5:
            github = st.text_input("GitHub Link")
        summary = st.text_area("Professional Summary")
        submit = st.form_submit_button("Save")

    education = st.text_area("Education")
    experience = st.text_area("Work Experience")
    skills = st.text_area("Skills")

    if submit:
        data = {
            "name": name,
            "email": email,
            "phone": phone,
            "linkedin": linkedin,
            "github": github,
            "summary": summary,
            "education": education,
            "experience": experience,
            "skills": skills
        }
        pdf = generate_pdf(data)
        st.download_button(
            label="Download Resume PDF",
            data=pdf,
            file_name="resume.pdf",
            mime="application/pdf"
        )

if __name__ == "__main__":
    main()