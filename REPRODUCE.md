# 🛠️ Reproduction Guide

Follow these steps to run the FYP Buddy agent locally in a clean environment.

**1. Clone the Repository**
Open your terminal and clone the project:
```bash
git clone <YOUR-GITHUB-REPO-URL>
cd <YOUR-REPO-FOLDER>
```

**2. Install Dependencies**
Ensure you have Python installed, then install the required packages:
```bash
pip install -r requirements.txt
```

**3. Run the Application**
Launch the autonomous agent interface:
```bash
streamlit run app.py
```

**4. Testing the Agentic Workflow (Evaluation)**
1. Open the local browser URL provided by Streamlit.
2. Enter a free Groq API key (starts with `gsk_`).
3. Paste a broken Python script and its corresponding error message.
4. Click **Auto-Fix & Verify Loop** and observe the background verification.
