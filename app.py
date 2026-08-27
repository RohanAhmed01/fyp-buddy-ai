import streamlit as st
from google import genai

st.set_page_config(page_title="FYP Buddy", page_icon="🤖")

# Nayi key se client banao
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

BUG_PROMPT = """
You are an expert programmer. Fix the given code.
Return ONLY the fixed code, no explanation.
"""

st.title("FYP Buddy - Fix My Code")

code = st.text_area("Paste your code here:", height=300)
error = st.text_area("Paste error (optional):", height=100)

if st.button("Fix My Code"):
    if not code:
        st.warning("Please paste code first!")
    else:
        with st.spinner("Fixing..."):
            try:
                response = client.models.generate_content(
                    model="gemini-3.6-flash",
                    contents=f"{BUG_PROMPT}\n\nCode:\n{code}\n\nError:\n{error}"
                )
                st.success("Fixed!")
                st.code(response.text, language="python")
            except Exception as e:
                st.error(f"Error: {e}")
