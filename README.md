#  FYP-Buddy AI: Autonomous Co-Pilot & Examiner

> **Built by Micro1 Certified Talent (Outstanding Performance) | Powered by Gemini Pro | Micro1 Hackathon Aug 28-30**

### The Problem: 70% of FYP Time Wasted
University seniors spend 70% of their Final Year Project time stuck on obscure Pandas/Python bugs and stressing over the final defense. One `KeyError: 'Marks'` can waste 3 days.

### The Solution: What Micro1 Values
FYP-Buddy is a **Gemini Pro-powered vetting engine** that does what Micro1 does for hiring, but for FYPs:

1.  ** The Bug-Squashing Engine:** A senior engineer persona that instantly patches Python logic and explains the root-cause so you can defend it in viva.

2.  ** The Viva Simulator (Adversarial AI):** An AI that adopts the persona of a *strict external examiner*. It scans your project and interrogates you with tough data science, math, and scalability questions - bulletproofing you for the real viva.

**Why This Wins Micro1:** Micro1 values AI that **objectively accelerates engineering and assesses skill**. FYP-Buddy does both: it acts as a senior engineer during build phase and a strict vetting engine during defense phase. The underlying Viva tech can be pivoted into a B2B product that autonomously interviews junior data science hires.

### Tech Stack
- **AI Engine:** Gemini Pro API (2M context, fast inference)
- **Backend:** FastAPI (Lightweight, snappy)
- **Frontend:** Streamlit (Dual-pane: Code Fixer | Viva Chat)
- **Data Handling:** Native Python/Pandas parsing

### Demo (2-min Video - Coming Soon on Aug 30)
Live Demo: https://fyp-buddy-ai-edaamwbjjm5ipcfypkezje.streamlit.app/ 

### How to Run
```bash
pip install streamlit google-generativeai fastapi
streamlit run app.py
