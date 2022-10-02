import psycopg2
import config

from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

creds = config.db_creds


class DataBase:

    def __init__(self):
        self.cursor = self.connect()

    @classmethod
    def connect(cls) -> object | None:
        connection = None
        try:
            connection = psycopg2.connect(
                user=creds['user'],
                password=creds['password'],
                host=creds['host'],
                port=creds['port']
            )
            connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

            # Курсор для выполнения операций с базой данных
            cursor = connection.cursor()
            return cursor
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        finally:
            if connection:
                print(123)
                cursor.close()
                connection.close()
                print("Соединение с PostgreSQL закрыто")

    def create_tables(self):
        pass
