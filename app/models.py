from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from ckeditor.fields import RichTextField
# Lookup Models
class Department(models.Model):
    CHOICES = [
        ("Law", "Law"),
        ("Business Administration", "Business Administration"),
        ("Laboratory", "Laboratory"),
        ("Information Technology", "Information Technology"),
        ("Project Management", "Project Management"),
        ("Community Development", "Community Development"),
        ("Electricity", "Electricity"),
    ]
    name = models.CharField(max_length=100, choices=CHOICES, unique=True)
    
    def __str__(self):
        return self.name

class AcademicYear(models.Model):
    YEAR_CHOICES = [
        ("2025-2026", "2025-2026"),
        ("2024-2025", "2024-2025"),
        ("2023-2024", "2023-2024"),
    ]
    year = models.CharField(max_length=9, choices=YEAR_CHOICES, unique=True)
    
    def __str__(self):
        return self.year

class YearOfStudy(models.Model):
    year = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 7)], unique=True)
    
    def __str__(self):
        return str(self.year)

class Stream(models.Model):
    CHOICES = [
        ("Evening", "Evening"),
        ("Morning", "Morning"),
        ("Fulltime", "Fulltime"),
    ]
    name = models.CharField(max_length=50, choices=CHOICES, unique=True)
    
    def __str__(self):
        return self.name

class Level(models.Model):
    CHOICES = [
        ("Technician Certificate", "Technician Certificate"),
        ("Ordinary Diploma", "Ordinary Diploma"),
        ("Advanced Diploma", "Advanced Diploma"),
        ("Postgraduate Diploma", "Postgraduate Diploma"),
        ("Bachelor Degree", "Bachelor Degree"),
        ("Masters Degree", "Masters Degree"),
    ]
    name = models.CharField(max_length=50, choices=CHOICES, unique=True)
    
    def __str__(self):
        return self.name

# Programme Model
class Programme(models.Model):
    CHOICES = [
        ("Law", "Law"),
        ("Business Administration", "Business Administration"),
        ("Laboratory", "Laboratory"),
        ("Information Technology", "Information Technology"),
        ("Project Management", "Project Management"),
        ("Community Development", "Community Development"),
        ("Electricity", "Electricity"),
         ("Management Practice", "Management Practice"),
    ]
    name = models.CharField(max_length=100, choices=CHOICES)
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    year_of_study = models.ForeignKey(YearOfStudy, on_delete=models.CASCADE)
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name} - {self.academic_year}"



# Student Model without Authentication
class Student(models.Model):
    regno = models.CharField(max_length=20, unique=True)
    fullname = models.CharField(max_length=200)
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE,related_name="programme")
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE,related_name="academic_year")
    year_of_study = models.ForeignKey(YearOfStudy, on_delete=models.CASCADE,related_name="year_of_study")
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE,related_name="stream")
    level = models.ForeignKey(Level, on_delete=models.CASCADE,related_name="level")
    
    def __str__(self):
        return self.regno


# Course Model (child of Programme)
class Course(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20, unique=True)
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE, related_name='courses')
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.code}: {self.name}"


# Assignment Model (child of Programme)
class Assignment(models.Model):
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,default='301')  # Add this line
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    year_of_study = models.ForeignKey(YearOfStudy, on_delete=models.CASCADE)
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    question = RichTextField()   
    file = models.FileField(upload_to='assignments/', null=True, blank=True)
    
    def __str__(self):
        return f"Assignment for {self.programme}"

# Quiz Model (child of Programme)
class Quiz(models.Model):
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  # Add this line
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    year_of_study = models.ForeignKey(YearOfStudy, on_delete=models.CASCADE)
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    question  = RichTextField()
    file = models.FileField(upload_to='quizzes/', null=True, blank=True)
    
    def __str__(self):
        return f"Quiz for {self.programme}"
