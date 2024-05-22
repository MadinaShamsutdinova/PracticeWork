from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Callable


@dataclass
class Option:
    description: str
    action: Callable


class BaseMenu(ABC):
    options: list[Option]
    title: str
    prompt: str
    submenu: bool
    close: str
    username: str
    exit: str

    @abstractmethod
    def __init__(self,
                 options: list[Option],  # Mandatory
                 title: str = "Options:",
                 prompt: str = "Your choice: ",
                 submenu: bool = False,
                 close: str = "",
                 exit: str = "Exit") -> None:
        super().__init__()
        self.options = options
        self.title = title
        self.prompt = prompt
        self.submenu = submenu
        self.close = close
        self.exit = exit
        return None

    def askChoice(self) -> int:
        choice: int = -1
        feed = input(self.prompt)
        if feed.isdigit():
            choice = int(feed)
        return choice

    def showOptions(self) -> None:
        print(self.title)  # menu title
        # Iterate options
        for i, option in enumerate(self.options):
            print(f"{i + 1} - {option.description}")
        print(f"0 - {self.exit}")
        return None

    def activate(self) -> None:
        while True:
            # 1. Show options
            self.showOptions()
            # 2. Ask choice
            choice = self.askChoice()
            # 3. Do decision based choice
            if choice == 0:
                break
            elif 0 < choice <= len(self.options):
                index = choice - 1
                self.options[index].action()
            else:
                print("Unknown option.")
        print("")
        return None


