from sqlalchemy import Column, VARCHAR, Text, Integer
from app.core.database import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(VARCHAR(128), primary_key=True, index=True)
    nickname = Column(VARCHAR(32), default='')
    username = Column(VARCHAR(32), unique=True)
    password = Column(VARCHAR(128))
    permission = Column(Integer, default=1)
