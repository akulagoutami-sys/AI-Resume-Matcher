import streamlit as st
import os

# Set page config globally first
st.set_page_config(page_title="AI Resume Matcher PRO", page_icon="✨", layout="wide")

from database.db import init_db
from utils.styles import inject_custom_css

# Inject premium CSS
inject_custom_css()

# Initialize database on startup
if not os.path.exists('database/resume_matcher.db'):
    init_db()

# Simple routing logic based on Streamlit pages
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

def logout():
    from utils.auth import logout_user
    logout_user()
    st.rerun()

# Define pages
login_page = st.Page("pages/login.py", title="Log in", icon="🔐")
signup_page = st.Page("pages/signup.py", title="Sign up", icon="📝")

dashboard_page = st.Page("pages/dashboard.py", title="Dashboard", icon="📊", default=True)
resume_analysis_page = st.Page("pages/resume_analysis.py", title="Resume Analysis", icon="⚖️")
skill_gap_page = st.Page("pages/skill_gap.py", title="Skill Gap Analysis", icon="🎯")
interview_prep_page = st.Page("pages/interview_prep.py", title="Interview Prep", icon="🗣️")
resume_rewrite_page = st.Page("pages/resume_rewrite.py", title="Resume Rewrite", icon="📝")
roadmap_page = st.Page("pages/roadmap.py", title="Career Roadmap", icon="🗺️")

ranker_page = st.Page("pages/multi_ranker.py", title="Multi-Ranker", icon="👥")
export_reports_page = st.Page("pages/export_reports.py", title="Export Reports", icon="📄")

history_page = st.Page("pages/history.py", title="History", icon="🕰️")
profile_page = st.Page("pages/profile.py", title="Profile", icon="👤")
settings_page = st.Page("pages/settings.py", title="Settings", icon="⚙️")

if st.session_state['authenticated']:
    # Show authenticated pages
    pg = st.navigation(
        {
            "Core": [dashboard_page],
            "Insights": [resume_analysis_page, skill_gap_page, interview_prep_page, resume_rewrite_page, roadmap_page],
            "Tools": [ranker_page, export_reports_page],
            "Account": [history_page, profile_page, settings_page]
        }
    )
    with st.sidebar:
        st.write(f"Welcome back, **{st.session_state.get('user_name', 'User')}**")
        if st.button("Log out"):
            logout()
    pg.run()
else:
    # Show unauthenticated pages
    pg = st.navigation([login_page, signup_page])
    pg.run()
