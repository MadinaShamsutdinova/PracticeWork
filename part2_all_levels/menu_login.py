from base_menu import BaseMenu, Option
from dao_user import UserDB
from menu_note import MenuNote

import hashlib
class MenuLogin(BaseMenu):
    def __init__(self) -> None:
        super().__init__(
            options=[
                Option("Login", self.login_user),
                Option("Register", self.register_user),
            ]
        )

    def login_user(self) -> None:
        print("Insert credentials below:")
        insert_name = input("Insert username: ")
        insert_password = input("Insert password: ")
        user = UserDB.searchUser(insert_name)
        if not user:
            print("Failed to authenticate!")
            print("")
        else:
            md5_hash = hashlib.md5()
            md5_hash.update(insert_password.encode('utf-8'))
            encrypted_password = md5_hash.hexdigest()
            if encrypted_password == user.password:
                print("Authenticated!")
                print("")
                _menu = MenuNote(user)
                _menu.activate()
            else:
                print("Failed to authenticate!")
                print("")
        return None

    def register_user(self):
            insert_name = input("Insert username: ")
            if not self.checker_len(insert_name):
                print("Username must be between 4 and 10 characters long and can contain letters, digits, '_', and '-'")

            if UserDB.searchUser(insert_name):
                print("Username already exists!")

            insert_password = input("Insert password: ")
            confirm_password = input("Insert password again: ")
            if insert_password != confirm_password:
                print("Passwords do not match! Please try again.")

            if not self.checker_len(insert_password):
                print("Passwords must be between 4 and 10 characters long and can contain letters, digits, '_', and '-'")

            md5_hash = hashlib.md5()
            md5_hash.update(insert_password.encode('utf-8'))
            encrypted_password = md5_hash.hexdigest()
            UserDB.insertUser(insert_name, encrypted_password)
            print("Registration completed!")
            print("")
            return None

    @staticmethod
    def checker_len(name: str) -> bool:
        allowed_chars = set('_-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
        if len(name) < 4:
            print("")
            return False
        if len(name) > 10:
            print("")
            return False
        elif not all(char in allowed_chars for char in name):
            print("")
            return False
        return True



