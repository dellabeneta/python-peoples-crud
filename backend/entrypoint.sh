#!/bin/bash
set -e

# Esperar pelo PostgreSQL
python scripts/wait-for-postgres.py

# Criar usuário admin
python scripts/create_admin_simple.py

# Executar o script de inicialização original
./scripts/init.sh
