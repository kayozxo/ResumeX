import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="ResumeX - Professional Resume Builder",
    page_icon="Static/icon.svg",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.html (
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Special+Gothic+Expanded+One&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Raleway:ital,wght@0,100..900;1,100..900&display=swap');

    :root {
        --background-color: #212121;
        --secondary-bg: #1e1e1e;
        --text-color: #fafafa;
        --text-dark: #131616;
        --para-color: #999999;
        --accent-color: #ffbe1a;
        --accent-hover: #f5af00;
        --card-bg: #252525;
        --border-color: #333333;
        --border-radius: 0.625rem; /* 10px */
    }

    h1, h2, h3 {
        font-family: "Special Gothic Expanded One", sans-serif !important;
        font-weight: 500 !important;
    }

    h1{font-size: 2.8rem !important;}

    h2 {
        font-size: 2.4rem !important;
        margin-bottom: 2rem !important;
        margin-top: 6rem !important;
        text-align: center !important;
    }

    h3{font-size: 1.8rem !important;}


    h1, h2, h3, li {
        color: var(--text-color) !important;
    }

    p {
        font-family: "Raleway", sans-serif !important;
        font-weight: 400 !important;
        color: var(--paragraph-color) !important;
    }

    .stAppHeader, .stAppFooter {
        visibility: hidden;
    }

    .stAppHeader {
        height: 0rem !important;
    }

    div[data-testid="stSidebarCollapsedControl"] {
        visibility: hidden;
    }

    .material-symbols-outlined {
        font-size: 1rem !important;
        padding-right: 0.4rem !important;
    }

    span[data-testid="stHeaderActionElements"] {
        display: none !important;
    }

    iframe {
        border-radius: var(--border-radius) !important;
    }

    @media only screen and (max-width: 600px) {
        div[data-testid="stMainBlockContainer"] {
            padding: 2rem 2rem 0rem !important;
        }

        div[data-testid="stHeadingWithActionElements"]:has(h1, h2) {
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
        }

        h1, h2 {
            text-align: center !important;
        }

        h1 {
            font-size: 1.78rem !important;
            padding-bottom: 2.5rem !important;
            max-width: 21.6rem !important;
            margin-top: -2rem !important;
        }

        h2 {
            font-size: 1.5rem !important;
            padding-bottom: 0.5rem !important;
        }

        h3 {
            font-size: 1.2rem !important;
        }

        p {
            font-size: 1rem !important;
        }

        .hero-p {
            font-size: 1rem !important;
            text-align: center !important;
            padding-bottom: 0.6rem;
        }

        p:has(span.is-badge) {
            text-align: center !important;
            font-size: 0.6rem !important;
        }

        span.is-badge {
            margin-bottom: 0.8rem !important;
        }
    }

    @media only screen and (min-width: 1200px) {
        div[data-testid="stMainBlockContainer"] {
            padding: 2rem 5rem 0rem !important;
        }


    }

    @media only screen and (min-width: 1670px) {
        div[data-testid="stMainBlockContainer"] {
            padding: 2rem 14.6rem 0rem !important;
        }
    }

    @media only screen and (min-width: 1670px) {
        div[data-testid="stMainBlockContainer"] {
            padding: 2rem 24.2rem 0rem !important;
        }
    }
    /*
    .stMain {
        margin-top: -3rem !important;
    }
    */

    </style>
    """,
)

st.logo(
    "Static/logo.svg", size="large")

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
