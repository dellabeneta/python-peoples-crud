.PHONY: up down

# Desenvolvimento
up:
	./scripts/environment.sh start
	trivy image --severity CRITICAL,HIGH --format table python-peoples-crud-backend:latest
	trivy image --severity CRITICAL,HIGH --format table python-peoples-crud-frontend:latest


down:
	./scripts/environment.sh stop