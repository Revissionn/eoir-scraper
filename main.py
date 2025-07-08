from fastapi import FastAPI, Request

app = FastAPI()

@app.route("/status", methods=["POST"])
async def consulta(request):
    try:
        data = await request.json()
        alien = data.get("alien_number")
        if not alien:
            return response.json({"error": "El campo 'alien_number' es obligatorio."}, status=400)
        
        # Aquí va tu lógica de scraping con ese alien_number
        # ejemplo: resultado = buscar_en_eoir(alien)
        resultado = {"status": "simulado", "alien": alien}  # temporal

        return response.json(resultado)
    
    except Exception as e:
        return response.json({"error": str(e)}, status=500)
