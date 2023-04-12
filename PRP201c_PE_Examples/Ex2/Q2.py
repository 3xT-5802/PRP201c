#Write a program in the python programming language using object—oriented programming techniques.
# The program enters a list Of students, each with information on name, age and test scores.
# Sort students by name and order in the alphabet table.
# Print the list of students before and after the sorting.

import re
from _testcapi import exception_print

# Student class
class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def get_name(self):
        return self.name

    def to_String(self):
        return str(self.name) + '\t' + str(self.age) + '\t' + str(self.score)

# Input student list (stop when user confirms finish entering)
student_list = list()
isFinish = False
while not isFinish:
    while True:
        student_name = input("Enter student name: ").strip()
        student_name = re.sub(' +', ' ', student_name)
        if (student_name.replace(" ","").isalpha()):
            print(student_name)
            break
        else:
            print("Name must have only letters!")
    while True:
        try:
            student_age = input("Enter student age: ")
            age = int(student_age)
            if (age<0):
                print("Age must be a positive integer!")
                continue
            break
        except:
            print("Age must be a positive integer!")
    while True:
        try:
            test_score = input("Enter test score: ")
            score = float(test_score)
            if (score<0):
                print("Score must be a positive number!")
                continue
            break
        except:
            print("Score must be a positive number!")
    student = Student(student_name, student_age, test_score)
    student_list.append(student)
    finish = input("Finish? (Y/N) ").strip()
    # Stop entering when user confirms finish entering
    while True:
        if (finish.lower()=='y'):
            isFinish = True
            break
        elif (finish.lower()=='n'):
            break
        else:
            print("Only input Y/N!")



# Sort student list by name (ascending)
def sort_student_list(student_list):
    list_size = len(student_list)
    for i in range(list_size):
        for j in range(list_size - 1):
            if student_list[j].get_name() > student_list[j + 1].get_name():
                student_list[j], student_list[j + 1] = student_list[j + 1], student_list[j]

def show_students(student_list):
    print("Name\tAge\tTest Score")
    for student in student_list:
        print(student.to_String())

# Print the list before & after sorting
show_students(student_list)
sort_student_list(student_list)
show_students(student_list)