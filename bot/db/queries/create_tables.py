create_users =  """CREATE TABLE IF NOT EXISTS kb_users (
                    id          SERIAL,
                    user_id     int PRIMARY KEY NOT NULL UNIQUE,
                    chat_id     int,
                    user_name   varchar(100)
                );"""
create_films = """CREATE TABLE IF NOT EXISTS kb_films (
                    id          SERIAL,
                    film_id     int PRIMARY KEY NOT NULL UNIQUE,
                    film_name   varchar(255),
                    rating      REAL
                );"""
create_user_films = """CREATE TABLE IF NOT EXISTS kb_user_films (
                    id          SERIAL,
                    film_id     int NOT NULL REFERENCES kb_films (film_id) ON DELETE CASCADE,
                    user_id     int REFERENCES kb_users (user_id) ON DELETE CASCADE,
                    is_favorite boolean DEFAULT false NOT NULL
                );"""
