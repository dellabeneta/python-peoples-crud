import sys
import os
import random
from datetime import datetime

# Adiciona o diretório pai ao PYTHONPATH
backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(backend_dir)

from app.core.database import SessionLocal, engine, Base
from app.models.pessoa import Pessoa

# Listas de nomes e sobrenomes comuns brasileiros
nomes = [
    "João", "Maria", "José", "Ana", "Pedro", "Paulo", "Carlos", "Lucas",
    "Marcos", "Gabriel", "Rafael", "Felipe", "Bruno", "Rodrigo", "Gustavo",
    "Daniel", "Marcelo", "Eduardo", "Leonardo", "André", "Luiz", "Ricardo",
    "Julia", "Beatriz", "Mariana", "Larissa", "Amanda", "Fernanda", "Patricia",
    "Camila", "Carolina", "Leticia", "Isabela", "Gabriela", "Manuela", "Sofia",
    "Alice", "Laura", "Valentina", "Helena", "Sophia", "Isabella", "Miguel",
    "Arthur", "Bernardo", "Heitor", "Davi", "Lorenzo", "Théo", "Noah", "Isaac"
]

sobrenomes = [
    "Silva", "Santos", "Oliveira", "Souza", "Rodrigues", "Ferreira", "Alves",
    "Pereira", "Lima", "Gomes", "Costa", "Ribeiro", "Martins", "Carvalho",
    "Almeida", "Lopes", "Soares", "Fernandes", "Vieira", "Barbosa", "Rocha",
    "Dias", "Nascimento", "Andrade", "Moreira", "Nunes", "Marques", "Machado",
    "Mendes", "Freitas", "Cardoso", "Ramos", "Gonçalves", "Santana", "Teixeira",
    "Moraes", "Correia", "Pinto", "Cruz", "Cunha", "Azevedo", "Cavalcanti"
]

def gerar_cpf():
    """Gera um CPF válido"""
    def calcula_digito(digs):
        mult = len(digs) + 1
        soma = sum(d * m for d, m in zip(digs, range(mult, 1, -1)))
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    # Gera os primeiros 9 dígitos
    cpf = [random.randint(0, 9) for _ in range(9)]
    
    # Adiciona dígitos verificadores
    cpf.append(calcula_digito(cpf))
    cpf.append(calcula_digito(cpf))
    
    # Formata o CPF
    cpf_str = ''.join(map(str, cpf))
    return f"{cpf_str[:3]}.{cpf_str[3:6]}.{cpf_str[6:9]}-{cpf_str[9:]}"

def gerar_telefone():
    """Gera um número de telefone"""
    ddd = random.randint(11, 99)
    numero = random.randint(10000000, 99999999)
    return f"({ddd}) 9-{str(numero)[:4]}-{str(numero)[4:]}"

def gerar_data_nascimento():
    """Gera uma data de nascimento"""
    ano = random.randint(1960, 2005)
    mes = random.randint(1, 12)
    # Ajusta o último dia baseado no mês
    ultimo_dia = 31
    if mes in [4, 6, 9, 11]:
        ultimo_dia = 30
    elif mes == 2:
        ultimo_dia = 29 if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0) else 28
    
    dia = random.randint(1, ultimo_dia)
    return datetime(ano, mes, dia).date()

def gerar_email(nome, sobrenome):
    """Gera um email"""
    # Remove acentos
    from unicodedata import normalize
    nome_limpo = normalize('NFKD', nome.lower()).encode('ASCII', 'ignore').decode('ASCII')
    sobrenome_limpo = normalize('NFKD', sobrenome.lower()).encode('ASCII', 'ignore').decode('ASCII')
    
    # Diferentes formatos de email
    formatos = [
        f"{nome_limpo}.{sobrenome_limpo}",
        f"{nome_limpo}{sobrenome_limpo}",
        f"{nome_limpo}.{sobrenome_limpo[:3]}",
        f"{nome_limpo[:1]}{sobrenome_limpo}",
        f"{nome_limpo}{random.randint(1, 99)}"
    ]
    
    email = random.choice(formatos)
    dominios = ["gmail.com", "hotmail.com", "yahoo.com.br", "outlook.com", "uol.com.br"]
    return f"{email}@{random.choice(dominios)}"

def criar_pessoas(quantidade=200):
    """
    Cria a quantidade especificada de pessoas com dados aleatórios
    """
    # Criar tabelas se não existirem
    Base.metadata.create_all(engine)
    
    # Criar sessão
    db = SessionLocal()
    
    try:
        # Lista para armazenar todas as pessoas antes de fazer o commit
        pessoas = []
        emails_usados = set()
        cpfs_usados = set()
        
        while len(pessoas) < quantidade:
            nome = random.choice(nomes)
            sobrenome = random.choice(sobrenomes)
            email = gerar_email(nome, sobrenome)
            cpf = gerar_cpf()
            
            # Verifica se email ou CPF já foram usados
            if email in emails_usados or cpf in cpfs_usados:
                continue
                
            emails_usados.add(email)
            cpfs_usados.add(cpf)
            
            pessoa = Pessoa(
                nome=f"{nome} {sobrenome}",
                email=email,
                telefone=gerar_telefone(),
                cpf=cpf,
                data_nascimento=gerar_data_nascimento(),
                ativo=True
            )
            pessoas.append(pessoa)
        
        # Adiciona todas as pessoas de uma vez
        db.add_all(pessoas)
        db.commit()
        print(f"{quantidade} pessoas criadas com sucesso!")
        
    except Exception as e:
        print(f"Erro ao criar pessoas: {str(e)}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    criar_pessoas(200)
