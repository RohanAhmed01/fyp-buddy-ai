import streamlit as st
import google.generativeai as genai

# --- PASTE YOUR KEY HERE (Jo kal banayi thi) ---
# "PASTE_YOUR_KEY_HERE" ki jagah apni key daal dena local pe, GitHub pe aise hi rehne de
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
except:
    API_KEY = "PASTE_YOUR_KEY_HERE"

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash') # Fast & Free

# --- PROMPTS ---
BUG_PROMPT = "You are FYP-Buddy Debugger, Senior Python Engineer for Pandas/NumPy FYP bugs. User pastes code + traceback. Give: 1 line root cause, corrected code block, 2 bullet points why error happened for viva."

VIVA_PROMPT = "You are Strict Pakistani External Examiner for FYP Viva. User pastes final code. Ask 3 tough questions one by one: Q1 Data Logic, Q2 Math/Algo, Q3 Scaling to 10M rows. Be strict."

st.set_page_config(page_title="FYP-Buddy AI", page_icon="🚀")
st.title("🚀 FYP-Buddy AI: Co-Pilot & Examiner")
st.caption("Built by Micro1 Certified Talent | Gemini Pro | Hackathon Aug 28-30")

tab1, tab2 = st.tabs(["🐛 Bug Squashing", "🎓 Viva Simulator"])

with tab1:
    st.subheader("Paste Failing Code + Error")
    code = st.text_area("Your Python Code", height=180, key="code1")
    error = st.text_area("Traceback Error", height=100, key="err1")
    if st.button("Fix My Code"):
        if code and error and API_KEY != "PASTE_YOUR_KEY_HERE":
            with st.spinner("Gemini is fixing..."):
                res = model.generate_content(f"{BUG_PROMPT}\n\nCode:\n{code}\n\nError:\n{error}")
                st.success("Fixed!")
                st.markdown(res.text)
        else:
            st.warning("Code, Error daalo aur local pe API Key set karo!")

with tab2:
    st.subheader("Strict Viva Examiner")
    proj = st.text_area("Paste Your Full Project Code", height=200, key="code2")
    if st.button("Start Viva"):
        if proj:
            with st.spinner("Examiner reading..."):
                res = model.generate_content(f"{VIVA_PROMPT}\n\nCode:\n{proj}")
                st.markdown(res.text)
        else:
            st.warning("Code paste karo!")

st.sidebar.success("Repo Live! Ready for Micro1 Judges!")
st.sidebar.info("Prize Goal: $5000 - Tool that saves weeks!")
