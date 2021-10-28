import datetime


class Note:

    def __init__(self, task, finaldate):
        self.task = task
        self.finaldate = finaldate

    @property
    def task(self):
        return self.__task

    @task.setter
    def task(self, task):
        if not isinstance(task,str):
            raise TypeError('task must be string')
        if task and task.strip():
            self.__task = task
        else:
            raise TypeError("task is empty")

    @property
    def finaldate(self):
        return self.__finaldate

    @finaldate.setter
    def finaldate(self, finaldate):
        if not isinstance(finaldate, datetime.date):
            raise ValueError('final date must be datetime type')
        self.__finaldate = finaldate

    def __str__(self) -> str:
        return f'Finaldate: {self.__finaldate.strftime("%d.%B.%Y")}Task: {self.__task}'


class Notebook:
    def __init__(self, *notes):
        self.notes = notes

    @property
    def notes(self):
        return self.__notes

    @notes.setter
    def notes(self, notes):
        if any(not isinstance(note, Note) for note in notes):
            raise TypeError("notes must be of Note type")
        self.__notes = list(notes)

    def add_note(self, note):
        if isinstance(note, Note):
            self.__notes.append(Note)
        else:
            raise TypeError('notes must be Note type')

    def dell_product(self, note):
        self.notes.remove(note)

date = datetime.datetime(2013, 1, 1)
a = Note('task1', datetime.datetime(2013, 1, 1))
notebook = Notebook(Note('task1', datetime.datetime(2012, 1, 1)), Note('task2', datetime.datetime(1201,1,10)))
