import streamlit as st
import os

# Set page config globally first
st.set_page_config(page_title="AI Resume Matcher PRO", page_icon="📄", layout="wide")

from database.db import init_db

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
ranker_page = st.Page("pages/multi_ranker.py", title="Multi-Ranker", icon="👥")
history_page = st.Page("pages/history.py", title="History", icon="🕰️")
profile_page = st.Page("pages/profile.py", title="Profile", icon="👤")

if st.session_state['authenticated']:
    # Show authenticated pages
    pg = st.navigation(
        {
            "Main": [dashboard_page, ranker_page, history_page],
            "Account": [profile_page]
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
