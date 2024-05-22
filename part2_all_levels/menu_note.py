from base_menu import BaseMenu, Option
from model_user import User
### TEMPORARY START
from model_note import Note
NOTES = [
    Note(1, "example", "Hello\nworld"),
    Note(2, "tomorrow", "eat\nplay\nsleep")
]
### TEMPORARY END

class MenuNote(BaseMenu):
    # initialize
    def __init__(self, user: User) -> None:
        self.user = user
        super().__init__(
            options=[
                Option("List notes", self.listNotes),
                Option("View note", self.viewNote),
                Option("Add note", self.addNote),
                Option("Edit note", self.editNote),
                Option("Delete note", self.deleteNote),

            ],
            title=f"User '{user.name}' options:",
            exit="Logout"
        )


    def listNotes(self) -> None:
        print("List notes to be implemented...")

        # get_memos = NoteDAO.getNotes()
        #
        # if len(get_memos) > 0:
        #     rows = []
        #     for note in get_memos:
        #         rows.append(f"{note.id} - {note.title}")
        #     content = '\n'.join(rows)
        #     memo_details = KirjeDetails(
        #         content=content,
        #         header_separation=" - ",
        #         headers={
        #             'ID': 'Title',
        #             'Title': ' notes '
        #         }
        #     )
        #
        #     memo_list = Kirje(memo_details)
        #     memo_list.display("streamlined")
        #     rows.clear()
        # else:
        #     print("There are no notes to display.")
        # print("")
        # return None
    def viewNote(self) -> None:
        print("View note to be implemented...")

        #title = input("Search note by title: ")
        #
        # note = NoteDAO.searchNote(title)
        # if note:
        #     memo_details = KirjeDetails(
        #         content=note.content,
        #         header_separation=" - ",
        #         headers={
        #             'ID': str(note.id),
        #             'Title': note.title
        #         }
        #     )
        #
        #
        #     current_memo = Kirje(memo_details)
        #     current_memo.display("default")
        # else:
        #    print("Not found.")
        # print("")
        # return None

    def addNote(self) -> None:
        print("Add note to be implemented...")
        # title = input("Insert title: ")
        # num_rows = int(input("Insert the amount of rows: "))
        # rows = []
        #
        # for i in range(num_rows):
        #     row_content = input(f"Insert row {i + 1}: ")
        #     rows.append(row_content)
        #
        # content = '\n'.join(rows)
        # NoteDAO.addNote(title, content)
        #
        # print("Note stored!")
        # print("")

    def editNote(self) -> None:
        print("Edit note to be implemented...")
        # title = input("Insert note title: ")
        # note = NoteDAO.searchNote(title)
        #
        # if note:
        #         content_lines = note.content.split('\n')
        #         line_num = int(input(f"Insert row number to edit 1-{len(content_lines)}, 0 to cancel: ")) - 1
        #         if line_num == -1:
        #             print("Cancelled.")
        #             return None
        #         new_content = input("Insert replacement row: ")
        #         content_lines[line_num] = new_content
        #         update = '\n'.join(content_lines)
        #         NoteDAO.editNote(note.id, note.title, update)
        #         print("Edit completed!")
        #
        # else:
        #     print(f"'{title}' not found.")
        # print("")
        # return None
    def deleteNote(self) -> None:
        print("Delete note to be implemented...")
        # title = input("Delete note (insert title): ")
        # del_row = NoteDAO.deleteNote(title)
        # if del_row == 1:
        #         print("Note deleted.\n")
        # else:
        #     print(f"'{title}' not found.")
        #
        # return None
