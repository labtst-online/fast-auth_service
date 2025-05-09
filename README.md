# Auth Service

The Auth Service is responsible for user authentication and issuing JWT tokens. It is part of the FastAPI app.

## Tech Stack

- **FastAPI** – Web framework
- **PostgreSQL** – Relational database
- **Docker** – Containerization
- **GitHub Actions** – Continuous Integration and Continuous Delivery
- **Pytest** – Test framework

## API Endpoints

- `POST /auth/jwt/login` – Authenticate user and issue JWT token
- `POST /auth/register` – Register a new user
- `POST /auth/jwt/logout` – Logout user (invalidate token)
- `POST /auth/forgot-password` – Request password reset
- `POST /auth/reset-password` – Reset password with token
- `POST /auth/request-verify-token` – Request email verification
- `POST /auth/verify` – Verify email with token
- `GET /users/me` – Get current user info
- `GET /users/{id}` – Get user info by id

## Getting Started

> This service is a core part of the FastAPI backend. It is recommended to run the full system using [`fast-deployment`](https://github.com/labtst-online/fast-deployment.git).

### 1. Clone repository

```bash
git clone https://github.com/labtst-online/fast-auth_service.git
cd fast-auth_service
```

### 2. Configure

```bash
cp .env.sample .env
```
> Change variables before docker-compose up

### 3. Run with Docker

```bash
docker-compose up --build
```

## Testing

```bash
pytest
```

## GitHub Actions (CI, CD)

* Continuous Integration workflow runs tests and ruff formater check on every push and pull request to the main and develop branches.
* Continuous Delivery workflow build and push image to GHCR.

## License

This repository is licensed under the terms of the MIT license.
