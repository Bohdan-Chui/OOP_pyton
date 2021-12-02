from Notebook import Notebook
if __name__ == '__main__':
    notebook = Notebook()
    # notebook + Person("name2","surname2", "+380(63)-312-97-08", date(2002,10,26))
    # notebook - "name1"
    person = notebook * "name1"
    print(person)