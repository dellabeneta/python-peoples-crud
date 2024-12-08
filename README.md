## Status do Projeto

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/dellabeneta/python-peoples-crud/docker-publish.yml?label=Build)
![GitHub top language](https://img.shields.io/github/languages/top/dellabeneta/python-peoples-crud)
![GitHub License](https://img.shields.io/github/license/dellabeneta/python-peoples-crud?color=blue)
![GitHub Release](https://img.shields.io/github/v/release/dellabeneta/python-peoples-crud)

# Sistema de Cadastro de Pessoas

## Descrição do Projeto
Um sistema completo de CRUD de pessoas com autenticação JWT, frontend em React, backend em FastAPI e banco de dados PostgreSQL.

## Pré-requisitos
- Docker
- Docker Compose
- Make (opcional, mas recomendado)

## Configuração Local

### 1. Clonar o Repositório
```bash
git clone <url-do-repositorio>
cd python-peoples-crud
```

### 2. Configurar Variáveis de Ambiente
```bash
cp .env.example .env
```

### 3. Editar o `.env`
Abra o arquivo `.env` e configure as variáveis conforme necessário:

```
# Configurações do Banco
POSTGRES_PASSWORD=sua_senha_postgres
DATABASE_URL=postgresql://postgres:sua_senha_postgres@postgres:5432/sistema_cadastro

# Configurações JWT
JWT_SECRET_KEY=sua_chave_jwt_segura

# Configurações do Admin (opcional)
ADMIN_USERNAME=seunome
ADMIN_PASSWORD=sua_senha_admin
ADMIN_EMAIL=seu_email@exemplo.com
```

### 4. Iniciar o Projeto

#### Usando Make (Recomendado)
```bash
make up
```

#### Ou com Docker Compose Diretamente
```bash
docker compose -f config/docker-compose.yml --env-file .env up -d --build
```

## Acessar a Aplicação

- **Frontend**: http://localhost:5173
- **Backend**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

## Parar o Projeto

#### Usando Make
```bash
make down
```

#### Ou com Docker Compose
```bash
docker compose -f config/docker-compose.yml down
```

## Dicas Importantes

- Sempre use o `.env.example` como referência
- Não commite seu `.env` para o repositório
- As senhas padrão são fracas, então sempre personalize
- A primeira inicialização pode levar alguns minutos para baixar as imagens e configurar

## Credenciais Padrão

Se não configurar no `.env`, use:
- **Usuário**: admin
- **Senha**: admin
- **Email**: admin@example.com

## Tecnologias Utilizadas

- **Frontend**: React
- **Backend**: FastAPI
- **Banco de Dados**: PostgreSQL
- **Autenticação**: JWT
- **Containerização**: Docker

## Contribuição

[Especifica como contribuir]

## Licença

[Especificar a licença do projeto]
