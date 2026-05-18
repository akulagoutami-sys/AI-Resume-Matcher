import streamlit as st
from modules.roadmap import generate_roadmap
from modules.job_recommender import recommend_jobs

st.title("🗺️ 6-Month Career Roadmap")

if 'current_analysis' not in st.session_state:
    st.warning("⚠️ No resume analyzed yet. Please upload a resume on the Dashboard first.")
    st.stop()

analysis = st.session_state['current_analysis']
missing_skills = analysis.get('missing_skills', set())
resume_skills = analysis.get('resume_skills', set())

with st.container(border=True):
    st.markdown("Your personalized, highly-detailed 6-month action plan to acquire missing skills and land your target role.")
    
    jobs = recommend_jobs(resume_skills)
    target_role = jobs[0]['role'] if jobs else "Senior Engineer"
    st.markdown(f"### Target Role: **{target_role}**")
    
    roadmap = generate_roadmap(target_role, missing_skills)
    
    # Render the custom vertical timeline HTML
    timeline_html = '<div class="timeline-container"><div class="timeline-line"></div>'
    
    for item in roadmap:
        timeline_html += f'''
        <div style="position: relative; margin-bottom: 30px;">
            <div class="timeline-node"></div>
            <div class="timeline-content" style="margin-left: 40px;">
                <h4 style="margin-top: 0; color: #c084fc;">Month {item["month"]}: {item["skill"]}</h4>
                <p style="margin-bottom: 5px;"><strong>📚 Resources:</strong> {item["resources"]}</p>
                <p style="margin-bottom: 5px;"><strong>💻 Mini Project:</strong> {item["project"]}</p>
                <p style="margin-bottom: 0px; color: #4ade80;"><strong>🎯 Outcome:</strong> {item["outcome"]}</p>
            </div>
        </div>
        '''
        
    timeline_html += '</div>'
    
    st.markdown(timeline_html, unsafe_allow_html=True)
