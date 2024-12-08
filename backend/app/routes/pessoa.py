from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from datetime import date
from math import ceil

from app.core.database import get_db
from app.models.pessoa import Pessoa
from app.schemas.pessoa import PessoaCreate, PessoaUpdate, PessoaResponse
from app.schemas.pagination import PaginatedResponse
from app.core.auth import verify_token

# Criar o router com prefixo /pessoas
router = APIRouter(
    prefix="/pessoas",
    tags=["pessoas"],
    responses={404: {"description": "Pessoa não encontrada"}}
)

@router.post("/", response_model=PessoaResponse, status_code=status.HTTP_201_CREATED)
def criar_pessoa(pessoa: PessoaCreate, db: Session = Depends(get_db), current_user = Depends(verify_token)):
    """
    Cria uma nova pessoa no sistema.
    
    Args:
        pessoa: Dados da pessoa a ser criada
        db: Sessão do banco de dados
    
    Returns:
        PessoaResponse: Dados da pessoa criada
    
    Raises:
        HTTPException: Se o email já estiver cadastrado
    """
    # Verificar se já existe pessoa com este email
    db_pessoa = db.query(Pessoa).filter(Pessoa.email == pessoa.email).first()
    if db_pessoa:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email já cadastrado"
        )
    
    # Criar nova pessoa
    db_pessoa = Pessoa(**pessoa.model_dump())
    db.add(db_pessoa)
    db.commit()
    db.refresh(db_pessoa)
    return db_pessoa

@router.get("/", response_model=PaginatedResponse[PessoaResponse])
def listar_pessoas(
    page: int = 1,
    per_page: int = 10,
    search: str = None,
    db: Session = Depends(get_db),
    current_user = Depends(verify_token)
):
    """
    Lista todas as pessoas cadastradas com paginação e pesquisa.
    """
    # Query base
    query = db.query(Pessoa)
    
    # Aplicar filtro de pesquisa se fornecido
    if search:
        search_term = f"%{search}%"
        query = query.filter(
            (Pessoa.nome.ilike(search_term)) |
            (Pessoa.email.ilike(search_term)) |
            (Pessoa.cpf.ilike(search_term))
        )
    
    # Calcular total e aplicar paginação
    total = query.count()
    pessoas = query.offset((page - 1) * per_page).limit(per_page).all()
    
    total_pages = ceil(total / per_page) if total > 0 else 0
    
    return {
        "items": pessoas,
        "total": total,
        "page": page,
        "per_page": per_page,
        "total_pages": total_pages,
        "pages": total_pages
    }

@router.get("/{pessoa_id}", response_model=PessoaResponse)
def obter_pessoa(pessoa_id: int, db: Session = Depends(get_db), current_user = Depends(verify_token)):
    """
    Obtém uma pessoa específica pelo ID.
    
    Args:
        pessoa_id: ID da pessoa
        db: Sessão do banco de dados
    
    Returns:
        PessoaResponse: Dados da pessoa encontrada
    
    Raises:
        HTTPException: Se a pessoa não for encontrada
    """
    db_pessoa = db.query(Pessoa).filter(Pessoa.id == pessoa_id).first()
    if db_pessoa is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Pessoa não encontrada"
        )
    return db_pessoa

@router.put("/{pessoa_id}", response_model=PessoaResponse)
def atualizar_pessoa(
    pessoa_id: int,
    pessoa: PessoaUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(verify_token)
):
    """
    Atualiza os dados de uma pessoa específica.
    
    Args:
        pessoa_id: ID da pessoa
        pessoa: Dados a serem atualizados
        db: Sessão do banco de dados
    
    Returns:
        PessoaResponse: Dados atualizados da pessoa
    
    Raises:
        HTTPException: Se a pessoa não for encontrada
    """
    db_pessoa = db.query(Pessoa).filter(Pessoa.id == pessoa_id).first()
    if db_pessoa is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Pessoa não encontrada"
        )
    
    # Atualizar apenas os campos fornecidos
    for field, value in pessoa.model_dump(exclude_unset=True).items():
        setattr(db_pessoa, field, value)
    
    db.commit()
    db.refresh(db_pessoa)
    return db_pessoa

@router.delete("/{pessoa_id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_pessoa(pessoa_id: int, db: Session = Depends(get_db), current_user = Depends(verify_token)):
    """
    Remove uma pessoa do sistema.
    
    Args:
        pessoa_id: ID da pessoa
        db: Sessão do banco de dados
    
    Raises:
        HTTPException: Se a pessoa não for encontrada
    """
    db_pessoa = db.query(Pessoa).filter(Pessoa.id == pessoa_id).first()
    if db_pessoa is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Pessoa não encontrada"
        )
    
    db.delete(db_pessoa)
    db.commit()
    return None
