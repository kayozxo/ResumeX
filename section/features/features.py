import streamlit as st

def features_section():
  st.html("""
  <style>
      .feature-masonry {
          columns: 300px;
          column-gap: 1.5rem;
          width: 100%;
          max-width: 1200px;
          margin: 0 auto 2rem auto;
      }

      .feature-masonry .feature-card {
          display: inline-block;
          width: 100%;
          margin-bottom: 1.5rem;
          vertical-align: top;
      }
      .feature-p {
          color: var(--paragraph-color) !important;
      }
      /* Cards */
      .feature-card {
          background-color: var(--card-bg);
          border-radius: var(--border-radius);
          padding: 1.5rem;
          margin-bottom: 1rem;
          border: 1px solid var(--border-color);
          height: 100%;
          transition: transform 0.3s ease, box-shadow 0.3s ease-in-out;
      }
      .feature-card:hover {
          transform: translateY(-5px);
          box-shadow: 0 10px 20px rgba(0, 0, 0, 0.4);
      }
      /* Section spacing */
      .section {
          margin: 4rem 0;
      }
  </style>
  """)

  st.markdown("<div class='section'></div>", unsafe_allow_html=True)
  st.markdown("<h2>Powerful <span class='hero-badge'>Features</span></h2>", unsafe_allow_html=True)

  st.markdown("""
  <div class="feature-masonry">

    <div class='feature-card'>
        <h3><?xml version="1.0" encoding="UTF-8"?><svg width="1.4rem" height="1.4rem" viewBox="0 0 28 28" stroke-width="1.5" fill="#ffbe1a" xmlns="http://www.w3.org/2000/svg" color="#ffbe1a"><path d="M20 12V5.74853C20 5.5894 19.9368 5.43679 19.8243 5.32426L16.6757 2.17574C16.5632 2.06321 16.4106 2 16.2515 2H4.6C4.26863 2 4 2.26863 4 2.6V21.4C4 21.7314 4.26863 22 4.6 22H11" stroke="#ffbe1a" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M8 10H16M8 6H12M8 14H11" stroke="#131616" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M17.9541 16.9394L18.9541 15.9394C19.392 15.5015 20.102 15.5015 20.5399 15.9394V15.9394C20.9778 16.3773 20.9778 17.0873 20.5399 17.5252L19.5399 18.5252M17.9541 16.9394L14.963 19.9305C14.8131 20.0804 14.7147 20.2741 14.6821 20.4835L14.4394 22.0399L15.9957 21.7973C16.2052 21.7646 16.3988 21.6662 16.5487 21.5163L19.5399 18.5252M17.9541 16.9394L19.5399 18.5252" stroke="#ffbe1a" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M16 2V5.4C16 5.73137 16.2686 6 16.6 6H20" stroke="#131616" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></svg>Easy Resume Creation</h3>
        <p class='feature-p'>Step-by-step interface guides you through creating a professional resume with no design skills needed.</p>
    </div>

    <div class='feature-card'>
        <h3><?xml version="1.0" encoding="UTF-8"?><svg width="1.4rem" height="1.4rem" viewBox="0 0 26 26" fill="#ffbe1a" xmlns="http://www.w3.org/2000/svg" color="#ffbe1a" stroke-width="1.5"><path d="M8 15C12.8747 15 15 12.949 15 8C15 12.949 17.1104 15 22 15C17.1104 15 15 17.1104 15 22C15 17.1104 12.8747 15 8 15Z" fill="#ffbe1a" stroke="#ffbe1a" stroke-width="1.5" stroke-linejoin="round"></path><path d="M2 6.5C5.13376 6.5 6.5 5.18153 6.5 2C6.5 5.18153 7.85669 6.5 11 6.5C7.85669 6.5 6.5 7.85669 6.5 11C6.5 7.85669 5.13376 6.5 2 6.5Z" fill="#ffbe1a" stroke="#ffbe1a" stroke-width="1.5" stroke-linejoin="round"></path></svg>AI-Powered Optimization</h3>
        <p class='feature-p'>Our AI analyzes job descriptions and suggests improvements to make your resume stand out to recruiters.</p>
    </div>

    <div class='feature-card'>
        <h3><?xml version="1.0" encoding="UTF-8"?><svg width="1.4rem" height="1.4rem" stroke-width="1.5" viewBox="0 0 26 26" fill="none" xmlns="http://www.w3.org/2000/svg" color="#ffbe1a"><path d="M20 20H4V4" stroke="#ffbe1a" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M4 16.5L12 9L15 12L19.5 7.5" stroke="#ffbe1a" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></svg>ATS Compatibility</h3>
        <p class='feature-p'>Ensure your resume passes through Applicant Tracking Systems with our ATS-friendly templates.</p>
    </div>

    <div class='feature-card'>
        <h3><?xml version="1.0" encoding="UTF-8"?><svg width="1.4rem" height="1.4rem" viewBox="0 0 26 26" stroke-width="1.5" fill="none" xmlns="http://www.w3.org/2000/svg" color="#ffbe1a"><path d="M3 20.5V6.5C3 5.67157 3.67157 5 4.5 5H14.2515C14.4106 5 14.5632 5.06321 14.6757 5.17574L17.8243 8.32426C17.9368 8.43679 18 8.5894 18 8.74853V20.5C18 21.3284 17.3284 22 16.5 22H4.5C3.67157 22 3 21.3284 3 20.5Z" stroke="#ffbe1a" fill="#ffbe1a" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M14 5V8.4C14 8.73137 14.2686 9 14.6 9H18" stroke="#ffbe1a" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M7 18H10.5H14" stroke="#131616" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M7 14H7.5H8" stroke="#131616" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M7 10H8.5H10" stroke="#131616" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M7 2L16.5 2L21 6.5V19" stroke="#ffbe1a" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></svg>Multiple Sections</h3>
        <p class='feature-p'>Customize your resume with education, experience, skills, certifications, and more.</p>
    </div>

    <div class='feature-card'>
        <h3><?xml version="1.0" encoding="UTF-8"?><svg width="1.4rem" height="1.4rem" stroke-width="1.5" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg" color="#ffbe1a"><path d="M21.1679 8C19.6247 4.46819 16.1006 2 11.9999 2C6.81459 2 2.55104 5.94668 2.04932 11" stroke="#ffbe1a" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M17 8H21.4C21.7314 8 22 7.73137 22 7.4V3" stroke="#ffbe1a" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M2.88146 16C4.42458 19.5318 7.94874 22 12.0494 22C17.2347 22 21.4983 18.0533 22 13" stroke="#ffbe1a" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M7.04932 16H2.64932C2.31795 16 2.04932 16.2686 2.04932 16.6V21" stroke="#ffbe1a" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></svg>Easy Updates</h3>
        <p class='feature-p'>Make changes to your resume anytime and regenerate your PDF with a single click.</p>
    </div>

    <div class='feature-card'>
        <h3><?xml version="1.0" encoding="UTF-8"?><svg width="1.4rem" height="1.4rem" stroke-width="1.5" viewBox="0 0 26 26" fill="none" xmlns="http://www.w3.org/2000/svg" color="#ffbe1a"><path d="M19 3L5 3C3.89543 3 3 3.89543 3 5L3 19C3 20.1046 3.89543 21 5 21H19C20.1046 21 21 20.1046 21 19V5C21 3.89543 20.1046 3 19 3Z" stroke="#ffbe1a" stroke-width="1.5" fill="#ffbe1a" stroke-linecap="round" stroke-linejoin="round"></path><path d="M7 7L17 7" stroke="#131616" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M7 12L17 12" stroke="#131616" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M7 17L13 17" stroke="#131616" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></svg>PDF Export</h3>
        <p class='feature-p'>Download your finished resume as a professionally formatted PDF ready to send to employers.</p>
    </div>

  </div>
  """, unsafe_allow_html=True)