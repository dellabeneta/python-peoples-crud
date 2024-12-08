#!/bin/bash

set -e  # Exit on error

echo "Starting initialization script..."

# Esperar pelo PostgreSQL
echo "Waiting for PostgreSQL..."
python scripts/wait-for-postgres.py
if [ $? -ne 0 ]; then
    echo "Failed to connect to PostgreSQL"
    exit 1
fi
echo "PostgreSQL is ready!"

# Criar usuário admin
echo "Creating admin user..."
python scripts/create_admin_simple.py
if [ $? -ne 0 ]; then
    echo "Failed to create admin user"
    exit 1
fi
echo "Admin user created successfully!"

# Popular com 200 fakes de pessoas
echo "Creating fake pessoas..."
python scripts/create_fake_pessoas.py
if [ $? -ne 0 ]; then
    echo "Failed to create fake pessoas"
    exit 1
fi
echo "Fake pessoas created successfully!"

# Iniciar o servidor
echo "Starting Uvicorn server..."
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
