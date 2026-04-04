# Erebus

Starter full-stack web application.

## Stack
- PostgreSQL
- FastAPI
- React + Vite + TypeScript
- Docker Compose

## Features in this scaffold
- Login page
- Register page
- Welcome page
- EN / PL language switch
- Shared app shell with burger menu and profile icon
- Users, property types, and user settings API endpoints
- Database models for users, property types, user settings, sessions, password reset, email verification, and audit log

## Run with Docker
```bash
cp .env.example .env
docker compose up --build
```

Frontend: `http://localhost:3000`

Backend: `http://localhost:8000`

API docs: `http://localhost:8000/docs`

## Backend init
On first run, tables are created automatically.

## Next recommended steps
- Add Alembic migrations
- Add refresh token flow with HttpOnly cookies
- Add email verification flow
- Add admin-only CRUD permissions
- Add tests
- Add CI
