from django.db import models


# Create your models here.
class School(models.Model):
    school_name = models.CharField(max_length=255)

    def __str__(self):
        return self.school_name


class Teacher(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    # date_of_birth= models.DateTimeField()
    school = models.ManyToManyField(School)

    def __str__(self):
        return self.first_name


class Subject(models.Model):
    subject_name = models.CharField(max_length=255)
    teacher = models.ManyToManyField(Teacher)

    def __str__(self):
        return self.subject_name


class Department(models.Model):
    department_name = models.CharField(max_length=255)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.department_name
