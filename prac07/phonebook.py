import psycopg2

conn = psycopg2.connect(
    host="localhost",
    dbname="phonebook_db",
    user="postgres",
    password="12345678",
    port="5432"
)

cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) NOT NULL,
        phone VARCHAR(20) NOT NULL
    )
""")
conn.commit()

name = input("Enter name: ")
phone = input("Enter phone: ")

cur.execute(
    "INSERT INTO phonebook (username, phone) VALUES (%s, %s)",
    (name, phone)
)
conn.commit()

cur.execute("SELECT * FROM phonebook")
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()