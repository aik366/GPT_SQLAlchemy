from database import engine, get_session
from models import Base, User
from random import randint

# Создаём таблицы (если не существуют)
Base.metadata.create_all(bind=engine)


def add_user(name, surname, ege=18):
    session = get_session()
    user_id = randint(1000000, 9999999)
    try:
        user = User(user_id=user_id, name=name, surname=surname, ege=ege)
        session.add(user)
        session.commit()
        session.refresh(user)
        print(f"✅ Пользователь добавлен: ", user)  
    finally:
        session.close()


def del_user(user_id):
    session = get_session()
    try:
        user = session.query(User).filter(User.user_id == user_id).first()
        if user:
            session.delete(user)
            session.commit()
            print(f"🗑️ Пользователь {user.name} {user.surname} удалён")
        else:
            print(f"⚠️ Пользователь с ID {user_id} не найден")
    finally:
        session.close()


def update_user(user_id, name, surname, ege=26):
    session = get_session()
    try:
        user = session.query(User).filter(User.user_id == user_id).first()
        if user:
            user.ege = ege
            session.commit()
            session.refresh(user)
            print(f"Пользователь {name} {surname} обновлён")
        else:
            print(f"⚠️ Пользователь с ID {user_id} не найден")
    finally:
        session.close()


def view_all():
    """Показать всех пользователей"""
    session = get_session()
    try:
        users = session.query(User).all()
        if not users:
            print("📭 Нет пользователей в базе")
        else:
            print("📋 Все пользователи:")
            for user in users:
                reg_time = user.reg_at.strftime("%Y-%m-%d %H:%M:%S")
                print(f"ID: {user.user_id} | {user.name} {user.surname} ({user.ege}) | Зарегистрирован: {reg_time}")
        return users
    finally:
        session.close()


if __name__ == "__main__":
    # add_user("Тигран", "Галстян")
    # update_user("Айк", "Галстян", 53)
    del_user(7486894)
    view_all()
