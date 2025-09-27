import sqlite3
import os


def createDatabase():
    if os.path.exists("students.db"):
        os.remove("students.db")

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    return conn, cursor


def createTables(cursor):

    cursor.execute("""
    CREATE TABLE Students (
        id INTEGER PRIMARY KEY,
        name VARCHAR NOT NULL,
        age INTEGER,
        email VARCHAR UNIQUE,
        city VARCHAR)
    """)

    cursor.execute("""
                   CREATE TABLE Courses 
                   (
                       id    INTEGER PRIMARY KEY,
                       course_name  VARCHAR NOT NULL,
                       instructor TEXT,
                       credits  INTEGER
                   )
                   """)


def main():
    conn, cursor = createDatabase()

    try:
        createTables(cursor)
        conn.commit()

    except sqlite3.Error as e:
        print(e)

    finally:
        conn.close()


if __name__ == "__main__":
    main()
