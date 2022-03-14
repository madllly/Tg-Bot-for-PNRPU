import sqlite3


def create_bd():
    try:
        sqlite_connection = sqlite3.connect('Users.db')
        sqlite_create_table_query = '''CREATE TABLE users (
                                    id INTEGER UNIQUE,
                                    join_group TEXT NOT NULL );'''

        cursor = sqlite_connection.cursor()
        print("База данных подключена к SQLite")
        cursor.execute(sqlite_create_table_query)
        sqlite_connection.commit()
        print("Таблица SQLite создана")

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def create_bd_rasp():
    try:
        sqlite_connection = sqlite3.connect('rasp2.db')
        sqlite_create_table_query = '''CREATE TABLE "ACY-21" (
                                    day TEXT,
                                    pair TEXT,
                                    time TEXT,
                                    disc TEXT);'''

        cursor = sqlite_connection.cursor()
        cursor.execute(sqlite_create_table_query)
        sqlite_connection.commit()

        for i in range(36):
            day = 'Понеде'
            sql_update = """INSERT INTO "ACY-19" (day) VALUES ()"""

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def main():
    create_bd()
    # create_bd_rasp()



if __name__ == "__main__":
    main()
