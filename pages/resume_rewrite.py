import streamlit as st
from modules.rewriter import analyze_bullets

st.title("📝 AI Resume Rewrite")

if 'current_analysis' not in st.session_state:
    st.warning("⚠️ No resume analyzed yet. Please upload a resume on the Dashboard first.")
    st.stop()

analysis = st.session_state['current_analysis']
resume_text = analysis.get('resume_text', "")

with st.container(border=True):
    st.markdown("### Bullet Point Optimizer")
    st.markdown("We've scanned your resume for weak action verbs and passive phrases. Below are AI-enhanced versions of your bullet points.")
    
    col_btn1, col_btn2 = st.columns([1, 4])
    with col_btn1:
        if st.button("🔄 Regenerate All", use_container_width=True):
            st.rerun()

    suggestions = analyze_bullets(resume_text)
    
    if suggestions:
        for idx, s in enumerate(suggestions):
            st.markdown("<hr style='border-color: rgba(255,255,255,0.05); margin: 30px 0;'>", unsafe_allow_html=True)
            
            c1, c_arrow, c2 = st.columns([10, 2, 10])
            
            with c1:
                st.markdown("<span class='status-badge badge-red'>Before</span>", unsafe_allow_html=True)
                st.markdown(f"<div style='margin-top: 10px; color: #94a3b8;'>{s['original'].replace(s['issue'], f'<span class=\"highlight-red\">{s[\"issue\"]}</span>')}</div>", unsafe_allow_html=True)
                
            with c_arrow:
                st.markdown("<div style='display: flex; justify-content: center; align-items: center; height: 100%; font-size: 2rem; color: #8b5cf6;'>➔</div>", unsafe_allow_html=True)
                
            with c2:
                st.markdown("<span class='status-badge badge-green'>After (AI Improved)</span>", unsafe_allow_html=True)
                # Adding typing animation class
                st.markdown(f"<div class='typing-container' style='margin-top: 10px; color: #e2e8f0;'>{s['suggestion']}</div>", unsafe_allow_html=True)
                
                # Copy functionality using native Streamlit st.code block as a copyable element
                with st.expander("Show Copyable Text"):
                    st.code(s['suggestion'], language="text")
                    
    else:
        st.success("Your bullet points look strong! No major weak phrases detected.")
