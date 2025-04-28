import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space

def hero_section():
  st.html("""
  <style>
      .hero-p {
          font-weight: 600 !important;
          color: var(--paragraph-color) !important;
      }

      /* Custom button styling */
      .st-key-startButton button{
          background-color: var(--accent-color) !important;
          color: white !important;
          border-radius: var(--border-radius) !important;
          padding: 0.75rem 1.5rem !important;
          font-weight: bold !important;
          border: none !important;
          transition: all 0.3s ease-in-out !important;
      }

      .st-key-startButton:hover button{
          background-color: var(--accent-hover) !important;
      }

      .st-key-startButton p{
          font-size: 1rem !important;
          color: #131616 !important;
          font-weight: bold !important;
          transition: all 0.3s ease-in-out;
      }

      .st-key-startButton:hover p{
          transform: scale(1.05);
      }

      .st-key-aiButton button{
          background-color: transparent;
          border: 1px solid var(--text-color) !important;
          border-radius: var(--border-radius) !important;
          padding: 0.75rem 1.5rem !important;
          transition: all 0.3s ease-in-out;
      }

      .st-key-aiButton p{
          font-size: 1rem !important;
          color: var(--text-color) !important;
          font-weight: bold !important;
          transition: all 0.3s ease-in-out;
      }

      .st-key-aiButton:hover button{
          background-color: var(--text-color);
      }

      .st-key-aiButton:hover p{
          color: var(--text-dark) !important;
          transform: scale(1.05);
      }

  </style>
  """)

  st.title("")
  # Hero Section
  col1, col2 = st.columns(2, gap="large")

  with col1:
      st.markdown("<h1 style='font-size: 2.8rem'>Create your resume in minutes, <span class='hero-badge'>not days</span></h1>", unsafe_allow_html=True)
      st.markdown("""
      <p style='font-size: 1.2rem; margin-bottom: 2rem;' class='hero-p'>
      ResumeX is designed to help you create a professional, well-formatted resume with ease.
      Stand out from the crowd with AI-powered resume optimization tailored to job descriptions.
      </p>
      """, unsafe_allow_html=True)

      btn1, btn2 = st.columns(2)

      with btn1:
          if st.button(":material/edit: Build Your Resume", type="primary", key="startButton", use_container_width=True):
              st.switch_page("views/app.py")
      with btn2:
          if st.button(":material/bolt: Enhance Your Resume", type="secondary", key="aiButton", use_container_width=True):
              st.switch_page("views/ai.py")

      st.markdown(":green-badge[:material/check: 100% Free] &nbsp;&nbsp; :blue-badge[:material/account_circle: No signup] &nbsp;&nbsp; :orange-badge[:material/lock: Privacy focused]")

  with col2:
    _, col3 = st.columns([0.1, 0.9])
    with col3:
        st.image("./Static/hero-img-3d.svg", use_container_width=True)