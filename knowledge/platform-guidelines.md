# Гайдлайны платформы

## Общие принципы

1. Cloud Native подход
2. Контейнеризация (Docker)
3. CI/CD автоматизация
4. Infrastructure as Code

## Технологический стек

### Backend

- Strapi v4 (Node.js 16+)
- API Gateway (Python 3.9+ с FastAPI и Celery)
- Website Backend (PHP 8.x с Laravel 9+)
- PostgreSQL (центральная и site база)
- Elasticsearch (поисковый движок)

### Frontend

- React 18+
- TypeScript
- Material UI
- Redux Toolkit

### DevOps

- Docker
- Terraform (Infrastructure as Code)
- Ansible (управление конфигурацией и деплой)
- GitLab CI (сборка и тесты)
- Prometheus + Grafana (мониторинг)
- Loki (логирование)

## Требования к разработке

### Качество кода

- Code Review
- Conventional Commits

### Мониторинг

- Health Checks
- Metrics Collection
- Distributed Tracing
- Error Tracking

## Процессы разработки

1. Feature Branch Workflow
2. Trunk Based Development
3. Continuous Deployment
