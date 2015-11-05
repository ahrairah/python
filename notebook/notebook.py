import datetime

last_id = 0


class Note:
    """Represent a note in the notebook. Match against a string in searches and store tags for each note."""

    def __init__(self, memo, tags=''):
        """initialize a note with memo and optional space-separated tags. Automatically set the note's
        creation date and a unique id."""
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter_str):
        """Determine if this note matches the filter text. Return True if it matches, False otherwise.
        Search is case sensitive and matches both text and tags."""
        return filter_str in self.memo or filter_str in self.tags


class Notebook:
    def __init__(self):
        """Represents a collection of notes. Can be tagged, modified and searched."""
        self.notes = []

    def new_note(self, memo, tags=''):
        """Creates a new Note and adds it to 'notes' attribute."""
        self.notes.append(Note(memo, tags))

    def _find_note(self, note_id):
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None

    def modify_memo(self, note_id, memo):
        """Find a note with the given id an modify the value of it."""
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True
        return False

    def modify_tags(self, note_id, tags):
        """Find a note with the given id and modify the tag of it."""
        for note in self.notes:
            if note.id == note_id:
                note.tags = tags
                break

    def search(self, filter_str):
        """Finds all notes that match the filter"""
        return [note for note in self.notes if note.match(filter_str)]
