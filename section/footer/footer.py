import streamlit as st

def footer_section():

  st.html("""
  <style>
    .footer {
            padding: 2rem 0;
            border-top: 1px solid var(--border-color);
            text-align: center;
            margin-top: 3rem;
            width: 99.5vw;
            max-width: 99.5vw;
            position: relative;
            left: 50%;
            right: 50%;
            transform: translateX(-50%);
            box-sizing: border-box;
        }
  </style>
  """)

  st.markdown("""
  <div class='footer'>
      <p>© 2025 ResumeX | Professional Resume Builder & Enhancer</p>
      <p style='font-size: 0.9rem; margin-top: 0.5rem;'>
          Built with ❤️ by Manoj
      </p>
  </div>
  """, unsafe_allow_html=True)