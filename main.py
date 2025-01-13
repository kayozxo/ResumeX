import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Resume Builder", page_icon="📄")

st.html (
    """
    <style>
    .stSidebar {
        background-color: #141415 !important;
    }
    .stAppHeader, .stAppFooter {
        visibility: hidden;
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

pg = st.navigation(pages=[welcome_page, app_page])
pg.run()
