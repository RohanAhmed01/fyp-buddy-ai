import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="FYP Buddy v2", page_icon="🤖", layout="centered")

st.title("🤖 FYP Buddy v2.0")
st.caption("AI Code Debugger for FYP Students - Final Version")

# API Key
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

# UI
code_input = st.text_area("📋 Apna Code Yahan Paste Karo:", height=200, placeholder="def add(a,b)\n    return a + b")
error_input = st.text_area("❌ Error (Agar ho to):", height=100, placeholder="SyntaxError: expected ':'")

col1, col2 = st.columns(2)
with col1:
    fix_btn = st.button("🚀 Fix My Code", use_container_width=True)
with col2:
    explain_btn = st.button("📖 Explain in Urdu", use_container_width=True)

if fix_btn and code_input:
    with st.spinner("AI Fix kar raha hai..."):
        prompt = f"""
        You are FYP Buddy. Fix this student code.
        Code: {code_input}
        Error: {error_input}
        Give:
        1. Fixed Code (only python)
        2. Error ki wajah 1 line mai
        """
        try:
            response = model.generate_content(prompt)
            st.success("✅ Fixed!")
            st.code(response.text, language="python")
        except Exception as e:
            st.error(f"Error: {e}")

if explain_btn and code_input:
    with st.spinner("Explain kar raha hun..."):
        prompt = f"Is code ko simple Urdu/English mix mai explain karo FYP student ke liye: {code_input}"
        response = model.generate_content(prompt)
        st.info(response.text)

st.markdown("---")
st.markdown("Made for Hackathon | No Billing Needed | 100% Working")
