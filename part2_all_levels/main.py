from menu_login import MenuLogin
from db_conn import DB, DB_CONN



class Main:


    def __init__(self) -> None:
        DB.initializeDB()
        print("Program starting.")
        # initialize
        # run

        _menu = MenuLogin()
        # 2. Operate
        _menu.activate()

        # cleanup
        print("Program ending.")
        DB_CONN.commit()
        DB_CONN.close()
        return None


if __name__ == '__main__':
    app = Main()
