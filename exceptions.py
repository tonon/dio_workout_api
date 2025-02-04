from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError

async def integrity_error_handler(request: Request, exc: IntegrityError):
    if "cpf" in str(exc).lower():
        cpf = request.json().get("cpf")
        return JSONResponse(
            status_code=303,
            content={"detail": f"Já existe um atleta cadastrado com o cpf: {cpf}"}
        )
    return JSONResponse(
        status_code=500,
        content={"detail": "Erro de integridade no banco de dados"}
    )