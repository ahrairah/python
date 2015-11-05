import sys
from notebook import Note, Notebook


class Menu:
    """Display menu and respond to choices when run."""

    def __init__(self):
        self.Notebook = Notebook()
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit
        }

    def display_menu(self):
        print("""Notebook Menu:
         1. show all notes
         2. search notes
         3. add notes
         4. modify notes
         5. quit""")

    def run(self):
        """Display the menu and choices."""
        while True:
            self.display_menu()
            choice = input("Enter an option. ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice.".format(choice))

    def show_notes(self, notes=None):
        if not notes:
            notes = self.Notebook.notes
            for note in notes:
                print("{0}: {1}\n{2}".format(note.id, note.tags, note.memo))

    def search_notes(self):
        filter_str = input("Search for: ")
        notes = self.Notebook.search(filter_str)
        self.show_notes(notes)

    def add_note(self):
        memo = input("Enter a memo.")
        self.Notebook.new_note(memo)
        print("Your note has been added.")

    def modify_note(self):
        id = input("Enter a note id.")
        memo = input("Enter a memo.")
        tags = input("Enter tags: ")
        if memo:
            self.Notebook.modify_memo(id, memo)
        if tags:
            self.Notebook.modify_tags(id, tags)

    def quit(self):
        print("Thank you for using your Notebook today.")
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()
