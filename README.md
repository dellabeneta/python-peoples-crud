## Status do Projeto

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/dellabeneta/python-peoples-crud/build-and-push.yml?label=Build)
[![Trivy Scan](https://github.com/dellabeneta/python-peoples-crud/actions/workflows/trivy-scan.yml/badge.svg)](https://github.com/dellabeneta/python-peoples-crud/actions/workflows/trivy-scan.yml)
![GitHub top language](https://img.shields.io/github/languages/top/dellabeneta/python-peoples-crud)


![Docker Pulls](https://img.shields.io/docker/pulls/dellabeneta/python-peoples-crud-backend)
![Docker Image Version](https://img.shields.io/docker/v/dellabeneta/python-peoples-crud-backend/latest)
![Terraform Version](https://img.shields.io/badge/Terraform-v1.10.1-blue)

![GitHub License](https://img.shields.io/github/license/dellabeneta/python-peoples-crud)

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
git clone https://github.com/dellabeneta/python-peoples-crud.git
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

## Tree do Projeto, diretórios e aquivos:

```
della@fedora:~/projetos$ tree
.
└── python-peoples-crud
    ├── backend
    │   ├── app
    │   │   ├── core
    │   │   │   ├── auth.py
    │   │   │   ├── database.py
    │   │   │   └── __pycache__
    │   │   │       ├── auth.cpython-311.pyc
    │   │   │       └── database.cpython-311.pyc
    │   │   ├── main.py
    │   │   ├── models
    │   │   │   ├── pessoa.py
    │   │   │   ├── __pycache__
    │   │   │   │   ├── pessoa.cpython-311.pyc
    │   │   │   │   └── user.cpython-311.pyc
    │   │   │   └── user.py
    │   │   ├── __pycache__
    │   │   │   └── main.cpython-311.pyc
    │   │   ├── routes
    │   │   │   ├── auth.py
    │   │   │   ├── pessoa.py
    │   │   │   └── __pycache__
    │   │   │       ├── auth.cpython-311.pyc
    │   │   │       └── pessoa.cpython-311.pyc
    │   │   └── schemas
    │   │       ├── pagination.py
    │   │       ├── pessoa.py
    │   │       ├── __pycache__
    │   │       │   ├── pagination.cpython-311.pyc
    │   │       │   ├── pessoa.cpython-311.pyc
    │   │       │   └── user.cpython-311.pyc
    │   │       └── user.py
    │   ├── Dockerfile
    │   ├── entrypoint.sh
    │   ├── requirements.txt
    │   ├── scripts
    │   │   ├── create_admin_simple.py
    │   │   ├── create_fake_pessoas.py
    │   │   ├── init.sh
    │   │   ├── verify_admin.py
    │   │   └── wait-for-postgres.py
    │   └── tests
    ├── docker-compose.yml
    ├── docker-nuke.sh
    ├── frontend
    │   ├── Dockerfile
    │   ├── eslint.config.js
    │   ├── index.html
    │   ├── node_modules
    │   ├── package.json
    │   ├── package-lock.json
    │   ├── public
    │   │   └── vite.svg
    │   ├── src
    │   │   ├── App.jsx
    │   │   ├── components
    │   │   │   ├── Header.jsx
    │   │   │   ├── PrivateRoute.jsx
    │   │   │   └── ThemeToggle.jsx
    │   │   ├── contexts
    │   │   │   └── AuthContext.jsx
    │   │   ├── main.jsx
    │   │   ├── pages
    │   │   │   ├── CadastrarPessoa.jsx
    │   │   │   ├── EditarPessoa.jsx
    │   │   │   ├── ListaPessoas.jsx
    │   │   │   └── Login.jsx
    │   │   └── services
    │   │       └── api.js
    │   └── vite.config.js
    ├── LICENSE
    ├── Makefile
    ├── notas
    ├── README.md
    ├── scripts
    │   └── environment.sh
    └── terraform
        ├── backend.tf
        ├── database-cluster.tf.disabled
        ├── droplet.tf
        ├── networking.tf
        ├── outputs.tf
        ├── provider.tf
        └── ssh-key.tf

25 directories, 60 files
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir um pull request ou relatar problemas.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## FAQ
- **Como posso contribuir?**
  - Sinta-se à vontade para abrir um pull request com suas alterações ou sugestões.

- **Onde posso encontrar mais informações?**
  - Consulte a documentação do projeto ou entre em contato.

## Roadmap
- Adicionar mais funcionalidades de autenticação.
- Melhorar a interface do usuário.
- Implementar testes automatizados.
