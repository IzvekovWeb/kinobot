from psycopg2 import Error

from db.DataBase import DataBase


class User:
    def __init__(self, user_id, user_name='', chat_id=None):
        self.id = user_id
        self.name = user_name
        self.chat_id = chat_id

    def is_exist(self):
        db = DataBase()
        try:
            db.cursor.execute("SELECT COUNT(*) as c FROM kb_users WHERE user_id=%s", (self.id, ))
            result = db.cursor.fetchone()[0]

            if result > 0:
                return True

        except (Exception, Error) as e:
            print(f"Ошибка в ходе поиска пользователя: {e}")
        return False

    def add(self):
        db = DataBase()

        # if self.is_exist():
        #     print('Пользователь уже есть в базе')
        #     return

        try:
            db.cursor.execute("INSERT INTO kb_users "
                              "(user_id, chat_id, user_name) "
                              "VALUES (%s, %s, %s) ON CONFLICT DO NOTHING",
                              (self.id, self.chat_id, self.name))
        except (Exception, Error) as e:
            print(f"Ошибка в ходе добавления пользователя: {e}")

    @classmethod
    def get_all(cls):
        db = DataBase()

        try:
            db.cursor.execute("SELECT * FROM kb_users")
        except (Exception, Error) as e:
            print(f"Ошибка в ходе получения данных: {e}")
            return []

        result = db.cursor.fetchall()
        return result

    def get_by_id(self, user_id=None):
        if not user_id:
            user_id = self.id

        db = DataBase()
        try:
            db.cursor.execute("SELECT * FROM kb_users "
                              "WHERE user_id = %s", (user_id, ))
        except (Exception, Error) as e:
            print(f"Ошибка в ходе получения данных: {e}")
            return []

        result = db.cursor.fetchall()
        return result

    def update(self, new_name, new_chat_id=None):

        db = DataBase()

        try:
            db.cursor.execute("SELECT user_name, chat_id FROM kb_users WHERE user_id = %s", (self.id, ))
        except (Exception, Error) as e:
            print(f"Ошибка в ходе получения данных: {e}")

        user_ = db.cursor.fetchone()

        current_chat_id = None
        if user_:
            current_chat_id = user_[1]
        if new_chat_id is None and current_chat_id is None:
            new_chat_id = self.chat_id

        try:
            db.cursor.execute("UPDATE kb_users "
                              "SET user_name=%(new_name)s, chat_id=%(new_chat_id)s "
                              "WHERE user_id=%(user_id)s ",
                              {"user_id": self.id, "new_name": new_name, "new_chat_id": new_chat_id})
        except (Exception, Error) as e:
            print(f"Ошибка в ходе обновления данных: {e}")

    def delete(self):
        db = DataBase()
        try:
            db.cursor.execute("DELETE FROM kb_users WHERE user_id = %s", (self.id, ))
        except (Exception, Error) as e:
            print(f"Ошибка в ходе удаления пользователя: {e}")


if __name__ == '__main__':
    a = User(445743340, 'Izvekov_Alex', 445743340)
    a.is_exist()