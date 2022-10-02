from psycopg2 import Error
from psycopg2.errors import ForeignKeyViolation, UniqueViolation

from DataBase import DataBase


class Film:
    def __init__(self, film_id: int, film_name: str = '', rating: float = -1):
        self.id = film_id
        self.name = film_name
        self.rating = rating

    def add(self):
        db = DataBase()
        try:
            db.cursor.execute("INSERT INTO kb_films "
                              "(film_id, film_name, rating) "
                              "VALUES (%s, %s, %s) ON CONFLICT DO NOTHING",
                              (self.id, self.name, self.rating))
        except (Exception, Error) as e:
            print(f"Ошибка в ходе добавления фильма: {e}")

    @classmethod
    def get_all(cls):
        db = DataBase()

        try:
            db.cursor.execute("SELECT * FROM kb_films")
        except (Exception, Error) as e:
            print(f"Ошибка в ходе получения данных: {e}")
            return []

        result = db.cursor.fetchall()
        return result

    @classmethod
    def get_by_id(cls, film_id):

        db = DataBase()
        try:
            db.cursor.execute("SELECT * FROM kb_films "
                              "WHERE film_id = %s", (film_id, ))
        except (Exception, Error) as e:
            print(f"Ошибка в ходе получения данных: {e}")
            return []

        result = db.cursor.fetchall()
        return result

    def get(self):

        db = DataBase()
        try:
            db.cursor.execute("SELECT * FROM kb_films "
                              "WHERE film_id = %s", (self.id, ))
        except (Exception, Error) as e:
            print(f"Ошибка в ходе получения данных: {e}")
            return []

        result = db.cursor.fetchall()
        return result

    def update(self, new_name, new_rating):

        db = DataBase()

        try:
            db.cursor.execute("UPDATE kb_films "
                              "SET film_name=%(new_name)s, rating=%(new_rating)s "
                              "WHERE film_id=%(film_id)s ",
                              {"film_id": self.id, "new_name": new_name, "new_rating": new_rating})
        except (Exception, Error) as e:
            print(f"Ошибка в ходе обновления данных фильма: {e}")

    def delete(self):
        db = DataBase()
        try:
            db.cursor.execute("DELETE FROM kb_films WHERE film_id = %s", (self.id, ))
        except (Exception, Error) as e:
            print(f"Ошибка в ходе удаления пользователя: {e}")

    def add_to_collection(self, user_id: int, is_favorite=False):
        db = DataBase()

        try:
            with db.conn:
                db.cursor.execute("INSERT INTO kb_films_collection "
                                  "(user_id, film_id, is_favorite) "
                                  "VALUES (%s, %s, %s)",
                                  (user_id, self.id, is_favorite))
        except (ForeignKeyViolation, UniqueViolation) as e:
            print(e)
        except (Exception, Error) as e:
            print(f"Ошибка в ходе добавления данных: {e}")

    @classmethod
    def add_to_collection_by_id(cls, film_id: int, user_id: int, is_favorite=False):
        db = DataBase()

        try:
            with db.conn:
                db.cursor.execute("INSERT INTO kb_films_collection "
                                  "(user_id, film_id, is_favorite) "
                                  "VALUES (%s, %s, %s)",
                                  (user_id, film_id, is_favorite))
        except (ForeignKeyViolation, UniqueViolation) as e:
            print(e)
        except (Exception, Error) as e:
            print(f"Ошибка в ходе добавления данных: {e}")

    @classmethod
    def set_favorite(cls, film_id, user_id, is_favorite=True):
        db = DataBase()

        try:
            db.cursor.execute("UPDATE kb_films_collection "
                              "SET is_favorite=%s "
                              "WHERE user_id=%s AND film_id=%s",
                              (is_favorite, user_id, film_id))
        except (Exception, Error) as e:
            print(f"Ошибка в ходе обновления данных: {e}")
