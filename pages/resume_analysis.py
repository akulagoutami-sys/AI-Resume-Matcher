import streamlit as st
from modules.job_recommender import recommend_jobs
from charts.visualizations import create_ats_gauge

st.title("⚖️ Suggestions & Keyword Optimization")

if 'current_analysis' not in st.session_state:
    st.warning("⚠️ No resume analyzed yet. Please upload a resume on the Dashboard first.")
    st.stop()

analysis = st.session_state['current_analysis']
matched_skills = analysis.get('matched_skills', set())
missing_skills = analysis.get('missing_skills', set())
missing_kw = analysis.get('missing_kw', [])
ats_score = analysis.get('ats_score', 0)
resume_skills = analysis.get('resume_skills', set())

with st.container(border=True):
    st.subheader("🚀 ATS Optimization Score")
    
    # We reuse the gauge chart for optimization context
    gauge_fig = create_ats_gauge(ats_score)
    st.plotly_chart(gauge_fig, use_container_width=True)
    
    if ats_score >= 75:
        st.info("🔥 Great resume! Your keyword optimization is strong.")
    else:
        st.warning("⚠️ Your optimization score is low. Consider adding the missing skills and keywords below.")

with st.container(border=True):
    st.subheader("💡 Keyword Analysis")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### ✅ Detected Skills")
        if matched_skills:
            html = ""
            for s in matched_skills:
                html += f"<span class='skill-chip matched'>{s}</span>"
            st.markdown(html, unsafe_allow_html=True)
        else:
            st.info("None detected.")
            
    with c2:
        st.markdown("#### ❌ Missing Skills")
        if missing_skills:
            html = ""
            for s in missing_skills:
                html += f"<span class='skill-chip missing'>{s}</span>"
            st.markdown(html, unsafe_allow_html=True)
        else:
            st.success("None missing!")

with st.container(border=True):
    st.subheader("🌟 Recommended Contextual Keywords")
    if missing_kw:
        html = ""
        for kw in missing_kw:
             html += f"<span class='skill-chip recommended'>⚡ {kw}</span>"
        st.markdown(html, unsafe_allow_html=True)
    else:
        st.write("Your context keywords look good.")

with st.container(border=True):
    st.subheader("🎯 Top Job Matches")
    jobs = recommend_jobs(resume_skills)
    if jobs:
        for j in jobs:
            st.markdown(f"**{j['role']}**")
            st.progress(j['match_pct'] / 100)
    else:
        st.write("Upload more skills to get job recommendations.")
