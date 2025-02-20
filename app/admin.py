from django.contrib import admin
from .models import (
    Department, AcademicYear, YearOfStudy, Stream, Level, Programme,
    Student, Course, Assignment, Quiz
)

# Add search functionality to foreign key fields by specifying search_fields in the related models
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_per_page = 10
    list_max_show_all = 10
    search_fields = ['name']

@admin.register(AcademicYear)
class AcademicYearAdmin(admin.ModelAdmin):
    list_display = ('year',)
    list_per_page = 10
    list_max_show_all = 10
    search_fields = ['year']

@admin.register(YearOfStudy)
class YearOfStudyAdmin(admin.ModelAdmin):
    list_display = ('year',)
    list_per_page = 10
    list_max_show_all = 10
    search_fields = ['year']

@admin.register(Stream)
class StreamAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_per_page = 10
    list_max_show_all = 10
    search_fields = ['name']

@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_per_page = 10
    list_max_show_all = 10
    search_fields = ['name']

@admin.register(Programme)
class ProgrammeAdmin(admin.ModelAdmin):
    list_display = ('name', 'academic_year', 'year_of_study', 'stream', 'level', 'department')
    list_filter = ('academic_year', 'year_of_study', 'stream', 'level', 'department')
    list_per_page = 10
    list_max_show_all = 10
    search_fields = ['name', 'academic_year__year', 'year_of_study__year', 'stream__name', 'level__name', 'department__name']
    autocomplete_fields = ['academic_year', 'year_of_study', 'stream', 'level', 'department']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('regno', 'fullname', 'programme', 'department', 'academic_year', 'year_of_study', 'stream', 'level')
    search_fields = ('regno', 'fullname', 'programme__name', 'department__name', 'academic_year__year', 'year_of_study__year', 'stream__name', 'level__name')
    list_filter = ('programme', 'department', 'academic_year', 'year_of_study', 'stream', 'level')
    list_per_page = 10
    list_max_show_all = 10
    autocomplete_fields = ['programme', 'department', 'academic_year', 'year_of_study', 'stream', 'level']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'programme', 'academic_year', 'level')
    list_filter = ('programme', 'academic_year', 'level')
    list_per_page = 10
    list_max_show_all = 10
    search_fields = ['code', 'name', 'programme__name', 'academic_year__year', 'level__name']
    autocomplete_fields = ['programme', 'academic_year', 'level']

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('programme', 'department', 'academic_year', 'year_of_study', 'stream', 'level', 'start_date', 'end_date')
    list_filter = ('programme', 'department', 'academic_year', 'year_of_study', 'stream', 'level')
    list_per_page = 10
    list_max_show_all = 10
    search_fields = ['programme__name', 'department__name', 'academic_year__year', 'year_of_study__year', 'stream__name', 'level__name']
    autocomplete_fields = ['programme', 'department', 'academic_year', 'year_of_study', 'stream', 'level']

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('programme', 'department', 'academic_year', 'year_of_study', 'stream', 'level', 'start_date', 'end_date')
    list_filter = ('programme', 'department', 'academic_year', 'year_of_study', 'stream', 'level')
    list_per_page = 10
    list_max_show_all = 10
    search_fields = ['programme__name', 'department__name', 'academic_year__year', 'year_of_study__year', 'stream__name', 'level__name']
    autocomplete_fields = ['programme', 'department', 'academic_year', 'year_of_study', 'stream', 'level']
