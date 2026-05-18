import streamlit as st

def inject_custom_css():
    st.markdown("""
    <style>
        /* Modern Premium Dark Theme & Glassmorphism */
        
        /* App Background with premium layered effects */
        @keyframes float1 {
            0% { transform: translate(0, 0) scale(1); }
            33% { transform: translate(5vw, -5vh) scale(1.1); }
            66% { transform: translate(-3vw, 3vh) scale(0.9); }
            100% { transform: translate(0, 0) scale(1); }
        }
        @keyframes float2 {
            0% { transform: translate(0, 0) scale(1); }
            33% { transform: translate(-5vw, 5vh) scale(1.2); }
            66% { transform: translate(3vw, -3vh) scale(0.8); }
            100% { transform: translate(0, 0) scale(1); }
        }
        @keyframes gridMove {
            0% { background-position: 0 0, 0 0, 0 0, 0 0; }
            100% { background-position: 0 0, -40px -40px, 40px 40px, 40px 40px; }
        }
        
        .stApp {
            background-color: #030514; /* Deep navy base */
            /* Layered Background: 
               1. Center radial light
               2. Low-opacity glowing dots
               3. Subtle moving grid (vertical)
               4. Subtle moving grid (horizontal)
            */
            background-image: 
                radial-gradient(circle at 50% 50%, rgba(139, 92, 246, 0.08) 0%, transparent 60%),
                radial-gradient(rgba(255, 255, 255, 0.1) 1px, transparent 1px),
                linear-gradient(rgba(255, 255, 255, 0.02) 1px, transparent 1px),
                linear-gradient(90deg, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
            background-size: 100% 100%, 40px 40px, 40px 40px, 40px 40px;
            animation: gridMove 30s linear infinite;
            color: #e2e8f0;
            font-family: 'Inter', sans-serif;
            position: relative;
            z-index: 0;
        }

        /* Ensure main content stays above background effects */
        [data-testid="stAppViewContainer"], .stApp > header {
            z-index: 10 !important;
            position: relative;
            background: transparent !important;
        }

        /* Top-left purple glow & Bottom-right blue glow */
        .stApp::before, .stApp::after {
            content: '';
            position: fixed;
            border-radius: 50%;
            z-index: -1;
            filter: blur(120px);
            pointer-events: none;
        }
        
        .stApp::before {
            width: 50vw;
            height: 50vw;
            background: radial-gradient(circle, rgba(147, 51, 234, 0.3) 0%, rgba(236, 72, 153, 0.1) 50%, transparent 70%);
            top: -20vh;
            left: -20vw;
            animation: float1 20s infinite ease-in-out;
        }
        
        .stApp::after {
            width: 60vw;
            height: 60vw;
            background: radial-gradient(circle, rgba(59, 130, 246, 0.25) 0%, rgba(147, 51, 234, 0.1) 50%, transparent 70%);
            bottom: -20vh;
            right: -20vw;
            animation: float2 25s infinite ease-in-out;
        }
        
        /* Extra decorative light streak */
        [data-testid="stAppViewContainer"]::before {
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0; height: 1px;
            background: linear-gradient(90deg, transparent, rgba(168, 85, 247, 0.5), transparent);
            z-index: 11;
            opacity: 0.6;
        }

        /* Sidebar Styling */
        [data-testid="stSidebar"] {
            background: rgba(10, 15, 30, 0.6) !important;
            backdrop-filter: blur(20px) !important;
            -webkit-backdrop-filter: blur(20px) !important;
            border-right: 1px solid rgba(255,255,255,0.05);
        }

        /* Sidebar links */
        [data-testid="stSidebarNav"] ul li a{
            height:58px!important;
            min-height:58px!important;
            padding:0 22px!important;
        
            display:flex!important;
            align-items:center!important;
        
            border-radius:18px!important;
            margin:10px 0!important;
        
            background:
            linear-gradient(
            90deg,
            rgba(40,50,90,.90),
            rgba(60,40,90,.90)
            )!important;
        
            border:1px solid rgba(180,180,255,.15)!important;
            
            box-shadow:
            0 0 12px rgba(100,100,255,.18)!important;
        
            backdrop-filter:blur(12px)!important;
            color:white!important;
        
            transition:all .3s ease!important;
        
            overflow:hidden!important;
            position: relative !important;
        }
        
        /* Hover */
        [data-testid="stSidebarNav"] ul li a:hover{
            transform:translateX(4px)!important;
        
            box-shadow:
            0 0 18px rgba(160,100,255,.35)!important;
        }
        
        /* Active page */
        [data-testid="stSidebarNav"] ul li a[aria-current="page"]{
            background:
            linear-gradient(
            90deg,
            rgba(40,50,90,.90),
            rgba(60,40,90,.90)
            )!important;
        
            border:1px solid rgba(210,170,255,.45)!important;
        
            box-shadow:
            0 0 28px rgba(192,132,252,.65)!important;
        }
        
        /* text */
        [data-testid="stSidebarNav"] span{
            font-size:18px!important;
            font-weight:700!important;
        }
        
        /* Hide native Streamlit indicator */
        [data-testid="stSidebarNav"] li div {
            background: transparent !important;
        }
        
        /* Icons on the right */
        a[data-testid="stSidebarNavLink"][href*="login"]::after {
            content: '🔐';
            position: absolute;
            right: 20px;
            top: 50%;
            transform: translateY(-50%);
            font-size: 1.2rem;
            filter: drop-shadow(0 0 5px rgba(0, 212, 255, 0.6));
        }
        a[data-testid="stSidebarNavLink"][href*="signup"]::after {
            content: '✨';
            position: absolute;
            right: 20px;
            top: 50%;
            transform: translateY(-50%);
            font-size: 1.2rem;
            filter: drop-shadow(0 0 5px rgba(255, 95, 210, 0.6));
        }

        /* Glassmorphism for containers/cards */
        [data-testid="stVerticalBlockBorderWrapper"] {
            background: rgba(20, 25, 40, 0.5) !important;
            backdrop-filter: blur(20px) !important;
            -webkit-backdrop-filter: blur(20px) !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            border-radius: 20px !important;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3) !important;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
            position: relative;
            z-index: 10;
        }
        
        /* Auth Card specific styling */
        .auth-container {
            max-width: 450px !important;
            margin: 0 auto !important;
            padding-top: 5vh;
        }
        
        [data-testid="stVerticalBlockBorderWrapper"]:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 45px 0 rgba(124, 58, 237, 0.2) !important;
            border-color: rgba(124, 58, 237, 0.4) !important;
        }

        /* Glowing Gradient Buttons */
        div.stButton > button {
            background: linear-gradient(135deg, #4f46e5 0%, #9333ea 100%) !important;
            color: white !important;
            border: none !important;
            border-radius: 12px !important;
            padding: 0.6rem 1.5rem !important;
            font-weight: 600 !important;
            letter-spacing: 0.5px !important;
            box-shadow: 0 4px 15px rgba(147, 51, 234, 0.3) !important;
            transition: all 0.3s ease !important;
            position: relative;
            overflow: hidden;
        }
        
        div.stButton > button::after {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255,255,255,0.2) 0%, transparent 60%);
            opacity: 0;
            transition: opacity 0.3s;
        }
        
        div.stButton > button:hover::after {
            opacity: 1;
        }
        
        div.stButton > button:hover {
            transform: scale(1.05) !important;
            box-shadow: 0 8px 25px rgba(147, 51, 234, 0.6) !important;
        }

        /* Metrics */
        [data-testid="stMetric"] {
            background: rgba(20, 25, 40, 0.5);
            backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.05);
            padding: 20px;
            border-radius: 16px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.15);
            text-align: center;
            transition: transform 0.3s ease;
        }
        [data-testid="stMetric"]:hover {
            transform: translateY(-3px);
            border-color: rgba(147, 51, 234, 0.3);
        }
        [data-testid="stMetricValue"] {
            font-size: 2.5rem !important;
            background: -webkit-linear-gradient(45deg, #60a5fa, #c084fc, #f472b6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 800;
        }

        /* Inputs */
        .stTextArea textarea, .stTextInput input {
            background: rgba(10, 15, 30, 0.6) !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            color: #f8fafc !important;
            border-radius: 10px !important;
            padding: 12px 16px !important;
            transition: all 0.3s ease !important;
            box-shadow: inset 0 2px 4px rgba(0,0,0,0.1);
        }
        .stTextArea textarea:focus, .stTextInput input:focus {
            border-color: #a855f7 !important;
            box-shadow: 0 0 15px rgba(168, 85, 247, 0.4), inset 0 2px 4px rgba(0,0,0,0.1) !important;
            background: rgba(15, 20, 40, 0.8) !important;
        }

        /* Tabs */
        [data-testid="stTabs"] button {
            background: transparent !important;
            border: none !important;
            color: #64748b !important;
            font-size: 1.1rem !important;
            font-weight: 500 !important;
            transition: all 0.3s ease !important;
        }
        [data-testid="stTabs"] button[aria-selected="true"] {
            color: #c084fc !important;
            border-bottom: 2px solid #c084fc !important;
            text-shadow: 0 0 15px rgba(192, 132, 252, 0.5) !important;
        }
        
        /* Expanders */
        [data-testid="stExpander"] {
            background: rgba(20, 25, 40, 0.5) !important;
            border: 1px solid rgba(255, 255, 255, 0.05) !important;
            border-radius: 12px !important;
            margin-bottom: 15px;
            backdrop-filter: blur(10px);
        }
        
        /* Progress bars */
        .stProgress > div > div > div > div {
            background-image: linear-gradient(90deg, #3b82f6, #8b5cf6, #ec4899) !important;
            background-size: 200% 200%;
            animation: gradientMove 3s ease infinite;
        }
        @keyframes gradientMove {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        /* Typography & Custom Elements */
        @keyframes glowText {
            0% { text-shadow: 0 0 10px rgba(139, 92, 246, 0.5), 0 0 20px rgba(139, 92, 246, 0.3); }
            50% { text-shadow: 0 0 20px rgba(236, 72, 153, 0.7), 0 0 30px rgba(236, 72, 153, 0.5); }
            100% { text-shadow: 0 0 10px rgba(139, 92, 246, 0.5), 0 0 20px rgba(139, 92, 246, 0.3); }
        }
        .hero-title, .auth-title {
            font-size: 3.5rem;
            font-weight: 800;
            background: -webkit-linear-gradient(45deg, #60a5fa, #c084fc, #f472b6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
            margin-bottom: 0px;
            animation: glowText 4s infinite;
        }
        .auth-title {
            font-size: 2.2rem;
            line-height: 1.2;
        }
        .hero-subtitle, .auth-subtitle {
            font-size: 1.2rem;
            color: #94a3b8;
            text-align: center;
            margin-top: 10px;
            margin-bottom: 30px;
            letter-spacing: 1px;
        }
        .auth-subtitle {
            font-size: 1rem;
            margin-bottom: 20px;
        }
        
        .ai-avatar {
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 3rem;
            margin-bottom: 10px;
            filter: drop-shadow(0 0 15px rgba(168, 85, 247, 0.6));
        }

        /* Fix dividers */
        hr {
            border-color: rgba(255,255,255,0.08) !important;
            margin: 2rem 0 !important;
        }
        
        /* Fade in animation */
        .fade-in {
            animation: fadeIn 0.8s ease-out forwards;
        }
        @keyframes fadeIn {
            0% { opacity: 0; transform: translateY(20px); }
            100% { opacity: 1; transform: translateY(0); }
        }
        /* Skill Chips */
        .skill-chip {
            display: inline-block;
            padding: 5px 12px;
            margin: 4px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 600;
            background: rgba(30, 41, 59, 0.6);
            border: 1px solid rgba(255, 255, 255, 0.1);
            transition: all 0.3s ease;
            cursor: default;
        }
        .skill-chip:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 10px rgba(124, 58, 237, 0.4);
            border-color: rgba(124, 58, 237, 0.6);
        }
        .skill-chip.missing {
            border-color: rgba(244, 63, 94, 0.5);
            color: #fda4af;
        }
        .skill-chip.missing:hover {
            box-shadow: 0 4px 10px rgba(244, 63, 94, 0.4);
            border-color: #f43f5e;
        }
        .skill-chip.matched {
            border-color: rgba(34, 197, 94, 0.5);
            color: #86efac;
        }
        .skill-chip.matched:hover {
            box-shadow: 0 4px 10px rgba(34, 197, 94, 0.4);
            border-color: #22c55e;
        }
        .skill-chip.recommended {
            border-color: rgba(234, 179, 8, 0.5);
            color: #fde047;
        }
        
        /* Badges */
        .status-badge {
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 0.75rem;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 1px;
            display: inline-block;
        }
        .badge-red { background: rgba(244, 63, 94, 0.2); color: #f43f5e; border: 1px solid rgba(244, 63, 94, 0.5); }
        .badge-green { background: rgba(34, 197, 94, 0.2); color: #22c55e; border: 1px solid rgba(34, 197, 94, 0.5); }
        
        /* Timeline specific */
        .timeline-container {
            position: relative;
            padding-left: 30px;
            margin-bottom: 20px;
        }
        .timeline-line {
            position: absolute;
            left: 11px;
            top: 0;
            bottom: 0;
            width: 2px;
            background: linear-gradient(to bottom, #8b5cf6, rgba(139, 92, 246, 0.1));
        }
        .timeline-node {
            position: absolute;
            left: 0;
            top: 0;
            width: 24px;
            height: 24px;
            border-radius: 50%;
            background: #0f172a;
            border: 2px solid #8b5cf6;
            box-shadow: 0 0 10px #8b5cf6;
            z-index: 2;
        }
        .timeline-content {
            background: rgba(30, 41, 59, 0.5);
            border: 1px solid rgba(255, 255, 255, 0.1);
            padding: 15px;
            border-radius: 12px;
            margin-bottom: 25px;
            transition: all 0.3s ease;
        }
        .timeline-content:hover {
            transform: translateX(5px);
            border-color: #8b5cf6;
            box-shadow: -5px 5px 15px rgba(139, 92, 246, 0.2);
        }
        
        /* Typing animation */
        .typing-container {
            border-right: 2px solid #22c55e;
            white-space: pre-wrap;
            overflow: hidden;
            animation: typing 3s steps(40, end), blink-caret .75s step-end infinite;
        }
        @keyframes typing { from { max-height: 0; opacity: 0; } to { max-height: 1000px; opacity: 1; } }
        @keyframes blink-caret { from, to { border-color: transparent } 50% { border-color: #22c55e; } }
        
        /* Highlight words */
        .highlight-green {
            background: rgba(34, 197, 94, 0.2);
            color: #4ade80;
            padding: 0 4px;
            border-radius: 4px;
            border-bottom: 1px solid #22c55e;
            font-weight: 600;
        }
        .highlight-red {
            text-decoration: line-through;
            color: #f87171;
            opacity: 0.8;
        }
    </style>
    """, unsafe_allow_html=True)

def render_hero():
    st.markdown('''
        <div class="fade-in" style="text-align: center; padding: 30px 0px 40px 0px;">
            <div class="ai-avatar">✨</div>
            <h1 class="hero-title">AI Resume Matcher PRO</h1>
            <p class="hero-subtitle">Smart AI-powered resume intelligence platform</p>
        </div>
    ''', unsafe_allow_html=True)
    
def render_auth_header(title="Welcome to AI Resume Matcher PRO"):
    st.markdown(f'''
        <div class="fade-in" style="text-align: center;">
            <div class="ai-avatar">🧠</div>
            <h2 class="auth-title">{title}</h2>
            <p class="auth-subtitle">Smart Resume Intelligence Platform</p>
        </div>
    ''', unsafe_allow_html=True)
