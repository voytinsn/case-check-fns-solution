from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import JSONResponse
from pathlib import Path
import json

app = FastAPI()
DATA_DIR = Path("responses")

@app.get("/api/check")
def check(req: int = Query(..., description="INN number (must be int)")):
    file_path = DATA_DIR / f"{req}.json"

    if not file_path.exists():
        raise HTTPException(status_code=404, detail="INN not found")

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return JSONResponse(content=data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to load data: {e}")
