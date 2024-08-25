import streamlit as st

st.set_page_config(page_title="Resume Builder", page_icon="📄")

with st.sidebar:
    st.page_link("main.py", label="Welcome")
    st.page_link("pages/app.py", label="Resume Builder")

st.title("Welcome to the Resume Builder")

st.markdown("""
This Resume Builder is designed to help you create a professional, well-formatted resume with ease.
Follow the steps below to create your perfect resume!
""")

with st.expander("How to Use This Resume Builder", expanded=True):
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

with st.expander("Features", expanded=True):
    features = [
        "Easy-to-use interface",
        "Step-by-step resume creation process",
        "Automatic formatting of your resume",
        "PDF generation for easy sharing and printing",
        "Ability to add multiple education and experience entries",
        "Custom sections for skills, languages, certifications, and hobbies",
    ]
    for feature in features:
        st.markdown(f"- {feature}")

with st.expander("About the Developer", expanded=True):
    st.markdown("""
    This Resume Builder was created by Manoj.

    - **GitHub**: [kayozxo](https://github.com/kayozxo)
    - **LinkedIn**: [Penugurthi Manoj](https://linkedin.com/in/penugurthi-manoj)
    - **Email**: penugurthimanoj@gmail.com

    Feel free to reach out if you have any questions or suggestions!
    """)
