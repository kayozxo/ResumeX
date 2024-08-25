import streamlit as st
from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    HRFlowable,
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from reportlab.lib.units import inch
from io import BytesIO
import streamlit_antd_components as sac
import datetime, re
from pathlib import Path

st.set_page_config(page_title="Resume Builder", page_icon="📄")
with st.sidebar:
    st.page_link("main.py", label="Welcome")
    st.page_link("pages/app.py", label="Resume Builder")

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "style.css"

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


def format_date(date):
    return date.strftime("%b %Y")


def generate_pdf(data):
    buffer = BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        leftMargin=0.5 * inch,
        rightMargin=0.5 * inch,
        topMargin=0.3 * inch,
        bottomMargin=0.3 * inch,
    )
    styles = getSampleStyleSheet()
    story = []

    # Title
    if data["name"]:
        title_style = ParagraphStyle(
            name="Title",
            parent=styles["Heading1"],
            alignment=TA_CENTER,
            fontSize=24,
            spaceAfter=6,
        )
        story.append(Paragraph(f"{data['name']}".upper(), title_style))

    story.append(Spacer(1, 6))
    # Contact Info
    contact_style = ParagraphStyle(
        name="Contact",
        parent=styles["Normal"],
        alignment=TA_CENTER,
        fontSize=10,
        spaceAfter=6,
    )

    contact_parts = []
    if data["email"]:
        contact_parts.append(data["email"])
    if data["phone"]:
        contact_parts.append(data["phone"])
    if data["linkedin"]:
        contact_parts.append(
            f"<link href='{data['linkedin']}'><font color='blue'><u>{data['linkedin']}</u></font></link>"
        )
    if data["github"]:
        contact_parts.append(
            f"<link href='{data['github']}'><font color='blue'><u>{data['github']}</u></font></link>"
        )

    if contact_parts:
        contact_info = " | ".join(contact_parts)
        story.append(Paragraph(contact_info, contact_style))

    story.append(Spacer(1, 12))
    story.append(
        HRFlowable(
            width="100%", thickness=0.5, color=colors.grey, spaceBefore=0, spaceAfter=6
        )
    )

    normal_style = ParagraphStyle(
        name="Normal", parent=styles["Normal"], fontSize=11, spaceAfter=4
    )
    bold_style = ParagraphStyle(
        name="Normal", parent=styles["Normal"], fontSize=12, spaceAfter=4
    )

    # Sections
    sections = [
        ("SUMMARY", "summary"),
        ("EDUCATION", "education"),
        ("EXPERIENCE", "experience"),
        ("ADDITIONAL INFORMATION", "additional_information"),
    ]

    for section_title, section_key in sections:
        if section_key == "education":
            story.append(Paragraph(section_title, styles["Heading2"]))
            for edu in data["education"]:
                if edu["school"] and edu["timeline"]:
                    timeline_str = f"{format_date(edu['timeline'][0])} - {format_date(edu['timeline'][1])}"
                    story.append(
                        Paragraph(
                            f"<b>{edu['school'].title()}</b> | <b>{timeline_str}</b>",
                            bold_style,
                        )
                    )
                if edu["course"]:
                    story.append(Paragraph(f"{edu['course'].title()}", normal_style))
                if edu["grade"]:
                    story.append(
                        Paragraph(f"\u2022 Grade: {edu['grade']}", normal_style)
                    )
                story.append(Spacer(1, 8))

        elif section_key == "experience":
            story.append(Paragraph(section_title, styles["Heading2"]))
            for exp in data["experience"]:
                if exp["company"] and exp["timeline"] and exp["role"]:
                    timeline_str = f"{format_date(exp['timeline'][0])} - {format_date(exp['timeline'][1])}"
                    story.append(
                        Paragraph(
                            f"<b>{exp['company'].title()}, {exp['role'].title()}</b> | <b>{timeline_str}</b>",
                            bold_style,
                        )
                    )
                if exp["experience_summary"]:
                    # Split the experience summary into bullet points
                    bullet_points = re.split(
                        r"\s*-\s+", exp["experience_summary"].strip()
                    )
                    for point in bullet_points:
                        if point:  # Ensure the point is not empty
                            story.append(Paragraph(f"\u2022 {point}", normal_style))
                story.append(Spacer(1, 8))

        elif section_key == "additional_information":
            story.append(Paragraph(section_title, styles["Heading2"]))
            if data["skills"]:
                story.append(
                    Paragraph(f"<b>Skills:</b> {data['skills']}", normal_style)
                )
            if data["languages"]:
                story.append(
                    Paragraph(f"<b>Languages:</b> {data['languages']}", normal_style)
                )
            if data["certifications"]:
                story.append(
                    Paragraph(
                        f"<b>Certifications:</b> {data['certifications']}", normal_style
                    )
                )
            if data["hobbies"]:
                story.append(
                    Paragraph(f"<b>Hobbies:</b> {data['hobbies']}", normal_style)
                )

        elif section_key in data and data[section_key].strip():
            story.append(Paragraph(section_title, styles["Heading2"]))
            story.append(Paragraph(data[section_key], normal_style))

        story.append(Spacer(1, 6))
        story.append(
            HRFlowable(
                width="100%",
                thickness=0.5,
                color=colors.grey,
                spaceBefore=0,
                spaceAfter=6,
            )
        )

    doc.build(story)
    buffer.seek(0)
    return buffer


