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
  </style>
  """)

  st.markdown("<h2>How ResumeX <span class='hero-badge'>Works</span></h2>", unsafe_allow_html=True)

  st.markdown("""
  <div class='video-container'>
      <iframe src="https://youtube.com/embed/zGo0iO4Ib9U&rel=0?loop=1&playlist=zGo0iO4Ib9U&autoplay=1" title="youtube video" loading="lazy"
      frameborder="0" allow="clipboard-write; encrypted-media; gyroscope; picture-in-picture"></iframe>
  </div>
  """, unsafe_allow_html=True)