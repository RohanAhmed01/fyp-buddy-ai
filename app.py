import streamlit as st

st.set_page_config(page_title="FYP Buddy - No API", page_icon="🤖")
st.title("🤖 FYP Buddy - Direct Gemini Pro")
st.caption("No API | No Billing | No Card Needed")

code = st.text_area("📋 Paste your code here 👇:", height=200)
error = st.text_area("❌ Error (if any):", height=100)

if st.button("✨ Generate perfect prompt"):
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
        
        st.success("✅ Prompt Ready! Copy code:")
        st.code(prompt, language="markdown")
        st.markdown("### 👇 Now do this:")
        st.markdown("1. Copy the upper code")
        st.markdown("2. Jao 👉 https://gemini.google.com")
        st.markdown("3. Paste it - Fixed code will be given!")
        st.link_button("🚀 Open Gemini Pro", "https://gemini.google.com")
