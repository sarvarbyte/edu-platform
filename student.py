from coursera.send_email import send_massage
from file_manager import read, write


class Student:
    def __init__(self, email, name):
        self.name = name
        self.email = email

    def buy_course(self):
        courses = read(path="data/courses.csv")
        course_list = [self.email]
        print(course_list)
        for course in courses:
            print(course)

        course_name = input("Enter your coruse name: ")

        for course in courses:
            if course[0] == course_name:
                course_list.extend(course)
                write(path="data/course_list.csv", data=course_list)
        else:
            print("Course not found")

    def my_course(self):
        courses = read(path="data/course_list.csv")

        for course in courses:
            if course[0] == self.email:
                print(course)
            else:
                print("Course not found")
    def send_massage(self):
        email = input("Enter your coruse email: ")
        massage = input("Enter your massage: ")
        send_massage(email, massage)



def student_menu(email, username):
    student = Student(email, username)
    print("""
    1. Send a massage
    2. Notications
    3. My courses
    4. Buy a new course
    5. Exit
    """)

    choice = input("Enter your choice: ")
    if choice == "1":
        student.send_massage()
    elif choice == "2":
        pass
    elif choice == "3":
        student.my_course()
    elif choice == "4":
        student.buy_course()
    elif choice == "5":
        return
    else:
        print("Invalid choice")

    student_menu(email, username)