import mysql.connector as mysql
from configparser import ConfigParser


class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is not None:
            return cls._instance

        cls._instance = super(DatabaseConnection, cls).__new__(cls)
        config = ConfigParser()
        config.read('config.ini')

        db_params = {
            'host':     config.get('database', 'host'),
            'user':     config.get('database', 'user'),
            'password': config.get('database', 'password'),
            'database': config.get('database', 'database'),
        }

        cls._instance.connection = mysql.connect(**db_params)
        return cls._instance

    def get_connection(self):
        return self._instance.connection
