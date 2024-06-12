from services.sheet_service import app
from data_parser.worksheet_manager import WorksheetManagerFactory


if __name__ == "__main__":
    import uvicorn

    worksheet_manager_factory = WorksheetManagerFactory()
    uvicorn.run(app, host="0.0.0.0", port=8000)
