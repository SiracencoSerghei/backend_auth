## 1. Створи базу і користувача:

sudo -u postgres psql
CREATE DATABASE fastapi_db;
CREATE USER postgres WITH ENCRYPTED PASSWORD 'postgres';
GRANT ALL PRIVILEGES ON DATABASE fastapi_db TO postgres;
\q

## 2.

* `postgresql://` – драйвер SQLAlchemy для PostgreSQL.
* `postgres:postgres` – `username:password`.
* `localhost:5432` – хост та порт.
* `fastapi_db` – назва бази даних.

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/fastapi_db"

## 3.

```bash
docker-compose up -d
```

## 4.

```
pip freeze > requirements.txt
pip install -r requirements.txt
```
## 5.

```
docker-compose down -v
docker-compose up --build
```
## 5.

```
curl -X POST http://localhost:8000/signup \
-H "Content-Type: application/json" \
-d '{"email":"test@example.com","password":"1234"}'
```