from django.db import models
from datetime import timedelta


class Language(models.Model):
    name = models.CharField(max_length=30)
    month_to_learn = models.IntegerField()

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        super().save(*args, **kwargs)


class AbstractPerson(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=13)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.phone_number[0] == '0':
            self.phone_number = '+996' + self.phone_number[1:10]
        super().save(*args, **kwargs)


class Student(AbstractPerson):
    work_study_place = models.CharField(max_length=35, null=True)
    has_own_notebook = models.BooleanField()
    preferred_os = models.CharField(max_length=15)


class Mentor(AbstractPerson):
    student = models.ManyToManyField(Student, related_name='mentors', through='Course')
    main_work = models.CharField(max_length=35, null=True)
    experience = models.DateField()


class Course(models.Model):
    name = models.CharField(max_length=25)
    language = models.CharField(max_length=25)
    date_started = models.DateField()
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def get_end_date(self):
        days = self.language.month_to_learn * 30
        date_end = self.date_started + timedelta(days=days)
        print(f'У студента {self.student.name} курс заканчивается {date_end}')

