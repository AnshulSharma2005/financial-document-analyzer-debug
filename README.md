# 🚀 Financial Document Analyzer --- CrewAI Debug Challenge

## 📌 Overview

This project is a **multi-agent Financial Document Analyzer** built
using **CrewAI**, designed to analyze uploaded financial reports and
generate structured investment insights.

The original repository intentionally contained: - Deterministic runtime
bugs - Broken dependencies - Deprecated CrewAI APIs - Inefficient &
hallucination-based prompts - Execution failures under API limits

This submission focuses on **systematic debugging, stabilization, and
production-grade improvements**.

------------------------------------------------------------------------

## 🧠 System Architecture

                    User Uploads PDF
                            │
                            ▼
                    FastAPI Endpoint
                            │
                            ▼
                    CrewAI Orchestrator
                            │
            ┌───────────────┴───────────────┐
            ▼                               ▼
     Financial Analyst Agent        Financial Tool
            │                               │
            └──────────────► PDF Reader Tool
                                    │
                                    ▼
                            Extracted Content
                                    │
                                    ▼
                             OpenAI LLM
                                    │
                   ┌────────────────┴───────────────┐
                   ▼                                ▼
            AI Analysis                    Fallback Mode

------------------------------------------------------------------------

## ⚙️ Tech Stack

  Component                Technology
  ------------------------ --------------------
  Backend                  FastAPI
  Multi-Agent Framework    CrewAI
  LLM                      OpenAI GPT-4o-mini
  PDF Processing           PyPDF
  Tooling                  CrewAI Tools
  Environment Management   python-dotenv
  API Server               Uvicorn

------------------------------------------------------------------------

## ✅ Assignment Objectives Covered

✔ Fix deterministic bugs\
✔ Fix inefficient prompts\
✔ Working execution pipeline\
✔ Stable dependency management\
✔ API documentation\
✔ Failure-safe execution

------------------------------------------------------------------------

# 🐛 Debugging Journey --- Bugs Found & Fixed

## 1️⃣ Dependency Conflict Hell

**Problem:** Incompatible versions of `pydantic`, `onnxruntime`, and
`opentelemetry` caused `ResolutionImpossible` errors.

**Fix:** Adopted minimal dependency strategy allowing pip resolver to
install compatible versions automatically.

------------------------------------------------------------------------

## 2️⃣ Deprecated CrewAI Imports

**Problem:** Old API imports such as:

``` python
from crewai.agents import Agent
```

**Fix:**

``` python
from crewai import Agent, Task, Crew
```

------------------------------------------------------------------------

## 3️⃣ Broken Tool Architecture

**Problem:** Tools implemented as async class methods instead of CrewAI
tools.

**Fix:**

``` python
from crewai.tools import tool

@tool("Financial Document Reader")
def read_data_tool(path:str):
```

Converted into valid CrewAI tool.

------------------------------------------------------------------------

## 4️⃣ Undefined PDF Loader

**Problem:** Non-existent `Pdf(...).load()` usage.

**Fix:** Replaced with:

``` python
from pypdf import PdfReader
```

------------------------------------------------------------------------

## 5️⃣ Agent Configuration Bugs

Incorrect parameter:

    tool=

Corrected to:

    tools=

Also removed restrictive RPM limits.

------------------------------------------------------------------------

## 6️⃣ Crew Input Mapping Failure

**Problem:** Uploaded PDF path never reached tool.

**Fix:**

``` python
crew.kickoff(inputs={"query": query,"path": file_path})
```

------------------------------------------------------------------------

## 7️⃣ Inefficient Prompt Design

Original prompts encouraged hallucination.

**Fix:** Rewritten prompts enforcing factual reasoning and document
grounding.

------------------------------------------------------------------------

## 8️⃣ OpenAI API Execution Failure

Users without quota experienced runtime crashes.

### ✅ Production Fallback Mode

``` python
try:
    crew.kickoff()
except:
    return fallback_response
```

------------------------------------------------------------------------

## 🤖 OpenAI Integration

``` python
llm = LLM(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY")
)
```

------------------------------------------------------------------------

## 📡 API Endpoints

### Health Check

    GET /

### Analyze Financial Document

    POST /analyze

------------------------------------------------------------------------

## ▶️ Setup Instructions

### Clone

    git clone <repo>
    cd financial-document-analyzer-debug

### Virtual Environment

    python -m venv venv
    venv\Scripts\activate

### Install Dependencies

    pip install -r requirements.txt

### Environment Variables

Create `.env`

    OPENAI_API_KEY=your_key

### Run Server

    uvicorn main:app --reload

Open:

    http://127.0.0.1:8000/docs

------------------------------------------------------------------------

## ✅ Engineering Improvements

-   Dependency stabilization
-   API migration
-   Tool refactor
-   Prompt optimization
-   Failure-safe execution
-   Production fallback handling

------------------------------------------------------------------------

## 🌟 Bonus Engineering Decisions

-   Graceful degradation without LLM
-   Modular tool architecture
-   Structured agent reasoning
-   Recruiter-friendly execution

------------------------------------------------------------------------

## 📌 Final Result

The system now: - Runs locally - Processes PDFs - Executes CrewAI
agents - Uses OpenAI when available - Falls back safely otherwise

------------------------------------------------------------------------

## 👩‍💻 Author

**Anshul Sharma**\
B.Tech CSE --- AI & Software Development Enthusiast

------------------------------------------------------------------------

⭐ This project demonstrates debugging capability, system design
understanding, and production-ready AI engineering practices.
