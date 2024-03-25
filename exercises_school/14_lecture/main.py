from src.database_singleton import DatabaseConnection
from src.user import User
from src.user_dao import UserDAO


def main():
    """založí dva uživatele (C) Petru co má rádá modrou a číslo 3 a Viléma co má rád růžovou a číslo 4,
pak jednoho vyhledá (R1) a změňte mu oblíbenou barvu (U) na lososovou,
druhého pak smaže (D)
a nakonec pak vypište všechny uživatele v databázi (R2)."""
    c = User('Petr', 'modrá', 3)
    v = User('Vilém', 'růžová', 4)
    dao = UserDAO()
    dao.create_user(c)
    dao.create_user(v)
    print(dao.read_user_search_by_username('Petr'))
    c.favorite_color = 'lososová'
    dao.update_favorite_color(c)
    dao.delete_user(v)
    print(dao.read_user_get_all())


if __name__ == '__main__':
    main()
