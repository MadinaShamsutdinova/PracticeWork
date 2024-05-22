import sqlite3
import hashlib
from db_conn import DB, DB_CONN
from model_user import User
class UserDB:
    @staticmethod
    def searchUser(name: str) -> None | User:
        cursor = DB_CONN.cursor()
        single = (name,)
        sql_query = "SELECT * FROM user WHERE name = ?"
        cursor.execute(sql_query, single)
        record = cursor.fetchone()
        cursor.close()
        if record:
            user = User(*record)
            return user
        return None

    @staticmethod
    def insertUser(name: str, password: str) -> None:
        cursor = DB_CONN.cursor()
        user_data = (name, password)
        sql_query = "INSERT INTO user (name, password) VALUES (?, ?)"
        cursor.execute(sql_query, user_data)
        DB_CONN.commit()
        cursor.close()