from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.database import Base
from app.models.user import User
import os

# URL de conexão com o PostgreSQL
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@postgres:5432/sistema_cadastro"
)

# Configurações do Admin via Variáveis de Ambiente
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "admin")
ADMIN_EMAIL = os.getenv("ADMIN_EMAIL", "admin@example.com")

# Criar banco e tabelas
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

# Criar sessão
SessionLocal = sessionmaker(bind=engine)
db = SessionLocal()

# Verificar se o admin já existe
existing_admin = db.query(User).filter(User.username == ADMIN_USERNAME).first()

if not existing_admin:
    # Criar usuário admin apenas se não existir
    admin = User(
        username=ADMIN_USERNAME,
        email=ADMIN_EMAIL,
        hashed_password=User.get_password_hash(ADMIN_PASSWORD)
    )

    # Adicionar ao banco
    db.add(admin)
    db.commit()
    print(f"Usuário admin criado:")
    print(f"Username: {ADMIN_USERNAME}")
    print(f"Email: {ADMIN_EMAIL}")
else:
    print(f"Usuário admin {ADMIN_USERNAME} já existe, pulando criação")

db.close()
