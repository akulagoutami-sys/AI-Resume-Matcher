import streamlit as st
from charts.visualizations import create_skills_pie_chart

st.title("🎯 Skill Gap Analysis")

if 'current_analysis' not in st.session_state:
    st.warning("⚠️ No resume analyzed yet. Please upload a resume on the Dashboard first.")
    st.stop()

analysis = st.session_state['current_analysis']
matched_skills = analysis.get('matched_skills', set())
missing_skills = analysis.get('missing_skills', set())

with st.container(border=True):
    st.subheader("Skill Coverage")
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Skills Matched", f"{len(matched_skills)}")
    c2.metric("Missing Skills", f"{len(missing_skills)}")
    
    total = len(matched_skills) + len(missing_skills)
    match_rate = int((len(matched_skills) / total * 100)) if total > 0 else 0
    c3.metric("Coverage %", f"{match_rate}%")
    
    # Render Pie Chart
    pie_fig = create_skills_pie_chart(matched_skills, missing_skills)
    if pie_fig:
        st.plotly_chart(pie_fig, use_container_width=True)
