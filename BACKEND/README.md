# Domicare Backend

Django backend application built with Clean Architecture and CQRS pattern.

## Architecture

This project follows **Clean Architecture** principles with **CQRS** (Command Query Responsibility Segregation) pattern:

- **Domain Layer**: Business entities, value objects, and domain logic
- **Application Layer**: Use cases, commands, queries, and handlers
- **Infrastructure Layer**: Data persistence, external services, and frameworks
- **Presentation Layer**: API controllers and serializers

## Project Structure

```
BACKEND/
├── src/
│   ├── Domicare.API/          # Presentation Layer
│   ├── Domicare.Application/  # Application Layer (CQRS)
│   ├── Domicare.Domain/       # Domain Layer
│   └── Domicare.Infrastructure/ # Infrastructure Layer
├── config/                     # Django configuration
├── tests/                      # Test suites
├── docs/                       # Documentation
├── docker/                     # Docker configuration
├── scripts/                    # Utility scripts
└── requirements/              # Python dependencies
```

## Getting Started

### Prerequisites

- Python 3.11+
- PostgreSQL 15+
- Redis 7+

### Installation

1. Clone the repository
2. Create virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements/development.txt
   ```

4. Create `.env` file:
   ```bash
   cp .env.example .env
   # Update .env with your configuration
   ```

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Run development server:
   ```bash
   python manage.py runserver
   ```

### Using Docker

```bash
cd docker
docker-compose -f docker-compose.dev.yml up
```

## API Documentation

Once the server is running, visit:
- Swagger UI: http://localhost:8000/api/docs/
- API Schema: http://localhost:8000/api/schema/

## Testing

Run tests:
```bash
pytest
```

With coverage:
```bash
pytest --cov=src
```

## Key Features

- Clean Architecture with CQRS
- Domain-Driven Design
- Repository Pattern
- Event-Driven Architecture
- JWT Authentication
- Google OAuth Integration
- VNPay Payment Gateway
- Email Service
- File Storage (Cloudinary)
- Redis Caching
- API Documentation (Swagger)

## License

MIT
