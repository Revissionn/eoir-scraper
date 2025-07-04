from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/eoir-status")
async def consultar_eoir(request: Request):
    data = await request.json()
    alien_number = data.get("alien_number")
    
    # Aquí iría la lógica para consultar EOIR y devolver datos simulados o reales
    return {
        "nombre": "JUAN PÉREZ",
        "estatus": "Audiencia programada",
        "fecha": "2025-10-12",
        "juez": "Hon. Martínez"
    }
