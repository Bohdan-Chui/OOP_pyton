from datetime import date

from notebook import Notebook
from lab4.part1.person import Person

if __name__ == '__main__':
    notebook = Notebook()
    notebook + Person("name1","surname1", "+380(63)-312-97-08", date(2002,10,26))
    # notebook - "name1"
    person = notebook * "name1"
    print(person)