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
    reg_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        reg_time = self.reg_at.strftime("%Y-%m-%d %H:%M")
        return f"<ID='{self.user_id}', Имя='{self.name}', Фамилия='{self.surname}', лет='{self.ege}', дата регистрации='{reg_time}'/>"
