-- 1.insert new user,if exists update phone
CREATE OR REPLACE PROCEDURE upsert_user(p_username VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (
        SELECT 1
        FROM phonebook
        WHERE username = p_username
    ) THEN
        UPDATE phonebook
        SET phone = p_phone
        WHERE username = p_username;
    ELSE
        INSERT INTO phonebook(username, phone)
        VALUES (p_username, p_phone);
    END IF;
END;
$$;

-- 2.insert many users with validation
CREATE OR REPLACE PROCEDURE insert_many_users(
    p_usernames VARCHAR[],
    p_phones VARCHAR[]
)
LANGUAGE plpgsql
AS $$
DECLARE
    i INT;
BEGIN
    FOR i IN 1 .. array_length(p_usernames, 1)
    LOOP
        IF p_phones[i] ~ '^\+?[0-9]{10,15}$' THEN
            IF EXISTS (
                SELECT 1 FROM phonebook WHERE username = p_usernames[i]
            ) THEN
                UPDATE phonebook
                SET phone = p_phones[i]
                WHERE username = p_usernames[i];
            ELSE
                BEGIN
                    INSERT INTO phonebook(username, phone)
                    VALUES (p_usernames[i], p_phones[i]);
                EXCEPTION
                    WHEN unique_violation THEN
                        INSERT INTO incorrect_data(username, phone)
                        VALUES (p_usernames[i], p_phones[i]);
                END;
            END IF;
        ELSE
            INSERT INTO incorrect_data(username, phone)
            VALUES (p_usernames[i], p_phones[i]);
        END IF;
    END LOOP;
END;
$$;


-- 3.delete by username or by phone
CREATE OR REPLACE PROCEDURE delete_user(p_value VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM phonebook
    WHERE username = p_value
       OR phone = p_value;
END;
$$;