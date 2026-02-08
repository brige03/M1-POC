import streamlit as st
import time
import google.generativeai as genai
import base64

# --- 1. THE CORE CONFIGURATION (HIDDEN WIRES) ---
st.set_page_config(layout="wide", page_title="M1: I AM ONE", page_icon="💠")

# SECURITY PROTOCOL: KEY INJECTED
API_KEY = "AIzaSyDULsrvSE7TkVJfE1Wya2mncp_dnVEcV9A" 

# --- 2. THE AUDIO ENGINE (THE CHIME) ---
def play_chime():
    # Base64 encoded 'glass ping' sound for instant feedback
    audio_code = """
    <audio autoplay>
    <source src="data:audio/wav;base64,UklGRl9vT19XQVZFZm10IBAAAAABAAEAQB8AAEAfAAABAAgAZGF0YUvvT18AAAAAAP//AAAAAAAA//8AAAAAAAAAAAAA//8AAAAA//8AAAAAAAAAAAAA//8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" type="audio/wav">
    </audio>
    <script>
    var audio = new Audio('https://cdn.freesound.org/previews/336/336899_4939229-lq.mp3');
    audio.volume = 0.5;
    audio.play();
    </script>
    """
    st.components.v1.html(audio_code, height=0, width=0)

# --- 3. THE AVATAR X APPLE DESIGN SYSTEM (CSS) ---
def inject_avatar_css(crystal_mode):
    # The M1 Color Palettes (Extracted from your Brand Deck)
    palettes = {
        "Lapis":    {"bg": "#020b1c", "accent": "#2E86C1", "glow": "0 0 20px #2E86C1"}, # Deep Blue
        "Emerald":  {"bg": "#051405", "accent": "#27AE60", "glow": "0 0 20px #27AE60"}, # Nature Green
        "Citrine":  {"bg": "#141002", "accent": "#F1C40F", "glow": "0 0 20px #F1C40F"}, # Wealth Gold
        "Ruby":     {"bg": "#140202", "accent": "#C0392B", "glow": "0 0 20px #C0392B"}, # Vital Red
        "Quartz":   {"bg": "#0a0a0a", "accent": "#ECF0F1", "glow": "0 0 20px #FFFFFF"}, # Pure White
    }
    theme = palettes.get(crystal_mode, palettes["Lapis"])

    st.markdown(f"""
    <style>
        /* GLOBAL RESET - APPLE ERGONOMICS */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@200;400;600&display=swap');
        
        .stApp {{
            background-color: {theme['bg']};
            background-image: 
                radial-gradient(circle at 50% 50%, rgba(255,255,255,0.03) 0%, transparent 50%),
                radial-gradient(circle at 80% 20%, {theme['accent']}22 0%, transparent 30%);
            font-family: 'Inter', sans-serif;
            color: #ffffff;
            transition: background 1s ease;
        }}
        
        /* THE 3D CRYSTAL MATRIX */
        .crystal-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
            gap: 20px;
            padding: 20px;
        }}
        .crystal-card {{
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 20px;
            text-align: center;
            cursor: pointer;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            backdrop-filter: blur(10px);
        }}
        .crystal-card:hover {{
            transform: translateY(-10px) scale(1.05);
            box-shadow: {theme['glow']};
            border-color: {theme['accent']};
            background: rgba(255, 255, 255, 0.1);
        }}
        .crystal-icon {{
            font-size: 40px;
            display: block;
            margin-bottom: 10px;
            animation: spin 10s linear infinite;
        }}
        
        /* UI ELEMENTS */
        .stButton>button {{
            background: linear-gradient(135deg, {theme['accent']}44, {theme['accent']}11);
            color: white;
            border: 1px solid {theme['accent']};
            border-radius: 50px; /* Apple Roundness */
            padding: 10px 30px;
            font-weight: 500;
            transition: all 0.3s ease;
            width: 100%;
        }}
        .stButton>button:hover {{
            background: {theme['accent']};
            box-shadow: {theme['glow']};
            transform: scale(1.02);
        }}
        
        /* TEXT INPUTS */
        .stTextInput input {{
            background: rgba(0,0,0,0.3) !important;
            border: 1px solid rgba(255,255,255,0.2) !important;
            border-radius: 15px !important;
            color: white !important;
            padding: 15px !important;
        }}
        
        /* LOGO ANIMATION */
        @keyframes spin {{ 
            0% {{ transform: rotateY(0deg); }} 
            100% {{ transform: rotateY(360deg); }} 
        }}
    </style>
    """, unsafe_allow_html=True)

# --- 4. STATE MANAGEMENT ---
if 'setup_done' not in st.session_state: st.session_state.setup_done = False
if 'vibe' not in st.session_state: st.session_state.vibe = "Lapis"
if 'history' not in st.session_state: st.session_state.history = []

