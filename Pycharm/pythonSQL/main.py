import sqlite3
import os

def createDatabase():
    if os.path.exists("students.db"):
        os.remove("students.db")

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    return conn, cursor



def main():
    conn, cursor = createDatabase()

if __name__ == "__main__":
    main()
