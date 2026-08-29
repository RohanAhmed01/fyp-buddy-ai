import streamlit as st
import subprocess
import os
import re
from groq import Groq

st.set_page_config(page_title="FYP Buddy - Autonomous Code Agent", page_icon="🤖")
st.title("🤖 FYP Buddy - Autonomous Code Agent")
st.caption("Micro1 Hackathon | Powered by Groq (Free Tier, No Card Required)")

api_key = st.text_input("Enter your Free Groq API Key (starts with gsk_):", type="password")

def extract_python_code(text: str) -> str:
    """Extracts clean python code from markdown blocks."""
    match = re.search(r"```python\s*(.*?)\s*```", text, re.DOTALL)
    if match:
        return match.group(1).strip()
    match_generic = re.search(r"```\s*(.*?)\s*```", text, re.DOTALL)
    if match_generic:
        return match_generic.group(1).strip()
    return text.strip()

def run_code_sandbox(code_to_run: str):
    """Executes the Python code in a safe subprocess and captures stdout/stderr."""
    temp_file = "temp_exec.py"
    try:
        with open(temp_file, "w", encoding="utf-8") as f:
            f.write(code_to_run)
        
        result = subprocess.run(
            ["python", temp_file], 
            capture_output=True, 
            text=True, 
            timeout=5
        )
        if os.path.exists(temp_file):
            os.remove(temp_file)
        
        if result.returncode == 0:
            return True, result.stdout if result.stdout else "Executed successfully with 0 exit code."
        else:
            return False, result.stderr
            
    except subprocess.TimeoutExpired:
        if os.path.exists(temp_file):
            os.remove(temp_file)
        return False, "Timeout: Code execution exceeded 5 seconds (potential infinite loop)."
    except Exception as e:
        if os.path.exists(temp_file):
            os.remove(temp_file)
        return False, str(e)

code = st.text_area("📋 Paste your broken code here 👇:", height=180)
error = st.text_area("❌ Error / Traceback (if any):", height=90)

if st.button("🚀 Auto-Fix & Verify Loop"):
    if not api_key:
        st.error("Please enter your Groq API key to start.")
        st.stop()
    if not code.strip():
        st.warning("Please paste some code to debug.")
        st.stop()
        
    client = Groq(api_key=api_key)
    
    current_prompt = f"""You are an expert autonomous code debugger.
Fix the Python code below based on the error.

CODE:
{code}

ERROR CONTEXT:
{error}

Rules:
1. Provide the complete executable fix inside a ```python ``` block.
2. Do not include markdown notes outside the code block."""

    max_retries = 3
    success = False
    final_code = ""
    
    with st.status("Running Autonomous Agent Loop...", expanded=True) as status:
        for attempt in range(1, max_retries + 1):
            st.write(f"🔄 **Iteration {attempt}**: Requesting patch from Llama 3...")
            
            try:
                chat_completion = client.chat.completions.create(
                    messages=[
                        {"role": "system", "content": "You are a code repair agent. Always return code inside ```python blocks."},
                        {"role": "user", "content": current_prompt}
                    ],
                    model="llama-3.3-70b-versatile",
                    temperature=0.2,
                )
                
                raw_response = chat_completion.choices[0].message.content
                extracted_code = extract_python_code(raw_response)
                
                st.write("⚙️ Executing patch in sandbox...")
                passed, exec_output = run_code_sandbox(extracted_code)
                
                if passed:
                    st.write("✅ Execution passed verification!")
                    status.update(label="Debugging Completed Successfully!", state="complete", expanded=False)
                    final_code = extracted_code
                    success = True
                    break
                else:
                    st.write(f"⚠️ Run failed on attempt {attempt}. Feeding error traceback back to agent...")
                    with st.expander(f"Attempt {attempt} Traceback"):
                        st.code(exec_output, language="bash")
                    
                    # Update reflection prompt for next iteration
                    current_prompt = f"""The previous fix produced the following runtime error:

FAILED CODE:
{extracted_code}

TRACEBACK / RUNTIME ERROR:
{exec_output}

Fix the code so it executes without error. Return ONLY the code inside ```python ``` blocks."""
            
            except Exception as e:
                st.error(f"API Error: {e}")
                break
                
    if success:
        st.success("🎉 Working Code Verified & Ready!")
        st.code(final_code, language="python")
    else:
        st.error("❌ Agent could not resolve all execution errors within maximum retries.")
