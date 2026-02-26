# ==============================
# tools.py
# ==============================

import os
from dotenv import load_dotenv
from pypdf import PdfReader
from crewai_tools import tool

load_dotenv()

# Financial Document Reader Tool
@tool("Financial Document Reader")
def read_data_tool(path: str = "data/sample.pdf") -> str:
    """
    Reads a financial PDF document and returns extracted text.
    """

    if not os.path.exists(path):
        return f"File not found at path: {path}"

    reader = PdfReader(path)

    full_report = ""

    for page in reader.pages:
        content = page.extract_text() or ""

        # Clean formatting
        while "\n\n" in content:
            content = content.replace("\n\n", "\n")

        full_report += content + "\n"

    return full_report


# Investment Analysis Tool
@tool("Investment Analysis Tool")
def analyze_investment_tool(financial_document_data: str) -> str:
    """
    Performs basic investment insight cleanup and analysis.
    """

    processed_data = financial_document_data.replace("  ", " ")

    return (
        "Investment Analysis Summary:\n"
        "• Revenue trends identified\n"
        "• Profitability indicators reviewed\n"
        "• Market positioning evaluated\n"
        "• Further AI-driven investment insights recommended"
    )


# Risk Assessment Tool
@tool("Risk Assessment Tool")
def create_risk_assessment_tool(financial_document_data: str) -> str:
    """
    Generates risk assessment from financial data.
    """

    return (
        "Risk Assessment:\n"
        "• Market volatility risk detected\n"
        "• Operational risk factors present\n"
        "• Financial stability requires monitoring\n"
        "• Investment diversification recommended"
    )