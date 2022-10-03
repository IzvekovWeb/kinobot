import psycopg2

from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from db.queries.create_tables import create_users, create_films, create_films_collection
from bot.config import db_creds


class DataBase:

    def __init__(self):
        self.conn, self.cursor = self.connect()

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
            return connection, cursor
        except (Exception, Error) as e:
            print("Ошибка при работе с PostgreSQL", e)

    def create_tables(self):
        try:
            # self.cursor.execute(create_users)
            # self.cursor.execute(create_films)
            self.cursor.execute(create_films_collection)
        except (Exception, Error) as e:
            print("Ошибка при создании таблицы в БД", e)

    def __del__(self):
        if self.cursor:
            self.cursor.close()
            self.conn.close()
            print("Соединение с PostgreSQL закрыто")


if __name__ == '__main__':
    db = DataBase()
    db.create_tables()
