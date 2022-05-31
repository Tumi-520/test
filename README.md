# Project template for FastAPI

## Quick Guide

1. Install dependencies use `pip install -r requirements.txt`
2. Run server use `python main.py`

You should see following contents in console:

```shell
INFO: Started server process [26980]
INFO: Waiting for application startup.
INFO: Application startup complete.
INFO: Uvicorn running on http://127.0.0.1:8005 (Press CTRL+C to quit)
```

Open your browser, then access [http://127.0.0.1:8005/api/v1/docs/swagger](http://127.0.0.1:8005/api/v1/docs/swagger) to
visit your Swagger docs site

You can also access [http://127.0.0.1:8005/api/v1/docs/redoc](http://127.0.0.1:8005/api/v1/docs/redoc) to see ReDoc docs
site

## Configuration

### Intro

Along with this template, you will have the following features:

- Connect to SQL (Relational) Databases (by SQLAlchemy)
- User authentication and authorization based on OAuth2 and JWT, using bcrypt for encryption
- Symmetric encryption (by cryptography)
- Password hashing (by passlib, bcrypt)

Related packages as below:

```shell
pip install fastapi                     # FastAPI
pip install "uvicorn[standard]"         # ASGI Server
pip install python-multipart            # FormData analyze
pip install SQLAlchemy                  # ORM
pip install "python-jose[cryptography]" # JWT & Symmetric encryption
pip install "passlib[bcrypt]"           # Password hash
```

For convenience, I'll use `/` for project's root dictionary.

### Config File

This template is using [uvicorn](https://www.uvicorn.org/) as ASGI server

- Server port/Listen address config available in `/main.py`
- CORS feature is available in `/app/main.py`
- Database type & url is set in `/app/core/config.py`
- API node specific setting is in `app/api/<API_NODE>/init.py` (including docs setting & error catch)

### Database

Default ORM is SQLAlchemy, default config is use sqlite database.

if you use MySQL/MariaDB, choose one of these Drivers below:

```shell
pip install PyMySQL # If use “sha256_password” or “caching_sha2_password” for authenticate, Use `pip install PyMySQL[rsa]`
pip install mysql-connector-python # use MySQL-Connector
```

After install driver, open `/app/core/config.py`, change `DB_TYPE` to `mysql`. Then uncomment correct `DB_URL` in config

### User Authentication

open `/app/core/config.py`, change `JWT_SECRET` to your own secret.

### Documentation & Contribution

- FastAPI - [Visit WebSite](https://fastapi.tiangolo.com/)
- Uvicorn - [Visit WebSite](https://www.uvicorn.org/)
- Starlette - [Visit WebSite](https://www.starlette.io/)
- pydantic - [Visit WebSite](https://pydantic-docs.helpmanual.io/)
- SQLAlchemy - [Visit WebSite](https://www.sqlalchemy.org/)
- PyMySQL - [Visit WebSite](https://pymysql.readthedocs.io/en/latest/index.html)
- MySQL Connector - [Visit WebSite](https://dev.mysql.com/doc/relnotes/connector-python/en/)
- python-multipart - [Visit WebSite](https://andrew-d.github.io/python-multipart/index.html)
- python-jose - [Visit WebSite](https://github.com/mpdavis/python-jose)
- Cryptography - [Visit WebSite](https://cryptography.io/en/latest/)
- PassLib - [Visit WebSite](https://passlib.readthedocs.io/en/stable/)
- bcrypt - [Visit WebSite](https://github.com/pyca/bcrypt/)
