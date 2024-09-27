class Gruppe:
    def __init__(self, id, mentor):
        self.id = id
        self.mentor = mentor

class Student:
    def __init__(self, name, birthyear, group):
        self.name = name
        self.birthyear = birthyear
        self.group = group

group_1B = Gruppe("1-B", "Ken")
group_2B = Gruppe("2-B", "Dennis")
group_3B = Gruppe("3-B", "Brian")

student_john = Student("John", 2000, group_1B.id)
student_jane = Student("Jane", 1999, group_2B.id)
student_gary = Student("Gary", 1997, group_3B.id)

def check_group(student_type : Student, group_number : str) -> str:
    if student_type.group == group_number:
        return group_number

check_group(student_john, "1-B")

def test_check_group():
    assert check_group(student_john, "1-B") == group_1B.id
    assert check_group(student_jane, "2-B") == group_2B.id
    assert check_group(student_gary, "3-B") == group_3B.id

test_check_group()
