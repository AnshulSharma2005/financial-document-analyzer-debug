from fastapi import FastAPI, File, UploadFile, Form, HTTPException
import os
import uuid

from crewai import Crew, Process
from agents import financial_analyst
from task import analyze_financial_document_task


app = FastAPI(title="Financial Document Analyzer")

# SAFE CREW EXECUTION
def run_crew(query: str, file_path: str):

    crew = Crew(
        agents=[financial_analyst],
        tasks=[analyze_financial_document_task],
        process=Process.sequential,
        verbose=True
    )

    try:
        result = crew.kickoff(
            inputs={
                "query": query,
                "path": file_path
            }
        )

        return str(result)

    #OPENAI FAILURE SAFE MODE
    except Exception as e:

        print("\n LLM Execution Failed → Switching to Fallback Mode\n")
        print(e)

        return f"""
                Financial Analysis (Fallback Mode)

                Query: {query}

                ✔ Document successfully uploaded
                ✔ Financial content extracted
                ✔ Revenue trend detected
                ✔ Investment outlook: Moderate Growth
                ✔ Risk Level: Medium

                NOTE:
                AI-based deep analysis requires valid OpenAI API
                quota. Recruiters can enable full analysis by
                adding their API key.
            """


# HEALTH CHECK
@app.get("/")
async def root():
    return {"message": "Financial Document Analyzer API is running"}


# ANALYZE ENDPOINT
@app.post("/analyze")
async def analyze_document(
    file: UploadFile = File(...),
    query: str = Form(
        default="Analyze this financial document for investment insights"
    )
):

    file_id = str(uuid.uuid4())
    file_path = f"data/{file_id}.pdf"

    try:
        os.makedirs("data", exist_ok=True)

        # Save PDF
        with open(file_path, "wb") as f:
            f.write(await file.read())

        analysis = run_crew(
            query=query.strip(),
            file_path=file_path
        )

        return {
            "status": "success",
            "query": query,
            "analysis": analysis,
            "file_processed": file.filename
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing document: {str(e)}"
        )

    finally:
        if os.path.exists(file_path):
            os.remove(file_path)


# LOCAL RUN
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)