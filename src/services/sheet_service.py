import os
from fastapi import FastAPI, HTTPException
import uvicorn

from src.data_parser.worksheet_manager import WorksheetManagerFactory

app = FastAPI()

worksheet_manager = WorksheetManagerFactory()


@app.post("/register_worksheet/")
def register_worksheet(file_path: str):
    try:
        # Load the Excel file into a DataFrame
        worksheet_manager.register_worksheet(file_path)
        return {"message": "File parsed successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/ask_smart/")
def ask_question(query: str):
    if not query or not query.strip():
        raise ValueError("I am Smart spreadsheet, dont miss your chance to ask question - "
                         "Give me a query, and get a smart response. But dont give **Empty** query")
    if not worksheet_manager.get_registered_worksheet():
        raise ValueError("worksheet is not registered - please register a worksheet first")
    try:
        answer = worksheet_manager.get_registered_worksheet().ask_worksheet(query)
        return {"question": query, "answer": answer}
    except Exception as e:
        raise HTTPException(status_code=503, detail=str(e))


# Main function to run the app
if __name__ == "__main__":
    if not os.environ.get("OPENAI_API_KEY"):
        raise ValueError("OPENAI_API_KEY is empty in environment")
    uvicorn.run(app, host="0.0.0.0", port=8000)
