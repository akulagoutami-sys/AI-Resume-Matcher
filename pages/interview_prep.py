import streamlit as st
from modules.interview_generator import generate_interview_questions

st.title("🗣️ Interview Prep")

if 'current_analysis' not in st.session_state:
    st.warning("⚠️ No resume analyzed yet. Please upload a resume on the Dashboard first.")
    st.stop()

analysis = st.session_state['current_analysis']
matched_skills = analysis.get('matched_skills', set())
missing_skills = analysis.get('missing_skills', set())
resume_text = analysis.get('resume_text', "")
job_description = analysis.get('job_description', "")

with st.container(border=True):
    st.markdown("We've generated custom interview questions based on your resume and the target job description.")
    questions = generate_interview_questions(matched_skills, missing_skills, resume_text, job_description)
    if questions:
        st.write(f"**Generated {len(questions)} tailored interview questions:**")
        for q in questions:
            with st.expander(f"[{q['category']}] {q['skill']} - {q['question']}"):
                st.write(f"💡 **Hint:** {q['hint']}")
    else:
        st.success("No specific skills detected to generate questions for. Keep practicing general behavioral questions!")
