from pydantic import BaseModel, EmailStr, Field, validator
from datetime import date, datetime
from typing import Optional
import re

class PessoaBase(BaseModel):
    """Schema base com os campos comuns"""
    nome: str = Field(..., min_length=2, max_length=100, description="Nome completo da pessoa")
    email: str = Field(..., max_length=100, description="Endereço de email")
    telefone: str = Field(..., max_length=20, description="Número de telefone")
    cpf: str = Field(..., max_length=14, description="CPF da pessoa")
    data_nascimento: date = Field(..., description="Data de nascimento")
    ativo: bool = Field(default=True, description="Status do cadastro")

    @validator('data_nascimento', pre=True)
    def parse_data_nascimento(cls, v):
        if isinstance(v, str):
            try:
                # Tenta converter do formato dd/mm/yyyy
                return datetime.strptime(v, "%d/%m/%Y").date()
            except ValueError:
                try:
                    # Se falhar, tenta o formato ISO (yyyy-mm-dd)
                    return datetime.strptime(v, "%Y-%m-%d").date()
                except ValueError:
                    raise ValueError("Data deve estar no formato dd/mm/yyyy ou yyyy-mm-dd")
        return v

    @validator('cpf')
    def validate_cpf(cls, v):
        # Remove caracteres não numéricos
        cpf = re.sub(r'\D', '', v)
        
        if len(cpf) != 11:
            raise ValueError('CPF deve ter 11 dígitos')
            
        # Verifica se todos os dígitos são iguais
        if len(set(cpf)) == 1:
            raise ValueError('CPF inválido')
            
        # Validação do primeiro dígito verificador
        soma = 0
        for i in range(9):
            soma += int(cpf[i]) * (10 - i)
        resto = (soma * 10) % 11
        if resto == 10:
            resto = 0
        if resto != int(cpf[9]):
            raise ValueError('CPF inválido')
            
        # Validação do segundo dígito verificador
        soma = 0
        for i in range(10):
            soma += int(cpf[i]) * (11 - i)
        resto = (soma * 10) % 11
        if resto == 10:
            resto = 0
        if resto != int(cpf[10]):
            raise ValueError('CPF inválido')
            
        return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'

class PessoaCreate(PessoaBase):
    """Schema para criação de pessoa - herda todos os campos do PessoaBase"""
    pass

class PessoaUpdate(BaseModel):
    """
    Schema para atualização de pessoa.
    Todos os campos são opcionais, pois podemos querer atualizar apenas alguns campos.
    """
    nome: Optional[str] = Field(None, min_length=2, max_length=100)
    email: Optional[str] = Field(None, max_length=100)
    telefone: Optional[str] = Field(None, max_length=20)
    cpf: Optional[str] = Field(None, max_length=14)
    data_nascimento: Optional[date] = None
    ativo: Optional[bool] = None

class PessoaResponse(PessoaBase):
    """
    Schema para resposta - herda do PessoaBase e adiciona o id.
    Usado para retornar dados da API.
    """
    id: int = Field(..., description="ID único da pessoa")

    class Config:
        """Configuração para permitir o uso de modelos SQLAlchemy"""
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "nome": "João Silva",
                "email": "joao@email.com",
                "telefone": "(11) 98765-4321",
                "cpf": "123.456.789-01",
                "data_nascimento": "1990-01-01",
                "ativo": True
            }
        }
