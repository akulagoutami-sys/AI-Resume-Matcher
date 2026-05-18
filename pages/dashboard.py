import streamlit as st
from utils.styles import render_hero
from modules.extractor import extract_text_from_pdf
from modules.analyzer import extract_skills, calculate_similarity
from modules.ats_scorer import calculate_ats_score, get_match_level
from modules.keyword_optimizer import optimize_keywords
from database.db import save_analysis

# Render premium animated title
render_hero()

col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Job Description")
    job_description = st.text_area("Paste JD here:", height=250)

with col2:
    st.subheader("2. Upload Resume")
    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
    analyze_btn = st.button("🚀 Analyze", type="primary", use_container_width=True)

if analyze_btn:
    if not job_description.strip() or not uploaded_file:
        st.warning("⚠️ Please provide both a job description and a resume.")
    else:
        with st.spinner("Analyzing..."):
            try:
                resume_text = extract_text_from_pdf(uploaded_file)
                
                if not resume_text:
                    st.error("❌ Could not extract text from the PDF. It may be an image-based PDF or corrupted.")
                else:
                    sim_score = calculate_similarity(resume_text, job_description)
                    
                    resume_skills = extract_skills(resume_text)
                    jd_skills = extract_skills(job_description)
                    
                    matched_skills = jd_skills.intersection(resume_skills)
                    missing_skills = jd_skills - resume_skills
                    
                    ats_score = calculate_ats_score(sim_score, matched_skills, jd_skills, resume_text)
                    match_level, level_color = get_match_level(ats_score)
                    
                    found_kw, missing_kw = optimize_keywords(resume_text, job_description)
                    
                    # Save to DB
                    if st.session_state.get('authenticated'):
                        save_analysis(
                            st.session_state['user_id'],
                            uploaded_file.name,
                            "Custom Job", 
                            ats_score,
                            int(sim_score),
                            ",".join(matched_skills),
                            ",".join(missing_skills)
                        )
                    
                    from charts.visualizations import create_skills_pie_chart, create_ats_gauge
                    
                    # Save analysis to session state
                    st.session_state['current_analysis'] = {
                        "resume_text": resume_text,
                        "job_description": job_description,
                        "matched_skills": matched_skills,
                        "missing_skills": missing_skills,
                        "missing_kw": missing_kw,
                        "ats_score": ats_score,
                        "resume_skills": resume_skills,
                        "match_level": match_level
                    }
                    
                    st.divider()
                    st.subheader("📈 Results Overview")
                    
                    # Render ATS Gauge
                    gauge_fig = create_ats_gauge(ats_score)
                    st.plotly_chart(gauge_fig, use_container_width=True)
                    
                    st.success("✅ Analysis Complete! Use the sidebar navigation to explore detailed insights like Interview Prep, Skill Gap, and Resume Rewrite.")
                    
            except Exception as e:
                st.error(f"An unexpected error occurred during analysis: {e}")
                st.info("Please verify your PDF is text-readable and try again.")
