# kinobot


###

Сбросить serial

    ALTER SEQUENCE kb_users_id_seq RESTART WITH 2;
    UPDATE kb_users SET id=nextval('kb_users_id_seq'); 