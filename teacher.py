from coursera.file_manager import write, read
from coursera.send_email import send_massage


class Teacher(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def add_course(self):
        course_name = input("Enter course name: ")
        course_duration = input("Enter course duration: ")
        teacher_name = input("Enter teacher's fullname: ")
        course_price = input("Enter course's price: ")
        data = [course_name, course_duration, teacher_name, course_price]

        write("data/courses.csv", data)

    def show_students(self):
        teacher_name = input("Enter teacher's fullname: ")
        data = read("data/course_list.csv")

        for row in data:
            if row[3] == teacher_name:
                print(row)
        else:
            print("Invalid teacher")

    def change_prices(self):
        course_name = input("Enter course name: ")
        course_duration = input("Enter course duration: ")
        new_price = input("Enter new course price: ")
        courses = read("data/courses.csv")

        for course in courses:
            if course[0] == course_name and course[1] == course_duration:
                course[3] = new_price
            else:
                print("No found course")

    def send_massage(self):
        email = input("Enter e-mail address: ")
        massage = input("Enter massage: ")
        send_massage(email, massage)
    11


def teacher_menu(username, password):
    teacher = Teacher(username, password)
    print(f"""
    1. Notification()
    2. Add a new course
    3. Show all students
    4. Change course price
    5. Exit the program
    """)
    choice = input("Enter your choice: ")
    if choice == "1":
        pass
    elif choice == "2":
        teacher.add_course()
    elif choice == "3":
        teacher.show_students()
    elif choice == "4":
        teacher.change_prices()
    elif choice == "5":
        return
    else:
        print("Invalid choice")

    teacher_menu(username, password)