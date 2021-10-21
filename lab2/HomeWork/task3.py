from Student import  Student
from Group import  Group

if __name__ == '__main__':
    try:
        st1 = Student('name1', 'surname1', {"sub1": 1, "sub2": 1, "sub4": 1})
        st2 = Student('name2', 'surname2', {"sub1": 2, "sub2": 2, "sub4": 2})
        st3 = Student('name3', 'surname3', {"sub1": 3, "sub2": 3, "sub4": 3})
        st4 = Student('name4', 'surname4', {"sub1": 4, "sub2": 4, "sub4": 4})
        st5 = Student('name5', 'surname5', {"sub1": 5, "sub2": 5, "sub4": 5})
        st6 = Student('name6', 'surname6', {"sub1": 6, "sub2": 6, "sub4": 6})

        group = Group(st1,st2,st3,st4,st5,st6)

        for i in group.highest_average_score(5):
            print(i)
    except Exception as ve:
        print(ve)

