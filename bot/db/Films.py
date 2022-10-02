from psycopg2 import Error

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


if __name__ == '__main__':
    film = Film(1)
    # film.add()
    # film.update('Санктум', new_rating=7.7)
    # film.delete()
