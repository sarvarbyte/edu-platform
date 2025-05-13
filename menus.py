from coursera.file_manager import write, read
from coursera.student import student_menu
from coursera.teacher import teacher_menu


def auth_menu()->int:
    print("""
    1. Sign in
    2. Sign up
    3. Exit
    """)
    choice = int(input("Enter your choice: "))

    return choice

def sign_in():
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()
    role = input("Enter your role(student or teacher): ").strip()

    if role == "teacher":
        data = read("data/teacher.csv")
        for row in data:
            if row[1] == username and row[2] == password:
                teacher_menu(username, role)
                return

        print("Invalid username or password")
    elif role == "student":
        data = read("data/student.csv")
        for row in data:
            if row[1] == username and row[2] == password:
                student_menu(row[0], row[1])
                return
        print("Invalid username or password")
    else:
        print("Invalid role")


def sign_up():
    role = input("Enter your role(student or teacher): ").strip().lower()
    email = input("Enter your email: ").strip()
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()
    password_again = input("Enter your password: ").strip()
    if role == "student":
        if password == password_again and email.endswith("@gmail.com"):
            data = [email, username, password, role]
            write("data/student.csv", data)
            print("Sign up successful")
        else:
            print("Sign up failed, please try again")
    elif role == "teacher":
        if password == password_again and email.endswith("@gmail.com"):
            data = [email, username, password, role]
            write("data/teacher.csv", data)
            print("Sign up successful")
        else:
            print("Sign up failed, please try again")
    else:
        print("There isn't this role.")