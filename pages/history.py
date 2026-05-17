import streamlit as st
import pandas as pd
from database.db import get_analyses_by_user

st.title("🕰️ Analysis History")

user_id = st.session_state.get('user_id')
if user_id:
    analyses = get_analyses_by_user(user_id)
    if not analyses:
        st.info("No past analyses found. Go to the dashboard to analyze a resume!")
    else:
        st.write(f"Found {len(analyses)} past analyses.")
        
        # Convert to DataFrame for nice table
        data = []
        for row in analyses:
            data.append({
                "Date": row['created_at'],
                "Resume": row['resume_filename'],
                "Job Title": row['job_title'],
                "ATS Score": row['ats_score'],
                "Match %": row['match_pct']
            })
            
        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True)
else:
    st.error("User not found in session.")
