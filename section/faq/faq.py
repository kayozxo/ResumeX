import streamlit as st

def faq_section():

    st.html("""
    <style>
            p {
              color: #fafafa !important;
            }

            .stExpander {
              background-color: var(--card-bg) !important;
              border-radius: 10px !important;
            }

            svg[data-testid="stExpanderToggleIcon"] {
              color: var(--paragraph-color) !important;
            }
    </style>
    """)

    st.markdown("<div class='section'></div>", unsafe_allow_html=True)
    st.markdown("<h2>Frequently Asked <span class='hero-badge'>Questions</span></h2>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([0.2, 0.6, 0.2], gap="small")

    with col2:
      with st.expander("What is ResumeX?"):
          st.write("ResumeX is an AI-powered resume builder that helps you create, enhance, and optimize your resume for job applications. It provides ATS scoring, job description matching, and professional templates.")

      with st.expander("Is ResumeX really free to use?"):
          st.write("Yes! ResumeX is completely free to use. All features, including AI enhancements and PDF export, are available at no cost.")

      with st.expander("How does the AI enhancer work?"):
          st.write("The AI enhancer analyzes your resume and the job description you provide, then suggests improvements and rewrites to help you stand out and increase your ATS score.")

      with st.expander("What is an ATS score?"):
          st.write("ATS (Applicant Tracking System) score measures how well your resume matches a job description. ResumeX helps you optimize your resume to improve this score and increase your chances of getting noticed.")

      with st.expander("Can I download my resume as a PDF?"):
          st.write("Absolutely! Once you finish editing, you can export your resume as a professionally formatted PDF, ready to send to employers.")

      with st.expander("Do I need to create an account?"):
          st.write("No account is required to use ResumeX. You can start building and downloading your resume instantly.")