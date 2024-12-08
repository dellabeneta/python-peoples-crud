from sqlalchemy import Column, Integer, String, Date, Boolean
from app.core.database import Base

class Pessoa(Base):
    """
    Modelo de dados para a tabela de pessoas.
    
    Atributos:
        id: Identificador único
        nome: Nome completo da pessoa
        email: Endereço de email (único)
        telefone: Número de telefone
        cpf: CPF da pessoa (único)
        data_nascimento: Data de nascimento
        ativo: Status do cadastro
    """
    __tablename__ = "pessoas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    telefone = Column(String(20))
    cpf = Column(String(14), unique=True, index=True, nullable=False)
    data_nascimento = Column(Date)
    ativo = Column(Boolean, default=True)

    def __repr__(self):
        return f"<Pessoa(id={self.id}, nome='{self.nome}', email='{self.email}')>"
