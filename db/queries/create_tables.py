create_users = """DROP TABLE IF EXISTS kb_users CASCADE;
                CREATE TABLE IF NOT EXISTS kb_users (
                    id          SERIAL,
                    user_id     int PRIMARY KEY NOT NULL UNIQUE,
                    chat_id     int,
                    user_name   varchar(100),
                    created_at  timestamp DEFAULT current_timestamp
                );"""
create_films = """DROP TABLE IF EXISTS kb_films CASCADE;
                CREATE TABLE IF NOT EXISTS kb_films (
                    id          SERIAL,
                    film_id     int PRIMARY KEY NOT NULL UNIQUE,
                    film_name   varchar(255),
                    rating      REAL
                );"""
create_films_collection = """DROP TABLE IF EXISTS kb_films_collection CASCADE;
                CREATE TABLE IF NOT EXISTS kb_films_collection (
                    id          SERIAL,
                    film_id     int NOT NULL REFERENCES kb_films (film_id) ON DELETE CASCADE,
                    user_id     int REFERENCES kb_users (user_id) ON DELETE CASCADE,
                    is_favorite boolean DEFAULT false NOT NULL,
                    CONSTRAINT unique_pair UNIQUE (film_id, user_id)
                );"""
