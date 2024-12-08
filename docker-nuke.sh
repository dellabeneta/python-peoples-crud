#!/bin/bash

# Script para limpar todos os recursos do Docker
echo "Limpando todos os recursos do Docker..."

# Parar todos os containers em execução
echo "Parando todos os containers..."
docker ps -q | xargs -r docker stop

# Remover todos os containers
echo "Removendo todos os containers..."
docker ps -aq | xargs -r docker rm -f

# Remover todos os volumes
echo "Removendo todos os volumes..."
docker volume ls -q | xargs -r docker volume rm

# Remover todas as redes personalizadas (exceto padrão)
echo "Removendo todas as redes personalizadas..."
docker network ls -q | grep -v "^\(bridge\|host\|none\)$" | xargs -r docker network rm

# Remover todas as imagens
echo "Removendo todas as imagens..."
docker images -q | xargs -r docker rmi -f

# Limpar todos os caches e dados não utilizados
echo "Executando docker system prune --all --force..."
docker system prune --all --force --volumes

echo "Limpeza completa do Docker realizada!"
