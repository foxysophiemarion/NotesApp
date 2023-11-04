import datetime
from os import path


class Note:
    note_id = 1

    def set_date(self) -> str:
        date = str(datetime.datetime.today().date())
        time = str(datetime.datetime.today().time())[:8]
        return "{} {}".format(date, time)

    def __init__(self, title: str, text: str):
        try:
            with open('notes.csv', 'r') as data:
                last_line = data.readlines()[-1]
                Note.note_id = int(last_line.split(";")[0]) + 1
        except FileNotFoundError as e:
            print("First note has been created!")
        except IndexError as e:
            print("First note has been created!")
        id = Note.note_id
        date = self.set_date()
        if title =="":
            title = "No title " + str(id)
        self.note = {"id": id, "date": date, "title": title, "text": text}

