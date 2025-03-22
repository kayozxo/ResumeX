import streamlit as st


st.title("✨ Welcome to the ResumeX!")

st.markdown("""
Resumex is designed to help you create a professional, well-formatted resume with ease.
Follow the steps below to create your perfect resume!
""")

if st.button("Start Building Your Resume", type="secondary",  use_container_width=True, icon=":material/arrow_forward:", key="startButton"):
    st.switch_page("views/app.py")

st.html(
    """
    <style>
    .st-key-startButton button{
        background-color: #00b809 !important;
    }
    .st-key-startButton button:hover{
        background-color: #00cc0a !important;
    }
    .st-key-startButton p{
        color: #fafafa !important;
    }
    </style>
    """,
)

with st.expander("How to Use This Resume Builder", expanded=True, icon=":material/question_mark:"):
    st.markdown("""
    1. **Basic Information**: Enter your personal details such as name, contact information, and a brief summary.
    2. **Education**: Add your educational background. You can add multiple entries.
    3. **Experience**: Input your work experience. Remember to use bullet points for better formatting (see tip below).
    4. **Skills**: List your skills, languages, certifications, and hobbies.
    5. **Generate PDF**: Review your information and generate your resume as a PDF.

    **Pro Tip**: When entering your experience, use '- ' (hyphen followed by a space) at the start of each new point to create bullet points in your PDF resume.

    Example:
    ```
    - Developed a new product feature that increased user engagement by 25%
    - Led a team of 5 developers in an Agile environment
    - Implemented CI/CD pipelines, reducing deployment time by 40%
    ```
    """)

with st.expander("Features", expanded=True, icon=":material/check:"):
    st.markdown("""
    - Easy-to-use interface
    - Step-by-step resume creation process
    - Automatic formatting of your resume
    - PDF generation for easy sharing and printing
    - Ability to add multiple education and experience entries
    - Custom sections for skills, languages, certifications, and hobbies
    """)


with st.expander("About the Developer", expanded=True, icon=":material/person_4:"):
    st.markdown("""
    This Resume Builder was created by Manoj.

    - **GitHub**: [kayozxo](https://github.com/kayozxo)
    - **LinkedIn**: [Penugurthi Manoj](https://linkedin.com/in/penugurthi-manoj)
    - **Email**: penugurthimanoj@gmail.com

    Feel free to reach out if you have any questions or suggestions!
    """)
