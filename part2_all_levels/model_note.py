from dataclasses import dataclass
from db_conn import DB_CONN

@dataclass
class Note:
    id: int
    title: str
    content: str


class NoteDAO:
    @staticmethod
    def addNote(title: str, content: str) -> None:
            sql_query = "INSERT OR IGNORE INTO note (title, content) VALUES (?, ?)"
            values = (title, content)
            cursor = DB_CONN.cursor()
            cursor.execute(sql_query, values)

            DB_CONN.commit()
            cursor.close()

    @staticmethod
    def getNotes(limit: int = -1) -> list[Note]:
        notes = []
        try:
            cursor = DB_CONN.cursor()
            sql_query = "SELECT * FROM note LIMIT ?"
            cursor.execute(sql_query, (limit,))

            records = cursor.fetchall()

            for record in records:
                note = Note(*record)
                notes.append(note)
            cursor.close()
        except Exception:
            print("Error while fetching notes:")

        return notes
    @staticmethod
    def searchNote(title: str) -> Note | None:
        cursor = DB_CONN.cursor()
        single = (title,)
        sql_query = "SELECT * FROM note WHERE title = ?"
        cursor.execute(sql_query, single)
        record = cursor.fetchone()
        cursor.close()
        if record:
            return Note(record[0], record[1], record[2])

        return None

    @staticmethod
    def editNote(id: int, title: str, content: str) -> None:
        cursor = DB_CONN.cursor()
        tuple_data = (title, content, id)
        sql_query = "UPDATE note SET title = ?, content = ? WHERE id = ?"
        cursor.execute(sql_query, tuple_data)
        DB_CONN.commit()
        cursor.close()

        return None

    @staticmethod
    def deleteNote(title: str) -> int:
        cursor = DB_CONN.cursor()
        single = (title,)
        sql_query = "DELETE FROM note WHERE title = ?"
        cursor.execute(sql_query, single)
        DB_CONN.commit()
        del_rows = cursor.rowcount
        cursor.close()

        return del_rows