def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None


def is_valid_phone(phone):
    pattern = r"^\+?[0-9]{10,14}$"
    return re.match(pattern, phone) is not None


def is_valid_url(url):
    pattern = r"^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)$"
    return re.match(pattern, url) is not None


def is_valid_grade(grade):
    try:
        float(grade)
        return True
    except ValueError:
        return False


def main():
    st.title("Resume Builder")
    st.markdown("Built by [Manoj](https://github.com/kayozxo)")

    # Initialize session state
    if "data" not in st.session_state:
        st.session_state.data = {
            "name": "",
            "email": "",
            "phone": "",
            "linkedin": "",
            "github": "",
            "summary": "",
            "education": [],
            "experience": [],
            "skills": "",
            "languages": "",
            "certifications": "",
            "hobbies": "",
        }

    current_step = sac.steps(
        items=[
            sac.StepsItem(title="Basic Info"),
            sac.StepsItem(title="Education"),
            sac.StepsItem(title="Experience"),
            sac.StepsItem(title="Skills"),
            sac.StepsItem(title="Generate PDF"),
        ],
        size="xs",
        return_index=True,
    )

    if current_step == 0:
        with st.form("basic_info_form"):
            st.subheader("Basic Information")
            col1, col2, col3 = st.columns(3)
            with col1:
                name = st.text_input("Full Name", st.session_state.data["name"])
            with col2:
                email = st.text_input("Email", st.session_state.data["email"])
            with col3:
                phone = st.text_input("Phone", st.session_state.data["phone"])

            col4, col5 = st.columns(2)
            with col4:
                linkedin = st.text_input(
                    "LinkedIn Link", st.session_state.data["linkedin"]
                )
            with col5:
                github = st.text_input("GitHub Link", st.session_state.data["github"])

            summary = st.text_area("Summary", st.session_state.data["summary"])
            submit = st.form_submit_button("Save & Continue")

            if submit:
                error = False

                if not name:
                    st.error("Please enter your full name.")
                    error = True

                if not is_valid_email(email):
                    st.error("Please enter a valid email address.")
                    error = True

                if not is_valid_phone(phone):
                    st.error(
                        "Please enter a valid phone number (10-14 digits, optionally starting with +)."
                    )
                    error = True

                if linkedin and not is_valid_url(linkedin):
                    st.error("Please enter a valid LinkedIn URL.")
                    error = True

                if github and not is_valid_url(github):
                    st.error("Please enter a valid GitHub URL.")
                    error = True

                if not error:
                    st.session_state.data.update(
                        {
                            "name": name,
                            "email": email,
                            "phone": phone,
                            "linkedin": linkedin,
                            "github": github,
                            "summary": summary,
                        }
                    )
                    st.success("Basic information saved successfully!")

    elif current_step == 1:
        # Display existing education entries
        for i, edu in enumerate(st.session_state.data["education"]):
            st.write(f"Entry {i+1}: {edu['school']} - {edu['course']}")

        # Form for adding new education entry
        with st.form("education_form"):
            st.subheader("Education")
            col1, col2 = st.columns(2)
            with col1:
                school = st.text_input("School Name")
                start_date = st.date_input(
                    "Start Date",
                    min_value=datetime.date(1900, 1, 1),
                    max_value=datetime.date.today(),
                )
            with col2:
                course = st.text_input("Course Name")
                end_date = st.date_input(
                    "End Date",
                    min_value=datetime.date(1900, 1, 1),
                    max_value=datetime.date(2100, 1, 1),
                )
            grade = st.text_input("Grade (%)")
            submit = st.form_submit_button("Add Education Entry")

            if submit:
                error = False

                if not school:
                    st.error("Please enter the school name.")
                    error = True

                if not course:
                    st.error("Please enter the course name.")
                    error = True

                if start_date >= end_date:
                    st.error("End date must be after start date.")
                    error = True

                if not grade:
                    st.error("Please enter a grade.")
                    error = True
                elif not is_valid_grade(grade):
                    st.error("Please enter a valid grade (integer or decimal number).")
                    error = True

                if not error:
                    new_edu = {
                        "school": school,
                        "course": course,
                        "timeline": (start_date, end_date),
                        "grade": grade,
                    }
                    st.session_state.data["education"].append(new_edu)
                    st.success("Education entry added successfully!")

    elif current_step == 2:
        # Display existing education entries
        for i, exp in enumerate(st.session_state.data["experience"]):
            st.write(f"Entry {i+1}: {exp['company']} - {exp['role']}")

        with st.form("experience_form"):
            st.subheader("Work Experience")
            col1, col2 = st.columns(2)
            with col1:
                company = st.text_input("Company Name")
                start_date_c = st.date_input(
                    "Start Date",
                    min_value=datetime.date(1900, 1, 1),
                    max_value=datetime.date.today(),
                )
            with col2:
                role = st.text_input("Role")
                end_date_c = st.date_input(
                    "End Date",
                    min_value=datetime.date(1900, 1, 1),
                    max_value=datetime.date(2100, 1, 1),
                )
            experience_summary = st.text_area("Experience")
            submit = st.form_submit_button("Add Experience Entry")

            if submit:
                error = False

                if not company:
                    st.error("Please enter the company name.")
                    error = True

                if not role:
                    st.error("Please enter the role name.")
                    error = True

                if start_date_c >= end_date_c:
                    st.error("End date must be after start date.")
                    error = True

                if not experience_summary:
                    st.error("Please add a summary (5 points)")
                    error = True

                if not error:
                    new_exp = {
                        "company": company,
                        "role": role,
                        "timeline": (start_date_c, end_date_c),
                        "experience_summary": experience_summary,
                    }
                    st.session_state.data["experience"].append(new_exp)
                    st.success("Experience entry added successfully!")

    elif current_step == 3:
        with st.form("additional_info_form"):
            st.subheader("Additional Information")
            st.write("Add any additional information separated by commas.")
            skills = st.text_area("Skills", st.session_state.data["skills"])
            languages = st.text_area("Languages", st.session_state.data["languages"])
            certifications = st.text_area(
                "Certifications", st.session_state.data["certifications"]
            )
            hobbies = st.text_area("Hobbies", st.session_state.data["hobbies"])
            submit = st.form_submit_button("Save Additional Information")

            if submit:
                st.session_state.data["skills"] = skills
                st.session_state.data["languages"] = languages
                st.session_state.data["certifications"] = certifications
                st.session_state.data["hobbies"] = hobbies
                st.success("Additional information saved successfully!")

    elif current_step == 4:
        st.subheader("Generate PDF")
        if st.button("Generate Resume PDF"):
            pdf = generate_pdf(st.session_state.data)
            st.download_button(
                label="Download Resume PDF",
                data=pdf,
                file_name=f"{st.session_state.data['name']} - Resume.pdf",
                mime="application/pdf",
            )


if __name__ == "__main__":
    main()
