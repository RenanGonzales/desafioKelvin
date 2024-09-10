# CLI/models.py
from pydantic import BaseModel
from typing import List, Optional

class CotacaoModel(BaseModel):
    codigo: str
    preco: float
    variacao: float
    abertura: float
    fechamento: float
    horario: str
    data: str

class ClienteModel(BaseModel):
    cpf: str

class ApiResponseModel(BaseModel):
    cliente: ClienteModel
    cotações: List[CotacaoModel]
