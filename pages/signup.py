import streamlit as st
from utils.auth import register_user

# Inject custom CSS specifically for cinematic split layout
st.markdown("""
<style>
    /* Full page background styling */
    .stApp {
        background-color: #05050a;
        background-image: 
            linear-gradient(rgba(5, 5, 10, 0.95), rgba(5, 5, 10, 0.95)),
            linear-gradient(90deg, rgba(106, 90, 249, 0.04) 1px, transparent 1px),
            linear-gradient(rgba(106, 90, 249, 0.04) 1px, transparent 1px);
        background-size: 100% 100%, 40px 40px, 40px 40px;
        background-position: center center;
    }
    
    /* Background Elements */
    .bg-elements {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        z-index: 0;
        pointer-events: none;
        overflow: hidden;
    }
    
    /* Gradient Blobs */
    .blob {
        position: absolute;
        filter: blur(90px);
        opacity: 0.5;
        border-radius: 50%;
        animation: floatBlob 20s infinite alternate cubic-bezier(0.4, 0, 0.2, 1);
    }
    .blob-1 { top: -10%; left: -10%; width: 500px; height: 500px; background: radial-gradient(circle, #6a5af9, transparent 70%); animation-delay: 0s; }
    .blob-2 { bottom: -20%; right: -10%; width: 600px; height: 600px; background: radial-gradient(circle, #ff5fd2, transparent 70%); animation-delay: -5s; }
    .blob-3 { top: 40%; left: 40%; width: 400px; height: 400px; background: radial-gradient(circle, #00d4ff, transparent 70%); animation-delay: -10s; }
    .blob-4 { top: 20%; right: 20%; width: 300px; height: 300px; background: radial-gradient(circle, #c084fc, transparent 70%); animation-delay: -15s; }
    
    @keyframes floatBlob {
        0% { transform: translate(0, 0) scale(1); }
        50% { transform: translate(50px, 50px) scale(1.1); }
        100% { transform: translate(-50px, -50px) scale(0.9); }
    }
    
    /* Radial Light Beams */
    .light-beam {
        position: absolute;
        width: 100vw;
        height: 100vh;
        background: radial-gradient(circle at 0% 0%, rgba(106, 90, 249, 0.15) 0%, transparent 40%),
                    radial-gradient(circle at 100% 100%, rgba(0, 212, 255, 0.1) 0%, transparent 40%);
    }

    /* Floating AI Icons */
    .floating-icon {
        position: absolute;
        font-size: 2rem;
        opacity: 0.2;
        filter: drop-shadow(0 0 10px rgba(255,255,255,0.4));
        animation: floatIcon 15s infinite linear;
    }
    .icon-1 { top: 15%; left: 10%; animation-duration: 25s; }
    .icon-2 { top: 70%; left: 25%; font-size: 1.5rem; animation-duration: 20s; animation-direction: reverse; }
    .icon-3 { top: 25%; right: 40%; font-size: 2.5rem; animation-duration: 30s; }
    .icon-4 { top: 80%; right: 15%; font-size: 1.8rem; animation-duration: 22s; }
    
    @keyframes floatIcon {
        0% { transform: translateY(0) rotate(0deg); }
        50% { transform: translateY(-30px) rotate(180deg); }
        100% { transform: translateY(0) rotate(360deg); }
    }

    /* Moving particles (simplified using box-shadow) */
    .particles {
        position: absolute;
        width: 3px;
        height: 3px;
        background: #00d4ff;
        border-radius: 50%;
        box-shadow: 
            100px 200px #c084fc, 300px 400px #6a5af9, 500px 100px #ff5fd2, 700px 600px #00d4ff,
            900px 300px #c084fc, 1100px 800px #6a5af9, 200px 900px #ff5fd2, 400px 700px #00d4ff,
            600px 500px #c084fc, 800px 200px #6a5af9, 1000px 100px #ff5fd2, 1200px 400px #00d4ff,
            150px 350px #c084fc, 450px 750px #6a5af9, 850px 250px #ff5fd2, 1150px 550px #00d4ff;
        animation: particleMove 40s infinite linear;
        opacity: 0.6;
    }
    @keyframes particleMove {
        from { transform: translateY(100vh); }
        to { transform: translateY(-100vh); }
    }
    
    /* Cyber lines connecting dots (simulation) */
    .cyber-lines {
        position: absolute;
        width: 100vw;
        height: 100vh;
        background-image: 
            linear-gradient(45deg, transparent 48%, rgba(106, 90, 249, 0.05) 49%, rgba(106, 90, 249, 0.05) 51%, transparent 52%),
            linear-gradient(-45deg, transparent 48%, rgba(0, 212, 255, 0.05) 49%, rgba(0, 212, 255, 0.05) 51%, transparent 52%);
        background-size: 150px 150px;
        opacity: 0.4;
    }

    /* Content Layout */
    .content-wrapper {
        position: relative;
        z-index: 10;
    }
    
    .ai-hero-section {
        padding: 40px 20px;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        animation: fadeIn 1.5s ease-out;
        position: relative;
        z-index: 10;
    }
    @keyframes fadeIn { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }

    .typing-headline {
        font-size: 3.2rem;
        font-weight: 800;
        background: -webkit-linear-gradient(45deg, #00d4ff, #6a5af9, #c084fc, #ff5fd2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 20px;
        line-height: 1.2;
        overflow: hidden;
        border-right: .15em solid #c084fc;
        white-space: nowrap;
        margin: 0 auto;
        letter-spacing: .05em;
        animation: typingLogin 3.5s steps(40, end), blink-caret .75s step-end infinite;
    }
    @keyframes typingLogin { from { width: 0 } to { width: 100% } }
    @keyframes blink-caret { from, to { border-color: transparent } 50% { border-color: #c084fc } }
    
    .pulsing-icon-container {
        position: relative;
        width: 120px;
        height: 120px;
        margin: 20px 0 40px 0;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .pulse-ring {
        content: '';
        position: absolute;
        width: 100%;
        height: 100%;
        border-radius: 50%;
        border: 2px solid rgba(106, 90, 249, 0.6);
        animation: pulsing 2s infinite cubic-bezier(0.215, 0.61, 0.355, 1);
        box-shadow: 0 0 20px rgba(106, 90, 249, 0.4), inset 0 0 20px rgba(106, 90, 249, 0.4);
    }
    @keyframes pulsing {
        0% { transform: scale(0.8); opacity: 1; box-shadow: 0 0 0 0 rgba(106, 90, 249, 0.7); }
        100% { transform: scale(1.8); opacity: 0; box-shadow: 0 0 0 30px rgba(106, 90, 249, 0); }
    }
    

    
    /* Right column auth block */
    @keyframes floatAuth {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }
    
    /* Styling the Streamlit container to look like a glass card */
    [data-testid="stVerticalBlockBorderWrapper"] > div {
        background: rgba(15, 23, 42, 0.4) !important;
        backdrop-filter: blur(20px) !important;
        -webkit-backdrop-filter: blur(20px) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 24px !important;
        box-shadow: 0 20px 50px rgba(0,0,0,0.3), 0 0 20px rgba(106, 90, 249, 0.1) !important;
        transition: all 0.3s ease !important;
        position: relative;
        overflow: hidden;
        animation: floatAuth 6s ease-in-out infinite;
        margin-top: 5vh;
    }
    [data-testid="stVerticalBlockBorderWrapper"] > div::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: radial-gradient(circle at 50% 0%, rgba(106, 90, 249, 0.15) 0%, transparent 70%);
        pointer-events: none;
    }
    [data-testid="stVerticalBlockBorderWrapper"] > div:hover {
        box-shadow: 0 20px 50px rgba(0,0,0,0.4), 0 0 30px rgba(0, 212, 255, 0.2) !important;
        border-color: rgba(255, 255, 255, 0.2) !important;
    }
    
    /* Login button styling */
    button[data-testid="baseButton-primary"] {
        background: linear-gradient(45deg, #6a5af9, #c084fc, #ff5fd2) !important;
        border: none !important;
        box-shadow: 0 4px 15px rgba(106, 90, 249, 0.4) !important;
        transition: all 0.3s ease !important;
        font-weight: 600 !important;
        letter-spacing: 1px !important;
    }
    button[data-testid="baseButton-primary"]:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(255, 95, 210, 0.6) !important;
        background: linear-gradient(45deg, #ff5fd2, #c084fc, #6a5af9) !important;
    }
</style>

<!-- Background Elements Injection -->
<div class="bg-elements">
    <div class="cyber-lines"></div>
    <div class="light-beam"></div>
    <div class="blob blob-1"></div>
    <div class="blob blob-2"></div>
    <div class="blob blob-3"></div>
    <div class="blob blob-4"></div>
    <div class="particles"></div>
    <div class="floating-icon icon-1">⚡</div>
    <div class="floating-icon icon-2">✨</div>
    <div class="floating-icon icon-3">📈</div>
    <div class="floating-icon icon-4">🚀</div>
</div>
""", unsafe_allow_html=True)

