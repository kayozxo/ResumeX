import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from section.hero.hero import hero_section
from section.vid.vid import video_section
from section.features.features import features_section
from section.testimonial.testimonial import testimonial_section
from section.faq.faq import faq_section
from section.cta.cta import cta_section
from section.footer.footer import footer_section
import streamlit.components.v1 as components

# Custom CSS for dark theme and modern styling
st.html("""
<head>
    <meta name="description" content="Create or Enhance your resume in minutes, not in days!">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<style>
    /* Dark theme colors */
    :root {
        --background-color: #212121;
        --secondary-bg: #1e1e1e;
        --text-color: #fafafa;
        --text-dark: #131616;
        --accent-color: #ffbe1a;
        --accent-hover: #f5af00;
        --paragraph-color: #999999;
        --card-bg: rgba(37, 37, 37, 0.4);
        --border-color: #444444;
        --border-radius: 0.625rem; /* 10px */
    }

    /* Main background */
    .main .block-container {
        background-color: var(--background-color);
        padding: 2rem;
        max-width: 1200px;
        margin: 0 auto;
    }

    hr {
        border-color: rgba(68, 68, 68, 0.5) !important;
        margin: 1.2rem 0rem !important;
    }

    /* Footer */


    /* Custom divider */
    .divider {
        height: 4px;
        background: linear-gradient(90deg, transparent, var(--accent-color), transparent);
        margin: 2rem 0;
        border-radius: 2px;
    }

    /* Section spacing */
    .section {
        margin: 4rem 0;
    }

    .hero-badge {
        background-color: var(--text-color);
        padding: 0rem 0.5rem;
        color: var(--text-dark);
        transform: rotate(-2deg);
        display: inline-block;
    }

    svg {
        margin-right: 0.2rem !important;
    }



    /*
    button[data-testid="stBaseButton-headerNoPadding"] {
        visibility: hidden;
    }
    */

</style>
""")

@st.dialog("Suggest a feature", width="large")
def rating_dialog():

  components.iframe("https://insigh.to/b/resumex", height=500, scrolling=True)

from streamlit_extras.floating_button import floating_button
if floating_button(":material/star:"):
    rating_dialog()


# nav section
st.image("./Static/logo.svg", width=140)


# hero section
hero_section()


# Divider
#st.markdown("<div class='divider'></div>", unsafe_allow_html=True)


# How it works section with video
video_section()


# Features section
features_section()


# FAQ section
faq_section()


#Testimonials
testimonial_section()


# CTA section
cta_section()


# Footer
footer_section()