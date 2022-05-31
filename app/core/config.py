import os
from pydantic import BaseSettings


class _Config(BaseSettings):
    # Environment Type
    RUN_TYPE = os.getenv('RUN_TYPE', 'run')

    # Database Config
    DB_TYPE = 'sqlite'  # val: 'sqlite' | 'mysql'
    DB_URL = 'sqlite:///./database.db'
    # if use MySQL(Compatible wirth MariaDB):
    # DB_URL = 'mysql+pymysql://user:password@localhost/dbname?charset=utf8mb4' # Use PyMySQL
    # DB_URL = 'mysql+mysqlconnector://user:password@localhost/dbname?charset=utf8mb4' # Use MySQL-Connector

    # Encryption Config
    DES_SECRET = "Example"
    DES_VECTOR = b"example"
    JWT_ALGORITHM = "HS256"  # JWT Encryption Method
    JWT_SECRET = "ExampleJWTSecret"
    TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # 7 Days
    OAUTH2_TOKEN_URL = "/api/v1/auth/login"  # auth url


config = _Config()
