from django.db import models

# Create your models here.

class Pets(models.Model):
    gender_option=(("Male","Male"),("Female","Female"))
    type=(("D","Dog"),("C","Cat"))
    animal_type=models.CharField(max_length=30,choices=type,default="NA")
    name = models.CharField(max_length=30)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.CharField(max_length=20,choices=gender_option)
    price=models.FloatField(default=0)
    image = models.ImageField(upload_to="media")
    description = models.TextField(max_length=1000)

    class Meta:
        db_table = "PetTbl"


class Student(models.Model):
    student_name = models.CharField(max_length=100)
    student_age = models.IntegerField()
    student_email = models.EmailField()
    student_location = models.CharField(max_length=50)
    student_course = models.CharField(max_length=100)


class Author(models.Model):
    author_name=models.CharField(max_length=100)
    def _str_(self):
        return self.author_name


class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)

class Course(models.Model):
    course_name=models.CharField(max_length=100)
    student=models.ManyToManyField(Student)