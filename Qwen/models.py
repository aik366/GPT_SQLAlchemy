from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    ege = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<ID='{self.user_id}', Имя='{self.name}', Фамилия='{self.surname}', лет='{self.ege}'>"
