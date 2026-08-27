import streamlit as st

st.set_page_config(page_title="FYP Buddy - No API", page_icon="🤖")
st.title("🤖 FYP Buddy - Direct Gemini Pro")
st.caption("No API | No Billing | No Card Needed")

code = st.text_area("📋 Apna Code Paste Karo:", height=200)
error = st.text_area("❌ Error (agar hai):", height=100)

if st.button("✨ Perfect Prompt Banao"):
    if code:
        prompt = f"""Act as FYP Supervisor. Fix this code.

CODE:
{code}

ERROR:
{error}

YOUR TASK:
1. Give ONLY fixed working code with comments
2. Explain bug in 1 line simple Urdu
3. Keep simple for FYP student
Fix it now:"""
        
        st.success("✅ Prompt Ready! Copy karo:")
        st.code(prompt, language="markdown")
        st.markdown("### 👇 Ab ye karo:")
        st.markdown("1. Upar wala prompt Copy karo")
        st.markdown("2. Jao 👉 https://gemini.google.com")
        st.markdown("3. Paste karo - Fixed code mil jayega!")
        st.link_button("🚀 Open Gemini Pro", "https://gemini.google.com")
