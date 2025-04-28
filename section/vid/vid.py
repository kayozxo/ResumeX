import streamlit as st

def video_section():

  st.html("""
  <style>
      /* Video container */
      .video-container {
          position: relative;
          padding-bottom: 56.25%;
          height: 0;
          overflow: hidden;
          max-width: 100%;
          background-color: var(--card-bg);
          border-radius: 20px;
          border: 1px solid var(--border-color);
      }

      .video-container iframe {
          position: absolute;
          top: 50%;
          left: 50%;
          transform: translate(-50%, -50%);
          width: 98%;
          height: 97%;
          border-radius: 16px !important;
      }

      .video-container h3 {
          position: absolute;
          top: 50%;
          left: 50%;
          transform: translate(-50%, -50%);
          color: var(--text-color) !important;
          font-size: 2rem !important;
          font-weight: 600 !important;
      }
  </style>
  """)

  st.markdown("<h2>How ResumeX <span class='hero-badge'>Works</span></h2>", unsafe_allow_html=True)

  st.markdown("""
  <div class='video-container'>
        <h3>Coming Soon...</h3>
  </div>
  """, unsafe_allow_html=True)