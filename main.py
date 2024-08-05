import streamlit as st
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from reportlab.lib.units import inch
from io import BytesIO
import streamlit_antd_components as sac

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
    if data['name']:
        title_style = ParagraphStyle(name="Title", parent=styles['Heading1'], alignment=TA_CENTER, fontSize=16, spaceAfter=6)
        story.append(Paragraph(f"{data['name']}", title_style))

    # Contact Info
    contact_style = ParagraphStyle(name="Contact", parent=styles['Normal'], alignment=TA_CENTER, fontSize=10, spaceAfter=6)

    contact_parts = []
    if data['email']:
        contact_parts.append(data['email'])
    if data['phone']:
        contact_parts.append(data['phone'])
    if data['linkedin']:
        contact_parts.append(f"<link href='{data['linkedin']}'><font color='blue'><u>{data['linkedin']}</u></font></link>")
    if data['github']:
        contact_parts.append(f"<link href='{data['github']}'><font color='blue'><u>{data['github']}</u></font></link>")

    if contact_parts:
        contact_info = " | ".join(contact_parts)
        story.append(Paragraph(contact_info, contact_style))

    # Sections
    for section in ['summary', 'education', 'experience', 'skills']:
        if data[section].strip():
            story.append(Paragraph(section.capitalize(), styles['Heading2']))
            story.append(Paragraph(data[section], styles['Normal']))
            story.append(Spacer(1, 6))
            story.append(HRFlowable(width="100%", thickness=0.5, color=colors.grey, spaceBefore=0, spaceAfter=6))

    doc.build(story)
    buffer.seek(0)
    return buffer

def main():
    st.title("Resume Builder")

    # Initialize session state
    if 'data' not in st.session_state:
        st.session_state.data = {
            "name": "", "email": "", "phone": "", "linkedin": "", "github": "",
            "summary": "", "education": "", "experience": "", "skills": ""
        }

    current_step = sac.steps(
        items=[
            sac.StepsItem(title='Basic Info'),
            sac.StepsItem(title='Education'),
            sac.StepsItem(title='Experience'),
            sac.StepsItem(title='Skills'),
            sac.StepsItem(title='Generate PDF'),
        ], size='xs', return_index=True
    )

    if current_step == 0:
        with st.form("basic_info_form"):
            st.subheader("Basic Information")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.session_state.data["name"] = st.text_input("Full Name", st.session_state.data["name"])
            with col2:
                st.session_state.data["email"] = st.text_input("Email", st.session_state.data["email"])
            with col3:
                st.session_state.data["phone"] = st.text_input("Phone", st.session_state.data["phone"])

            col4, col5 = st.columns(2)
            with col4:
                st.session_state.data["linkedin"] = st.text_input("LinkedIn Link", st.session_state.data["linkedin"])
            with col5:
                st.session_state.data["github"] = st.text_input("GitHub Link", st.session_state.data["github"])

            st.session_state.data["summary"] = st.text_area("Summary", st.session_state.data["summary"])
            submit = st.form_submit_button("Save & Continue")

    elif current_step == 1:
        with st.form("education_form"):
            st.subheader("Education")
            st.session_state.data["education"] = st.text_area("Education", st.session_state.data["education"])
            submit = st.form_submit_button("Save & Continue")

    elif current_step == 2:
        with st.form("experience_form"):
            st.subheader("Work Experience")
            st.session_state.data["experience"] = st.text_area("Experience", st.session_state.data["experience"])
            submit = st.form_submit_button("Save & Continue")

    elif current_step == 3:
        with st.form("skills_form"):
            st.subheader("Skills")
            st.session_state.data["skills"] = st.text_area("Skills", st.session_state.data["skills"])
            submit = st.form_submit_button("Save & Continue")

    elif current_step == 4:
        st.subheader("Generate PDF")
        if st.button("Generate Resume PDF"):
            pdf = generate_pdf(st.session_state.data)
            st.download_button(
                label="Download Resume PDF",
                data=pdf,
                file_name=f"{st.session_state.data['name']}-Resume.pdf",
                mime="application/pdf"
            )

    st.write("Current Data:", st.session_state.data)

if __name__ == "__main__":
    main()