# --- 5. SCREEN 1: THE PORTAL (ONBOARDING) ---
def screen_onboarding():
    inject_avatar_css("Lapis") # Default dark blue start
    
    st.markdown("""
        <div style="text-align: center; margin-top: 50px; margin-bottom: 50px;">
            <h1 style="font-weight: 200; letter-spacing: 5px; text-transform: uppercase; font-size: 3em; text-shadow: 0 0 20px #2E86C1;">
                M1
            </h1>
            <p style="color: #888; letter-spacing: 2px;">I AM ONE.</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("### Pick Your Energy Stone")
    st.markdown("Select the one that calls to you. It will tune the interface to your frequency.")

    # THE 3D MATRIX GRID
    # We use columns to simulate the clickable grid since Streamlit buttons are limited.
    c1, c2, c3, c4, c5 = st.columns(5)
    
    with c1:
        st.markdown("<div class='crystal-card'><div class='crystal-icon'>🔵</div></div>", unsafe_allow_html=True)
        if st.button("Select Blue"):
            st.session_state.vibe = "Lapis"
            play_chime()
            st.session_state.setup_done = True
            st.rerun()
            
    with c2:
        st.markdown("<div class='crystal-card'><div class='crystal-icon'>🟢</div></div>", unsafe_allow_html=True)
        if st.button("Select Green"):
            st.session_state.vibe = "Emerald"
            play_chime()
            st.session_state.setup_done = True
            st.rerun()

    with c3:
        st.markdown("<div class='crystal-card'><div class='crystal-icon'>🟡</div></div>", unsafe_allow_html=True)
        if st.button("Select Gold"):
            st.session_state.vibe = "Citrine"
            play_chime()
            st.session_state.setup_done = True
            st.rerun()

    with c4:
        st.markdown("<div class='crystal-card'><div class='crystal-icon'>🔴</div></div>", unsafe_allow_html=True)
        if st.button("Select Red"):
            st.session_state.vibe = "Ruby"
            play_chime()
            st.session_state.setup_done = True
            st.rerun()

    with c5:
        st.markdown("<div class='crystal-card'><div class='crystal-icon'>⚪</div></div>", unsafe_allow_html=True)
        if st.button("Select White"):
            st.session_state.vibe = "Quartz"
            play_chime()
            st.session_state.setup_done = True
            st.rerun()

# --- 6. SCREEN 2: THE M1 CORE (MAIN APP) ---
def screen_app():
    inject_avatar_css(st.session_state.vibe)
    
    # Header
    c_logo, c_title = st.columns([1,10])
    with c_logo:
        # Mini 3D Logo
        st.markdown(f"<div style='font-size:40px; text-align:center;'>💠</div>", unsafe_allow_html=True)
    with c_title:
        st.markdown(f"**M1 INTELLIGENT SYSTEM** | MODE: {st.session_state.vibe.upper()}")

    st.divider()

    # Layout: Navigator (Left) vs Chat (Right)
    col_nav, col_chat = st.columns([1, 2])

    with col_nav:
        st.markdown("### 🧭 Your Compass")
        st.info("System Status: **ONLINE**")
        st.write("The system is listening to your patterns, not just your words.")
        
        st.markdown("---")
        st.markdown("**3-Day Journey**")
        st.caption("1. Chill Mode (Body)")
        st.caption("2. Pattern Decoder (Mind)")
        st.caption("3. Good Deeds (Soul)")
        
        st.markdown("---")
        if st.button("Change My Stone"):
            st.session_state.setup_done = False
            st.rerun()

    with col_chat:
        # Chat History Display
        for msg in st.session_state.history:
            role_icon = "👤" if msg["role"] == "user" else "💠"
            bg_color = "rgba(255,255,255,0.05)" if msg["role"] == "user" else "rgba(0,0,0,0.3)"
            st.markdown(f"""
            <div style='background:{bg_color}; padding:15px; border-radius:15px; margin-bottom:10px; border:1px solid rgba(255,255,255,0.1);'>
                <strong>{role_icon}</strong> {msg['content']}
            </div>
            """, unsafe_allow_html=True)

        # Input Area
        prompt = st.text_input("Talk to M1...", placeholder="I saw something weird today...")
        
        if st.button("Send Signal"):
            if prompt:
                # 1. User Message
                st.session_state.history.append({"role": "user", "content": prompt})
                play_chime() # Audio Feedback
                
                # 2. AI Logic (Gemini)
                try:
                    genai.configure(api_key=API_KEY)
                    model = genai.GenerativeModel('gemini-1.5-pro', system_instruction="""
                        You are M1. You are a digital friend, not a robot.
                        Speak simply. No big words.
                        Your goal: Help the user find clarity.
                        If they mention stress, tell them to breathe (Chill Mode).
                        If they mention seeing things, tell them what it means (Pattern Decoder).
                        Be warm, cool, and brief.
                    """)
                    
                    with st.spinner("Connecting to the Field..."):
                        response = model.generate_content(prompt)
                        reply = response.text
                        
                    st.session_state.history.append({"role": "ai", "content": reply})
                    st.rerun()
                    
                except Exception as e:
                    st.error(f"Signal Blocked: {e}")

# --- 7. MAIN EXECUTION LOOP ---
if not st.session_state.setup_done:
    screen_onboarding()
else:
    screen_app()
