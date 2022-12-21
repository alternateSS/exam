import datetime
from user.models import Student, Mentor, Language, Course

language_1 = Language.objects.create(name='Python', month_to_learn=6)
language_2 = Language.objects.create(name='Java Script', month_to_learn=6)
language_3 = Language.objects.create(name='UX-UI design', month_to_learn=2)

student_1 = Student.objects.create(name='Amanov Aman',
                            email='aman@mail.ru',
                            phone_number='+996700989898',
                            work_study_place='School №13',
                            has_own_notebook=True,
                            preferred_os='windows')

student_2 = Student.objects.create(name='Apina Alena',
                            email='aapina@bk.ru',
                            phone_number='0550888888',
                            work_study_place='TV',
                            has_own_notebook=True,
                            preferred_os='mac')

student_3 = Student.objects.create(name='Phil Spencer',
                        email='spencer@microsoft.com',
                        phone_number='0508312312',
                        work_study_place='Microsoft Gaming',
                        has_own_notebook=False,
                        preferred_os='linux')

mentor_1 = Mentor(name='Ilona Maskova',
                        email='imask@gmail.com',
                        phone_number='0500545454',
                        main_work=None,
                        experience=datetime.date(year=2021, month=10, day=23))
mentor_1.save()

mentor_2 = Mentor(name='Halil Nurmuhametov',
                        email='halil@gmail.com',
                        phone_number='0709989876',
                        main_work='University of Fort Collins',
                        experience=datetime.date(year=2010, month=9, day=18))
mentor_2.save()

course_py_1 = Course.objects.create(name='Python-21', mentor=mentor_2, student=student_1, date_started='2022-01-25', language=language_1)
course_py_2 = Course.objects.create(name='Python-21', mentor=mentor_2, student=student_2, date_started='2022-05-18', language=language_1)
course_ui = Course.objects.create(name='UXUI design-43', mentor=mentor_1, student=student_3, date_started='2022-02-05', language=language_3)