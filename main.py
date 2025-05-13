"""
Online kurslarni sotib olishlik va kurslarni yuklashlik
imkoniyatini beruvchi dastur yaratish kerak.
Misol uchun huddi udemy.com kabi, unda eng kamida quyidagi
imkoniyatlar bo'lishi kerak.

- Pochata orqali o'qituvchi yoki oddiy foydalanuvchi bo'lib ro'yxatda o'tish
- o'qituvchilarda yangi kurslar qo'shish va kurslarini kimlar sotib
  olganligini ko'rish
- kurslanri narxini o'zgartirishlik
- o'quvchilarda esa kurslarni sotib olishlik
- o'zi sotib olgan kurslarni ro'yxatini ko'rish
- kurs o'qituvchisiga habar yuborish pochta orqali va dastur orqali
- o'qituvchi o'quvchilardan kelgan habarlarni ko'ra olishi kerak
- bundan boshqa yana istalgancha imkoniyat qo'shishlik mumkin

"""
from coursera.menus import auth_menu, sign_in, sign_up

"""

My courses
My students
Messages(10)
    sanjarbeksocial@gmail.com(10)

    sanjarbeksocial@gmail.com(10)
    sanjarbeksocial@gmail.com(10)
    sanjarbeksocial@gmail.com(10)


My courses
Messages(2)
    sanjarbekwork@gmail(10)

"""


def main():
    choice = auth_menu()

    if choice == 1:
        sign_in()
    elif choice == 2:
        sign_up()
    elif choice == 3:
        print("Goodbye")
        return
    else:
        print("Wrong choice")
    
    main()



if __name__ == '__main__':
    main()