# Split screen layout cleanly centered
col_left, col_spacer, col_right = st.columns([1, 0.2, 1])

with col_left:
    st.markdown("""
<div class="ai-hero-section" style="align-items: center; text-align: center;">
<div class="pulsing-icon-container" style="margin: 0 auto 30px auto;">
<div class="pulse-ring"></div>
<div style="font-size: 4.5rem; filter: drop-shadow(0 0 20px rgba(168,85,247,0.8)); z-index: 2;">🧠</div>
</div>
<h1 class="typing-headline" style="text-align: center;">AI Resume Matcher PRO</h1>
<p style="color: #94a3b8; font-size: 1.2rem; letter-spacing: 1px; margin-top: -10px;">Smart AI-powered resume intelligence platform</p>
</div>
""", unsafe_allow_html=True)

with col_right:
    with st.container(border=True):
        st.markdown("""
<div class="fade-in" style="text-align: center; margin-bottom: 20px; padding-top: 10px;">
<h2 class="auth-title" style="font-size: 2.2rem; background: -webkit-linear-gradient(45deg, #00d4ff, #c084fc); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 5px;">Create Account</h2>
<p style="color: #94a3b8; letter-spacing: 1px; margin-top: 0;">Initialize your intelligence profile</p>
</div>
""", unsafe_allow_html=True)
        
        name = st.text_input("👤 Full Name")
        email = st.text_input("📧 Email Address")
        password = st.text_input("🔒 Password", type="password")
        confirm_password = st.text_input("🔒 Confirm Password", type="password")
        st.markdown("<div style='padding: 10px;'></div>", unsafe_allow_html=True)
        
        if st.button("🚀 Initialize Profile", type="primary", use_container_width=True):
            if password != confirm_password:
                st.error("Passwords do not match.")
            elif not name or not email or not password:
                st.error("Please fill in all fields.")
            else:
                if register_user(name, email, password):
                    st.success("Neural link established! You can now log in.")
                else:
                    st.error("Email already exists in the matrix. Please log in.")
