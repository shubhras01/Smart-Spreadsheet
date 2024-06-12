from src.services.sheet_service import app
import os


if __name__ == "__main__":
    import uvicorn

    if not os.environ.get("OPENAI_API_KEY"):
        raise ValueError("OPENAI_API_KEY is empty in environment")
    uvicorn.run(app, host="0.0.0.0", port=8000)
