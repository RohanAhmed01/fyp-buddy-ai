import streamlit as st
import subprocess
import os
import re
from google import genai

# UI Configuration
st.set_page_config(page_title="FYP Buddy - Agentic Workflow", page_icon="🤖")
st.title("🤖 FYP Buddy - Autonomous Code Agent")
st.caption("Micro1 Hackathon | Self-Correcting Execution Pipeline")

# We require an API key for the agent to function autonomously
api_key = st.text_input("Enter your Gemini API Key to run the agent:", type="password")

def extract_python_code(text: str) -> str:
    """Helper to extract raw Python code from markdown blocks."""
    match = re.search(r"```python\n(.*?)\n```", text, re.DOTALL)
    return match.group(1) if match else text

def run_code_sandbox(code_to_run: str):
    """Executes the Python code safely in a subprocess and captures output."""
    temp_file = "temp_exec.py"
    try:
        with open(temp_file, "w") as f:
            f.write(code_to_run)
        
        # Run with a 5-second timeout to prevent infinite loops
        result = subprocess.run(
            ["python", temp_file], 
            capture_output=True, 
            text=True, 
            timeout=5
        )
        os.remove(temp_file)
        
        if result.returncode == 0:
            return True, result.stdout
        else:
            return False, result.stderr
            
    except subprocess.TimeoutExpired:
        if os.path.exists(temp_file):
            os.remove(temp_file)
        return False, "Timeout: Code execution took too long (potential infinite loop)."
    except Exception as e:
        if os.path.exists(temp_file):
            os.remove(temp_file)
        return False, str(e)

# User Inputs
code = st.text_area("📋 Paste your broken code here 👇:", height=200)
error = st.text_area("❌ Error (if any):", height=100)

if st.button("✨ Auto-Fix & Verify"):
    if not api_key:
        st.error("Please provide a Gemini API Key to start the agent.")
        st.stop()
    if not code:
        st.warning("Please paste some code to fix.")
        st.stop()
        
    # Initialize the official Gen AI SDK
    client = genai.Client(api_key=api_key)
    
    # Base Prompt Configuration
    prompt = f"""Act as an Expert Code Surgeon. Fix the following Python code based on the provided error.
    
    CODE:
    {code}
    
    ERROR:
    {error}
    
    Provide ONLY the corrected Python code enclosed in ```python ``` blocks. Do not add any conversational text."""
    
    max_retries = 3
    success = False
    final_code = ""
    
    with st.status("Initializing Agentic Loop...", expanded=True) as status:
        for attempt in range(1, max_retries + 1):
            st.write(f"🔄 **Iteration {attempt}**: Generating fix via Gemini...")
            
            try:
                # Agent Step 1: Generate Code
                response = client.models.generate_content(
                    model='gemini-2.5-pro', # Use a capable model for coding
                    contents=prompt,
                )
                
                extracted_code = extract_python_code(response.text)
                
                # Agent Step 2: Sandbox Verification
                st.write("⚙️ Running code in sandbox verifier...")
                passed, execution_output = run_code_sandbox(extracted_code)
                
                if passed:
                    st.write("✅ Code passed sandbox execution!")
                    status.update(label="Debugging Complete!", state="complete", expanded=False)
                    final_code = extracted_code
                    success = True
                    break
                else:
                    st.write(f"❌ Execution failed. Extracting traceback for self-correction...")
                    with st.expander("View Traceback"):
                        st.code(execution_output, language="bash")
                    
                    # Agent Step 3: Self-Correction Prompt update
                    prompt = f"""The previous fix failed during execution. Here is the new traceback error.
                    
                    FAILED CODE:
                    {extracted_code}
                    
                    NEW EXECUTION ERROR:
                    {execution_output}
                    
                    Analyze the execution error and fix the code. Provide ONLY the corrected Python code enclosed in ```python ``` blocks."""
                    
            except Exception as e:
                st.error(f"API Error encountered: {e}")
                break
                
    # Final Output Display
    if success:
        st.success("🎉 Working Code Generated and Verified!")
        st.code(final_code, language="python")
    else:
        st.error("⚠️ The agent reached the maximum number of retries without finding a verifiable fix. Manual intervention required.")
