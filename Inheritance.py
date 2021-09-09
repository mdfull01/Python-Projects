
# creating parent class User
class User:
    fname = ''
    lname = ''
    email = ''
    password = ''
    ID_number = 0

# creating child class Professor
class Professor(User):
    mailing_address = ''
    salary = 0
    tenure = False

# creating child class Student
class Student(User):
    gpa = 0
    account_balance = 0
    lives_on_campus = True
    
    
