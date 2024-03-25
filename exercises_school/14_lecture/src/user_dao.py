from src.database_singleton import DatabaseConnection
from src.user import User


class UserDAO:
    def __init__(self):
        self.connection = DatabaseConnection().get_connection()

    def create(self, user: User):
        cursor = self.connection.cursor()
        sql = 'INSERT INTO user (username, favorite_number, favorite_color) VALUES (%s, %s, %s)'
        cursor.execute(sql, (user.username, user.favorite_number, user.favorite_color))
        self.connection.commit()
        cursor.close()

    def update(self, user: User):
        cursor = self.connection.cursor()
        sql = 'UPDATE user SET favorite_color = %s SET favorite_number = %s WHERE username = %s'f
        cursor.execute(sql, (user.favorite_color, user.username))
        self.connection.commit()
        cursor.close()

    def delete(self, user: User):
        cursor = self.connection.cursor()
        sql = 'DELETE FROM user WHERE username = %s'
        cursor.execute(sql, (user.username,))
        self.connection.commit()
        cursor.close()

    def get_all(self):
        cursor = self.connection.cursor()
        sql = 'SELECT * FROM user'
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result