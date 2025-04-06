import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="ResumeX - Professional Resume Builder",
    page_icon="📄",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.html (
    """
    <style>
    .stSidebar {
        background-color: #141415 !important;
    }
    .stAppHeader, .stAppFooter {
        visibility: hidden;
    }
    [data-testid="stExpander"] details {
        border-radius: 24px;
    }
    [data-testid="stFormSubmitButton"] button {
        border-radius: 12px;
    }
    .stForm {
        border-radius: 24px !important;
    }
    .st-key-generate_pdf_button button {
        border-radius: 50px;
    }
    .stAlertContainer {
        border-radius: 12px;
    }

    </style>
    """,
)

welcome_page = st.Page(
    page="views/welcome.py",
    title="Welcome",
    icon=":material/home:",
    default=True,
)

app_page = st.Page(
    page="views/app.py",
    title="Resume Builder",
    icon=":material/edit_square:",
)

ai_page = st.Page(
    page="views/ai.py",
    title="Resume Enhancer",
    icon=":material/star:",
)

pg = st.navigation(pages=[welcome_page, app_page, ai_page])
pg.run()
