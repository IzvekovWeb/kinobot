import psycopg2

from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from queries.create_tables import create_users, create_films, create_user_films
from bot.config import db_creds


class DataBase:

    def __init__(self):
        self.__cursor = self.connect()

    @classmethod
    def connect(cls):
        try:
            connection = psycopg2.connect(
                user=db_creds['user'],
                password=db_creds['password'],
                host=db_creds['host'],
                port=db_creds['port']
            )
            connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

            # Курсор для выполнения операций с базой данных
            cursor = connection.cursor()
            print("Соединение с PostgreSQL открыто")
            return cursor
        except (Exception, Error) as e:
            print("Ошибка при работе с PostgreSQL", e)

    def create_tables(self):
        try:
            self.__cursor.execute(create_users)
            self.__cursor.execute(create_films)
            self.__cursor.execute(create_user_films)
        except (Exception, Error) as e:
            print("Ошибка при создании таблицы в БД", e)

    def __del__(self):
        if self.__cursor:
            self.__cursor.close()
            print("Соединение с PostgreSQL закрыто")


if __name__ == '__main__':
    db = DataBase()
    db.create_tables()
