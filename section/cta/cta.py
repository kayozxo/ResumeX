import streamlit as st

def cta_section():

  st.html("""
  <style>
      .st-key-getStartedButton button{
            background-color: var(--accent-color) !important;
            color: white !important;
            border-radius: var(--border-radius) !important;
            padding: 0.75rem 1.5rem !important;
            margin-bottom: 6rem !important;
            font-weight: bold !important;
            border: none !important;
            transition: all 0.3s ease-in-out !important;
        }

        .st-key-getStartedButton:hover button{
            background-color: var(--accent-hover) !important;
        }

        .st-key-getStartedButton p{
            font-size: 1rem !important;
            color: #131616 !important;
            font-weight: bold !important;
            transition: all 0.3s ease-in-out;
        }

        .st-key-getStartedButton:hover p{
            transform: scale(1.05);
        }

  </style>
  """)

  # Call to action
  col1, col2, col3 = st.columns([0.2, 0.6, 0.2], gap="small")

  with col2:
      st.markdown("<div class='section'></div>", unsafe_allow_html=True)
      st.markdown("""
          <h2>Create, Enhance, Succeed!</h2>
          <p style='font-size: 1.2rem; margin: -1rem 0rem 3rem 0rem; color: var(--paragraph-color) !important; text-align: center;'>Build your career-winning resume in minutes!</p>
      """, unsafe_allow_html=True)

      if st.button(":material/edit: Get Started Now", type="primary", use_container_width=True, key="getStartedButton"):
          st.switch_page("views/app.py")