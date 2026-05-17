import streamlit as st
from modules.extractor import extract_text_from_pdf
from modules.analyzer import extract_skills, calculate_similarity
from modules.ats_scorer import calculate_ats_score, get_match_level
from modules.keyword_optimizer import optimize_keywords
from database.db import save_analysis

st.title("📊 Analysis Dashboard")

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
            resume_text = extract_text_from_pdf(uploaded_file)
            
            if not resume_text:
                st.error("❌ Could not extract text.")
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
                
                st.divider()
                st.subheader("📈 Results Dashboard")
                
                # Render ATS Gauge
                gauge_fig = create_ats_gauge(ats_score)
                st.plotly_chart(gauge_fig, use_container_width=True)
                
                r1, r2, r3 = st.columns(3)
                r1.metric("Match Level", match_level)
                r2.metric("Skills Matched", f"{len(matched_skills)}")
                r3.metric("Missing Skills", f"{len(missing_skills)}")
                
                # Render Pie Chart
                pie_fig = create_skills_pie_chart(matched_skills, missing_skills)
                if pie_fig:
                    st.plotly_chart(pie_fig, use_container_width=True)
                
                from modules.job_recommender import recommend_jobs
                from modules.rewriter import analyze_bullets
                from modules.interview_generator import generate_interview_questions
                from modules.roadmap import generate_roadmap
                
                st.divider()
                
                tab1, tab2, tab3, tab4 = st.tabs(["Resume Analysis", "Rewrite Suggestions", "Interview Prep", "Career Roadmap"])
                
                with tab1:
                    st.subheader("⚖️ Strengths & Weaknesses")
                    c1, c2 = st.columns(2)
                    with c1:
                        st.write("**Matched Skills**")
                        if matched_skills:
                            for s in matched_skills: st.success(s)
                        else: st.info("None")
                    with c2:
                        st.write("**Missing Skills**")
                        if missing_skills:
                            for s in missing_skills: st.error(s)
                        else: st.success("None")
                        
                    st.subheader("💡 Suggestions & Keyword Optimization")
                    if missing_kw:
                        st.warning(f"Consider integrating these missing keywords: {', '.join(missing_kw)}")
                    if ats_score >= 75:
                        st.info("Great resume! Keep it up.")
                    else:
                        st.warning("Consider adding the missing skills to your resume if you have experience with them.")
                        
                    st.subheader("🎯 Job Recommendations")
                    jobs = recommend_jobs(resume_skills)
                    if jobs:
                        for j in jobs:
                            st.write(f"**{j['role']}** - Match: {j['match_pct']}%")
                            st.progress(j['match_pct'] / 100)
                    else:
                        st.write("Upload more skills to get job recommendations.")
                        
                with tab2:
                    st.subheader("📝 Resume Rewrite Suggestions")
                    suggestions = analyze_bullets(resume_text)
                    if suggestions:
                        for idx, s in enumerate(suggestions):
                            st.error(f"**Original ({s['issue']}):** {s['original']}")
                            st.success(f"**Suggestion:** {s['suggestion']}")
                            st.write("---")
                    else:
                        st.success("Your bullet points look strong! No major weak phrases detected.")
                        
                with tab3:
                    st.subheader("🗣️ Interview Prep")
                    questions = generate_interview_questions(missing_skills)
                    if questions:
                        for q in questions:
                            with st.expander(f"{q['type']} - {q['skill']}"):
                                st.write(q['question'])
                    else:
                        st.success("No missing skills detected to generate questions for.")
                        
                with tab4:
                    st.subheader("🗺️ Career Roadmap")
                    target_role = jobs[0]['role'] if jobs else "Target Role"
                    roadmap = generate_roadmap(target_role, missing_skills)
                    for step in roadmap:
                        if isinstance(step, str):
                            st.write(step)
                        else:
                            st.markdown(f"**Step {step['step']}: {step['topic']}** ({step['duration']})")
                            st.write(step['action'])
                
                # --- Export Reports ---
                st.divider()
                st.subheader("📄 Export Reports")
                
                from modules.pdf_exporter import generate_pdf_report
                from modules.excel_exporter import generate_excel_report
                
                pdf_bytes = generate_pdf_report(ats_score, match_level, matched_skills, missing_skills, roadmap)
                excel_bytes = generate_excel_report(matched_skills, missing_skills, jobs)
                
                d1, d2, _ = st.columns([1, 1, 2])
                with d1:
                    st.download_button("📥 Download PDF", data=pdf_bytes, file_name="resume_report.pdf", mime="application/pdf", use_container_width=True)
                with d2:
                    st.download_button("📥 Download Excel", data=excel_bytes, file_name="resume_report.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", use_container_width=True)
