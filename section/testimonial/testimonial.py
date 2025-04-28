import streamlit as st

def testimonial_section():
    st.html("""
    <style>
    .testimonial-masonry {
        columns: 300px;
        column-gap: 1.5rem;
        width: 100%;
        max-width: 1200px;
        margin: 0 auto 2rem auto;
    }

    .testimonial-card {
        display: inline-block;
        width: 100%;
        margin: 0 0 1.5rem 0;
        border-radius: 1rem;
        padding: 1.5rem 1.2rem 1.2rem 1.2rem;
        color: #fafafa;
        font-family: 'Raleway', sans-serif;
        position: relative;
        border: none;
        background: #232323;
        transition: box-shadow 0.2s;
        vertical-align: top;
    }

    .testimonial-card.yellow { background: #ffbe1a; color: #131616; }

    .testimonial-card.brown { background: #2d2320; }

    .testimonial-card.dark { background: #232323; }

    .testimonial-card.blue { background: #1a223f; }

    .testimonial-card.tweet { background: #181c24; border: 1px solid #222; }

    .testimonial-card .highlight { background: #fff3cd; color: #131616; padding: 0.1rem 0.3rem; border-radius: 0.2rem; }

    .testimonial-card .highlight-dark { background: #ffbe1a; color: #131616; padding: 0.1rem 0.3rem; border-radius: 0.2rem; }

    .testimonial-card .avatar {
        width: 40px; height: 40px; border-radius: 50%; object-fit: cover; margin-right: 0.7rem; border: 2px solid #444;
        vertical-align: middle;
    }
    .testimonial-card .user {
        display: flex;
        align-items: center;
        margin-top: 1.2rem;
    }
    .testimonial-card .username {
        font-weight: 600; font-size: 1rem;
        margin-bottom: -0.4rem;
    }
    .testimonial-card .handle {
        font-size: 0.95rem; color: #bbb;
    }
    .testimonial-card .tweet-img {
        width: 100%; border-radius: 0.7rem; margin-top: 0.7rem;
    }
    </style>
    """)
    st.markdown("<div class='section'></div>", unsafe_allow_html=True)
    st.markdown("<h2>What Users <span class='hero-badge'>Say</span></h2>", unsafe_allow_html=True)

    st.markdown("""
    <div class="testimonial-masonry">

      <div class="testimonial-card yellow">
        <div style="font-size:1.05rem; font-weight:500; margin-bottom:0.7rem;">
          ResumeX helped me land my dream job! The AI suggestions made my resume stand out instantly.
        </div>
        <hr/>
        <div class="user">
          <img class="avatar" src="https://randomuser.me/api/portraits/women/13.jpg" loading="lazy" alt="Priya avatar" fetchpriority="low"/>
          <div>
            <div class="username">Priya Sharma</div>
            <div class="handle" style="color: #414141;">@priyasharma</div>
          </div>
        </div>
      </div>

      <div class="testimonial-card brown">
        <div style="font-size:1.05rem;">
          The ATS score feature is a game changer. I could see exactly how my resume matched the job description and improved it in minutes!
        </div>
        <hr/>
        <div class="user">
          <img class="avatar" src="https://randomuser.me/api/portraits/men/21.jpg" alt="James avatar" loading="lazy" fetchpriority="low"/>
          <div>
            <div class="username">James Lee</div>
            <div class="handle">@jameslee</div>
          </div>
        </div>
      </div>

      <div class="testimonial-card dark">
        <div style="font-size:1.05rem;">
          I love how ResumeX gives real-time feedback and AI-powered enhancements. <span class="highlight">My resume never looked better!</span>
        </div><hr/>
        <div class="user">
          <img class="avatar" src="https://randomuser.me/api/portraits/women/68.jpg" loading="lazy" alt="Emily avatar" fetchpriority="low"/>
          <div>
            <div class="username">Emily Chen</div>
            <div class="handle">@emchen</div>
          </div>
        </div>
      </div>

      <div class="testimonial-card tweet">
        <div style="display:flex;align-items:center;">
          <img class="avatar" src="https://randomuser.me/api/portraits/men/12.jpg" loading="lazy" alt="Rahul avatar" fetchpriority="low"/>
          <div>
            <span style="font-weight:600;">Rahul Verma</span> <span style="color:#1da1f2;">&#10003;</span><br>
            <span class="handle">@rahulv</span>
          </div>
        </div>
        <div style="margin-top:0.7rem;">
          Just got an interview call after updating my resume with ResumeX's AI enhancer. <span class="highlight-dark">Highly recommend!</span>
        </div>
        <img class="tweet-img" src="https://i.imgur.com/AywE5DA.jpeg" alt="pic" loading="lazy" fetchpriority="low"/>
        <div style="font-size:0.93rem; color:#aaa; margin-top:0.5rem;">9:15 AM · Mar 2, 2025</div>
      </div>
      <div class="testimonial-card brown">
        <div style="font-size:1.05rem;">
          The job description matching tool is so accurate. I could tailor my resume for every application and saw a huge increase in responses.
        </div>
        <hr/>
        <div class="user">
          <img class="avatar" src="https://randomuser.me/api/portraits/men/23.jpg" loading="lazy" alt="Carlos avatar" fetchpriority="low"/>
          <div>
            <div class="username">Carlos Mendez</div>
            <div class="handle">@carlosm</div>
          </div>
        </div>
      </div>

      <div class="testimonial-card yellow">
        <div style="font-size:1.05rem; font-weight:500; margin-bottom:0.7rem;">
          ResumeX's templates are modern and professional. I created a stunning resume in less than 10 minutes!
        </div>
        <hr/>
        <div class="user">
          <img class="avatar" src="https://randomuser.me/api/portraits/women/56.jpg" loading="lazy" alt="Sara avatar" fetchpriority="low"/>
          <div>
            <div class="username">Sara Kim</div>
            <div class="handle" style="color: #414141;">@sarakim</div>
          </div>
        </div>
      </div>

      <div class="testimonial-card dark">
        <div style="font-size:1.05rem;">
          The AI enhancer rewrote my work experience section and made it so much more impactful. <span class="highlight">Got shortlisted twice this week!</span>
        </div>
        <hr/>
        <div class="user">
          <img class="avatar" src="https://randomuser.me/api/portraits/men/77.jpg" loading="lazy" alt="Amit avatar" fetchpriority="low"/>
          <div>
            <div class="username">Amit Patel</div>
            <div class="handle">@amitpatel</div>
          </div>
        </div>
      </div>

      <div class="testimonial-card blue">
        <div style="font-size:1.05rem;">
          As a recruiter, I recommend ResumeX to all job seekers. The ATS score and AI suggestions really make a difference.
        </div><hr/>
        <div class="user">
          <img class="avatar" src="https://randomuser.me/api/portraits/women/65.jpg" loading="lazy" alt="Linda avatar" fetchpriority="low"/>
          <div>
            <div class="username">Linda Evans</div>
            <div class="handle">@lindaevans</div>
          </div>
        </div>
      </div>

      <div class="testimonial-card tweet">
        <div style="display:flex;align-items:center;">
          <img class="avatar" src="https://randomuser.me/api/portraits/men/34.jpg" loading="lazy" alt="Harsh avatar" fetchpriority="low"/>
          <div>
            <span style="font-weight:600;">Harsh Gupta</span> <span style="color:#1da1f2;">&#10003;</span><br>
            <span class="handle">@harshg</span>
          </div>
        </div>
        <div style="margin-top:0.7rem;">
          ResumeX's AI enhancer gave my resume a 92 ATS score. Recruiters finally noticed me!
        </div>
        <div style="font-size:0.93rem; color:#aaa; margin-top:0.5rem;">7:42 PM · Feb 25, 2025</div>
      </div>

    </div>
    """, unsafe_allow_html=True)