from connect import get_connection

def create_table():
    query = """
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        username VARCHAR(100) NOT NULL,
        phone VARCHAR(20) NOT NULL UNIQUE
    );
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query)
    print("Table is ready!")


def run_sql_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        sql = f.read()

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
    print(f"{filename} executed successfully.")


def search_by_pattern():
    pattern = input("Enter pattern: ")

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM search_phonebook(%s);", (pattern,))
            rows = cur.fetchall()

    if rows:
        print("\nSearch results:")
        for row in rows:
            print(row)
    else:
        print("No matching records found.")


def upsert_user():
    username = input("Enter username: ")
    phone = input("Enter phone: ")

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL upsert_user(%s, %s);", (username, phone))

    print("User inserted / updated successfully.")


def insert_many_users():
    n = int(input("How many users do you want to insert? "))

    usernames = []
    phones = []

    for i in range(n):
        username = input(f"Enter username #{i+1}: ")
        phone = input(f"Enter phone #{i+1}: ")
        usernames.append(username)
        phones.append(phone)

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL insert_many_users(%s, %s);", (usernames, phones))
            cur.execute("SELECT * FROM incorrect_data;")
            incorrect_rows = cur.fetchall()

    print("Bulk insert finished.")
    if incorrect_rows:
        print("\nIncorrect data:")
        for row in incorrect_rows:
            print(row)
    else:
        print("All data inserted correctly.")


def show_paginated():
    limit = int(input("Enter LIMIT: "))
    offset = int(input("Enter OFFSET: "))

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM get_phonebook_paginated(%s, %s);", (limit, offset))
            rows = cur.fetchall()

    if rows:
        print("\nPaginated results:")
        for row in rows:
            print(row)
    else:
        print("No data found.")


def delete_user():
    value = input("Enter username or phone to delete: ")

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL delete_user(%s);", (value,))

    print("User deleted if existed.")


def show_all():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM phonebook ORDER BY id;")
            rows = cur.fetchall()

    if rows:
        print("\nAll contacts:")
        for row in rows:
            print(row)
    else:
        print("Phonebook is empty.")


def menu():
    while True:
        print("""
1. Create table
2. Execute functions.sql
3. Execute procedures.sql
4. Search by pattern
5. Insert / Update user
6. Insert many users
7. Show paginated data
8. Delete user
9. Show all contacts
0. Exit
        """)

        choice = input("Choose an option: ")

        if choice == "1":
            create_table()
        elif choice == "2":
            run_sql_file("functions.sql")
        elif choice == "3":
            run_sql_file("procedures.sql")
        elif choice == "4":
            search_by_pattern()
        elif choice == "5":
            upsert_user()
        elif choice == "6":
            insert_many_users()
        elif choice == "7":
            show_paginated()
        elif choice == "8":
            delete_user()
        elif choice == "9":
            show_all()
        elif choice == "0":
            print("Bye!")
            break
        else:
            print("Invalid command")


if __name__ == "__main__":
    menu()