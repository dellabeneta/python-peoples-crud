#!/bin/bash

# Função para carregar variáveis de ambiente
load_env() {
    if [ -f ".env" ]; then
        set -a
        source .env
        set +a
    else
        echo "Arquivo .env não encontrado. Por favor, copie .env.example para .env e configure suas variáveis."
        exit 1
    fi
}

# Função para mostrar os links dos recursos
show_resources() {
    echo -e "\nRecursos disponíveis:"
    echo -e "Frontend: \033[36mhttp://localhost:5173\033[0m"
    echo -e "Backend: \033[36mhttp://localhost:8000\033[0m"
    echo -e "API Docs: \033[36mhttp://localhost:8000/docs\033[0m"
    echo -e "API Redoc: \033[36mhttp://localhost:8000/redoc\033[0m"
    echo -e "Database: \033[36mlocalhost:5432\033[0m"
}

# Função para iniciar ambiente
start_environment() {
    echo "Starting environment..."
    
    load_env
    
    docker compose -f docker-compose.yml \
                  --env-file .env \
                  up -d --build

    if [ $? -eq 0 ]; then
        echo -e "\n✅ Ambiente iniciado com sucesso!"
        show_resources
    else
        echo -e "\nErro ao iniciar o ambiente"
        exit 1
    fi
}

# Função para parar ambiente
stop_environment() {
    echo "Stopping environment..."
    
    load_env
    
    docker compose -f docker-compose.yml \
                  --env-file .env \
                  down

    if [ $? -eq 0 ]; then
        echo -e "\n✅ Ambiente parado com sucesso!"
    else
        echo -e "\nErro ao parar o ambiente"
        exit 1
    fi
}

# Função principal
main() {
    action=$1

    case $action in
        start)
            start_environment
            ;;
        stop)
            stop_environment
            ;;
        *)
            echo "Usage: $0 <start|stop>"
            exit 1
            ;;
    esac
}

# Executa a função principal com os argumentos passados
main "$@"
