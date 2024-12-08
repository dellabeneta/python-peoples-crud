from typing import Generic, TypeVar, List
from pydantic import BaseModel

# Tipo genérico para os itens
T = TypeVar('T')

class PaginatedResponse(BaseModel, Generic[T]):
    """Modelo para respostas paginadas"""
    items: List[T]
    total: int
    page: int
    per_page: int
    total_pages: int
