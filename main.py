from sanic import Sanic, response
from sanic_cors import CORS

app = Sanic("eoir-scraper")
CORS(app)

@app.route("/status", methods=["POST"])
async def consulta(request):
    try:
        data = await request.json()
        alien = data.get("alien_number")

        if not alien:
            return response.json({"error": "El campo 'alien_number' es obligatorio"}, status=400)

        # Aquí va tu scraping real. Por ahora, simulamos respuesta:
        resultado = {
            "name": "John Doe",
            "case_status": "Pending",
            "hearing_date": "2025-12-01",
            "judge": "Maria Reyes",
            "alien": alien
        }

        return response.json(resultado)

    except Exception as e:
        return response.json({"error": str(e)}, status=500)

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=10000)
