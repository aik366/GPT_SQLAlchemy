from database import engine, get_session
from models import Base, User

# Создаём таблицы (если не существуют)
Base.metadata.create_all(bind=engine)

# Работаем с данными
session = get_session()


def add_user(name, surname, ege=18):
    try:
        user = session.query(User).filter(User.name == name, User.surname == surname, User.ege == ege).first()
        if not user:
            new_item = User(name=name, surname=surname, ege=ege)
            session.add(new_item)
            session.commit()
            print("Создан:", new_item)
        else:
            print(f"Пользователь {name} {surname} уже существует")

    finally:
        session.close()


def del_user(name, surname):
    try:
        user = session.query(User).filter(User.name == name, User.surname == surname).first()
        if user:
            session.delete(user)
            session.commit()
            print(f"Пользователь {name} {surname} удалён")
        else:
            print(f"Пользователь {name} {surname} не найден")
    finally:
        session.close()


def update_user(name, surname, ege):
    try:
        user = session.query(User).filter(User.name == name, User.surname == surname).first()
        if user:
            user.ege = ege
            session.commit()
            print(f"Пользователь {name} {surname} обновлён")
    finally:
        session.close()


def all_view():
    try:
        # Читаем все
        users = session.query(User).all()
        print("Все записи:", users)
    finally:
        session.close()


if __name__ == "__main__":
    add_user("Айк", "Галстян", 54)
    update_user("Айк", "Галстян", 53)
    # del_user("Айк", "Галстян")
    all_view()
