from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AlienRequest(BaseModel):
    alien_number: str

@app.post("/status")
async def consultar_status(request: AlienRequest):
    try:
        alien = request.alien_number
        resultado = {
            "name": "John Doe",
            "case_status": "Pending",
            "hearing_date": "2025-12-01",
            "judge": "Maria Reyes",
            "alien": alien
        }
        return JSONResponse(content=resultado)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
