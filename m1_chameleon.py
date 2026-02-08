import streamlit as st
import time
import random
import google.generativeai as genai

# --- 1. THE CHAMELEON KERNEL (CSS/JS INJECTION) ---
st.set_page_config(layout="wide", page_title="M1 CHAMELEON", page_icon="💠")

def inject_chameleon_css(crystal_color):
    colors = {
        "Amethyst": ("#0f0518", "#a55eea", "#dcdde1"),
        "Obsidian": ("#000000", "#ffffff", "#2f3640"),
        "Quartz":   ("#f5f6fa", "#2f3640", "#7f8fa6"),
        "Gold":     ("#1e1e1e", "#f1c40f", "#f39c12"),
        "Neon":     ("#050505", "#00ff00", "#ff00ff")
    }
    bg, prime, sec = colors.get(crystal_color, colors["Obsidian"])
    
    css = f"""
    <style>
        .stApp {{
            background-color: {bg};
            background-image: radial-gradient({sec} 1px, transparent 1px), radial-gradient({sec} 1px, transparent 1px);
            background-size: 50px 50px;
            color: {prime};
            transition: all 0.8s cubic-bezier(0.2, 0.8, 0.2, 1);
        }}
        .m1-logo {{
            width: 100px; height: 100px; border-radius: 50%;
            background: linear-gradient(145deg, {prime}, {sec});
            margin: 0 auto; animation: pulse-quantum 2s infinite;
            display: flex; align_items: center; justify_content: center;
            font-size: 24px; font-weight: bold; color: {bg};
            box-shadow: 0 20px 50px rgba(0,0,0,0.5);
        }}
        @keyframes pulse-quantum {{
            0% {{ box-shadow: 0 0 0 0px rgba({int(prime[1:3],16)}, {int(prime[3:5],16)}, {int(prime[5:],16)}, 0.7); }}
            70% {{ box-shadow: 0 0 0 20px rgba({int(prime[1:3],16)}, {int(prime[3:5],16)}, {int(prime[5:],16)}, 0); }}
            100% {{ box-shadow: 0 0 0 0px rgba({int(prime[1:3],16)}, {int(prime[3:5],16)}, {int(prime[5:],16)}, 0); }}
        }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# --- 2. STATE VECTOR NAVIGATION ---
if 'onboarding_complete' not in st.session_state: st.session_state.onboarding_complete = False
if 'user_crystal' not in st.session_state: st.session_state.user_crystal = "Obsidian"
if 'gemini_history' not in st.session_state: st.session_state.gemini_history = []

# --- 3. ON-BOARDING ---
def run_onboarding():
    st.markdown("""<div style="text-align: center; padding: 50px;"><div class="m1-logo">M1</div><h1>SYSTEM INITIALIZATION</h1><p>CALIBRATING SENSORY PREFERENCES...</p></div>""", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1])
    with col1:
        crystal = st.select_slider("Select Resonance Frequency:", options=["Amethyst", "Obsidian", "Quartz", "Gold", "Neon"], value=st.session_state.user_crystal)
        st.session_state.user_crystal = crystal
        inject_chameleon_css(crystal)
    with col2:
        if st.button("▶ PLAY TEST TONE (0.1 Hz)"): st.success("Audio Resonance: MATCHED (Alpha State)")
        st.radio("Which horizon calls to you?", ["The Mountain", "The Ocean", "The Stars"])
    
    if st.button("ACTIVATE M1 INTERFACE"):
        st.session_state.onboarding_complete = True
        st.rerun()

# --- 4. M1 APP ---
def run_app():
    inject_chameleon_css(st.session_state.user_crystal)
    st.markdown(f"""<div style="display:flex; justify-content:space-between; align-items:center;"><div class="m1-logo" style="width:50px; height:50px; font-size:12px;">M1</div><h3>MODE: {st.session_state.user_crystal.upper()} // V19.0</h3></div>""", unsafe_allow_html=True)
    st.divider()
    col_nav, col_main = st.columns([1, 3])
    with col_nav:
        st.info("State Vector: STABLE")
        if st.button("RESET UI"):
            st.session_state.onboarding_complete = False
            st.rerun()
    with col_main:
        api_key = st.text_input("ENTER GEMINI API KEY:", type="password")
        for msg in st.session_state.gemini_history:
            with st.chat_message(msg["role"]): st.write(msg["content"])
        user_input = st.chat_input("State your intent...")
        if user_input and api_key:
            st.session_state.gemini_history.append({"role": "user", "content": user_input})
            with st.chat_message("user"): st.write(user_input)
            try:
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel('gemini-1.5-pro', system_instruction="You are M1, a Quantum Resonance Engine. Guide the user to their Destiny Vector.")
                with st.spinner("Collapsing Wave Function..."):
                    response = model.generate_content(user_input)
                    st.session_state.gemini_history.append({"role": "assistant", "content": response.text})
                    with st.chat_message("assistant"): st.write(response.text)
            except Exception as e: st.error(f"Quantum Entanglement Failed: {e}")

if not st.session_state.onboarding_complete: run_onboarding()
else: run_app()
