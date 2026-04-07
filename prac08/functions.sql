CREATE TABLE IF NOT EXISTS phonebook (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL UNIQUE
);

-- 1.search by pattern
-- Поиск по username или phone
CREATE OR REPLACE FUNCTION search_phonebook(p_pattern TEXT)
RETURNS TABLE (
    id INT,
    username VARCHAR,
    phone VARCHAR
)
AS $$
BEGIN
    RETURN QUERY
    SELECT pb.id, pb.username, pb.phone
    FROM phonebook pb
    WHERE pb.username ILIKE '%' || p_pattern || '%'
       OR pb.phone ILIKE '%' || p_pattern || '%'
    ORDER BY pb.id;
END;
$$ LANGUAGE plpgsql;


-- 2.pagination
CREATE OR REPLACE FUNCTION get_phonebook_paginated(p_limit INT, p_offset INT)
RETURNS TABLE (
    id INT,
    username VARCHAR,
    phone VARCHAR
)
AS $$
BEGIN
    RETURN QUERY
    SELECT pb.id, pb.username, pb.phone
    FROM phonebook pb
    ORDER BY pb.id
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;