import sqlite3
import sys
from pathlib import Path

DB_FILEPATH = Path("./notes.db")
DB_CONN = sqlite3.connect(DB_FILEPATH)
DB_CONN.execute("PRAGMA foreign_keys = ON")
DB_CONN.commit()

class DB:
    @staticmethod
    def loadSqlScript(filepath: str) -> str:
        content = ""
        try:
            with open(filepath, 'r', encoding="utf-8") as file:
                content = file.read()
        except FileNotFoundError:
            print(f"Failed to read '{filepath}' file.")
            sys.exit(-1)
        return content

    @staticmethod
    def initializeDB() -> None:
        script = DB.loadSqlScript("setup.sql")
        cursor = DB_CONN.cursor()
        cursor.executescript(script)
        DB_CONN.commit()
        cursor.close()