from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.database import Base
from app.models.user import User
import os

# Garantir que o diretório data existe
os.makedirs("./data", exist_ok=True)

# URL de conexão com o PostgreSQL
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@localhost:5432/sistema_cadastro"
)

# Criar engine e sessão
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
db = SessionLocal()

# Buscar admin
admin = db.query(User).filter(User.username == "admin").first()

if admin:
    print("Usuário admin encontrado:")
    print(f"Username: {admin.username}")
    print(f"Email: {admin.email}")
    print(f"Senha hash: {admin.hashed_password}")
else:
    print("Usuário admin NÃO encontrado!")

# Verificar se há algum usuário no banco
user_count = db.query(User).count()

print(f"Total de usuários no banco: {user_count}")

# Fechar a sessão
db.close()
