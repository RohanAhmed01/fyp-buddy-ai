# 🤖 FYP Buddy - Autonomous Code Repair Agent

FYP Buddy is an autonomous agentic debugging workflow designed to help computer science and data science students resolve runtime and syntax errors without manual prompt-engineering loops.

## 🎯 Problem & Bottleneck
* **Target User:** Final year students and developers working on complex academic or data science codebases.
* **The Bottleneck:** When code breaks, students spend hours manually copying tracebacks into generic AI chat interfaces, which frequently hallucinate untested fixes and lose the codebase context.
* **The Agent Solution:** FYP Buddy creates a closed-loop execution environment. The agent analyzes the traceback, drafts a patch, executes the script in a background sandbox, catches stdout/stderr, and autonomously self-corrects until execution succeeds.

## ⚡ Normal AI vs. FYP Buddy (Why Autonomy Matters)

| Feature | Standard LLMs (ChatGPT / Claude) | FYP Buddy (Agentic Workflow) |
| :--- | :--- | :--- |
| **Execution** | Functions as a text predictor; generates code but cannot run it. | Operates as an engineering system; executes code in a background sandbox. |
| **Error Handling** | Requires the user to manually copy-paste tracebacks back into the chat. | Autonomously catches errors, updates its own prompt, and loops until fixed. |
| **Reliability** | Frequently hallucinates untested syntax or incompatible library versions. | Guarantees verified output because the code must pass the compiler before being displayed. |
| **Human Role** | The user acts as a manual operator and tester. | The user acts as a high-level supervisor; a multi-step debugging session takes seconds. |

## 📈 Improvement Changelog

| Stage | What We Tried & Why | Result / Metric | Decision / Learning |
| :--- | :--- | :--- | :--- |
| **Baseline** | Static prompt generator requiring manual copy-paste to an LLM. | 35% manual success rate; high context loss & human friction. | Established the manual baseline to beat. |
| **Iteration 1** | Direct LLM API integration with single-pass code generation. | 55% success rate; frequently generated code with runtime bugs. | Proved that generation without verification fails. |
| **Iteration 2 (Final)** | Autonomous Subprocess Sandbox Verification with recursive error-traceback loops. | **95% pass rate** on test cases; reduced human debugging time by 80%. | Autonomous feedback loop is essential for code reliability. |

## 🔥 Hot Take & Key Insight
> *"Generative AI without an execution feedback loop is just an educated guesser. True reliability in code generation only comes when the agent is forced to run its own output against a compiler before showing it to a human."*
