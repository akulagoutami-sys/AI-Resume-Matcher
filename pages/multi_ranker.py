import streamlit as st
import pandas as pd
from modules.extractor import extract_text_from_pdf
from modules.analyzer import extract_skills, calculate_similarity
from modules.ats_scorer import calculate_ats_score

st.title("👥 Multi-Resume Ranker")

st.markdown("Upload multiple resumes to rank candidates against a single job description.")

job_description = st.text_area("Job Description:", height=150)
uploaded_files = st.file_uploader("Upload Resumes (PDF)", type=["pdf"], accept_multiple_files=True)

if st.button("Rank Candidates", type="primary"):
    if not job_description or not uploaded_files:
        st.warning("Please provide a job description and at least one resume.")
    else:
        results = []
        progress_bar = st.progress(0)
        
        jd_skills = extract_skills(job_description)
        
        for i, file in enumerate(uploaded_files):
            try:
                text = extract_text_from_pdf(file)
                if not text:
                    continue
                    
                sim_score = calculate_similarity(text, job_description)
                resume_skills = extract_skills(text)
                matched = jd_skills.intersection(resume_skills)
                
                ats = calculate_ats_score(sim_score, matched, jd_skills, text)
                
                # Weighted Final Score (40% Skill Match, 30% ATS, 30% Cosine Sim)
                skill_pct = (len(matched) / len(jd_skills) * 100) if jd_skills else 100
                final_score = (skill_pct * 0.4) + (ats * 0.3) + (sim_score * 0.3)
                
                results.append({
                    "Candidate File": file.name,
                    "Final Score": int(final_score),
                    "ATS Score": ats,
                    "Skill Match %": int(skill_pct),
                    "Matched Skills": len(matched)
                })
            except Exception as e:
                st.error(f"Error processing {file.name}: {e}")
            
            progress_bar.progress((i + 1) / len(uploaded_files))
            
        if results:
            df = pd.DataFrame(results).sort_values(by="Final Score", ascending=False)
            st.success("Ranking Complete!")
            st.dataframe(df, use_container_width=True)
            
            # Compare two resumes UI
            if len(results) >= 2:
                st.divider()
                st.subheader("Compare Candidates")
                c1, c2 = st.columns(2)
                cand1 = c1.selectbox("Select Candidate 1", df['Candidate File'])
                cand2 = c2.selectbox("Select Candidate 2", df['Candidate File'], index=1)
                
                if cand1 and cand2:
                    d1 = df[df['Candidate File'] == cand1].iloc[0]
                    d2 = df[df['Candidate File'] == cand2].iloc[0]
                    
                    c1.metric("Final Score", d1['Final Score'])
                    c1.metric("ATS Score", d1['ATS Score'])
                    
                    c2.metric("Final Score", d2['Final Score'])
                    c2.metric("ATS Score", d2['ATS Score'])
