import streamlit as st
from modules.pdf_exporter import generate_pdf_report
from modules.excel_exporter import generate_excel_report
from modules.job_recommender import recommend_jobs
from modules.roadmap import generate_roadmap

st.title("📄 Export Reports")

if 'current_analysis' not in st.session_state:
    st.warning("⚠️ No resume analyzed yet. Please upload a resume on the Dashboard first.")
    st.stop()

analysis = st.session_state['current_analysis']
ats_score = analysis.get('ats_score', 0)
match_level = analysis.get('match_level', 'Unknown')
matched_skills = analysis.get('matched_skills', set())
missing_skills = analysis.get('missing_skills', set())
resume_skills = analysis.get('resume_skills', set())

jobs = recommend_jobs(resume_skills)
target_role = jobs[0]['role'] if jobs else "Target Role"
roadmap = generate_roadmap(target_role, missing_skills)

with st.container(border=True):
    st.markdown("Download your complete AI analysis reports for offline review or sharing.")
    
    pdf_bytes = generate_pdf_report(ats_score, match_level, matched_skills, missing_skills, roadmap)
    excel_bytes = generate_excel_report(matched_skills, missing_skills, jobs)
    
    d1, d2 = st.columns(2)
    with d1:
        st.download_button("📥 Download PDF Report", data=pdf_bytes, file_name="resume_report.pdf", mime="application/pdf", use_container_width=True)
    with d2:
        st.download_button("📥 Download Excel Data", data=excel_bytes, file_name="resume_report.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", use_container_width=True)
