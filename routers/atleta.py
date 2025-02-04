from fastapi import APIRouter, Depends, Query
from sqlmodel import select
from sqlalchemy.exc import IntegrityError
from fastapi_pagination import Page, add_pagination, paginate

from atleta.models import atleta
from atleta.schemas import AtletaOut
from contrib.dependencies import DatabaseDependency

router = APIRouter()

@router.get("/", response_model=Page[AtletaOut])
async def get_all_atletas(
    db: DatabaseDependency,
    nome: str = Query(None, description="Filtrar por nome do atleta"),
    cpf: str = Query(None, description="Filtrar por CPF do atleta")
):
    query = select(Atleta)
    
    if nome:
        query = query.where(Atleta.nome.ilike(f"%{nome}%"))
    
    if cpf:
        query = query.where(Atleta.cpf == cpf)
    
    result = await db.exec(query)
    atletas = result.all()
    return paginate(atletas)