class Gruppe:
    def __init__(self, id, mentor): # Skap objektet
        self.id = id
        self.mentor = mentor # Viktig

class Student:
    def __init__(self, name, birthyear, group): # Skap objektet
        self.name = name
        self.birthyear = birthyear
        self.group = group

# Lag grupper med objektet
group_1B = Gruppe("1-B", "Ken")
group_2B = Gruppe("2-B", "Dennis")
group_3B = Gruppe("3-B", "Brian")

# Lag studenter med objektet
student_john = Student("John", 2000, group_1B.id)
student_jane = Student("Jane", 1999, group_2B.id)
student_gary = Student("Gary", 1997, group_3B.id)

def check_group(student_type : Student, group_number : str) -> str:
    if student_type.group == group_number: # Sjekk om student er lik gruppenummeret
        return group_number

def test_check_group(): # Alle tester funker, men gir assertion error om du endrer gruppenummer string
    assert check_group(student_john, "1-B") == group_1B.id
    assert check_group(student_jane, "2-B") == group_2B.id
    assert check_group(student_gary, "3-B") == group_3B.id

test_check_group()
