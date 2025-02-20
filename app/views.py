# your_app/views.py
import random
from django.shortcuts import render
from .models import AcademicYear, YearOfStudy, Stream, Level, Programme, Assignment, Quiz,Student
from django.http import FileResponse
from django.conf import settings
import os
from django.db.models import Count
from django.http import HttpResponse, FileResponse
from datetime import date

def find_assignment(request):
    academic_years = AcademicYear.objects.all()
    years_of_study = YearOfStudy.objects.all()
    streams = Stream.objects.all()
    levels = Level.objects.all()
    programmes = Programme.objects.all()
    today = date.today()

    assignments = []
    quizzes = []

    if request.GET:
        selected_academic_year = request.GET.get('academic_year')
        selected_year_of_study = request.GET.get('year_of_study')
        selected_stream = request.GET.get('stream')
        selected_level = request.GET.get('level')
        selected_programme = request.GET.get('programme')

        filters = {}
        if selected_academic_year:
            filters['academic_year'] = selected_academic_year
        if selected_year_of_study:
            filters['year_of_study'] = selected_year_of_study
        if selected_stream:
            filters['stream'] = selected_stream
        if selected_level:
            filters['level'] = selected_level
        if selected_programme:
            filters['programme'] = selected_programme

        if filters:  # Only query if filters are selected
            assignments = Assignment.objects.filter(**filters)
            quizzes = Quiz.objects.filter(**filters)



    context = {
        'academic_years': academic_years,
        'years_of_study': years_of_study,
        'streams': streams,
        'levels': levels,
        'programmes': programmes,
        'assignments': assignments,
        'quizzes': quizzes,
        'today': today,
    }
    return render(request, 'find_assignment.html', context)


def download_file(request, file_path):
    file_path = os.path.join(settings.MEDIA_ROOT, file_path) # Important for security
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            response = FileResponse(f, content_type='application/octet-stream') # Or appropriate content type
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
            return response
    # Handle file not found error
    return HttpResponse("File not found", status=404)





def group_students(request):
    # Get objects for form dropdowns
    levels = Level.objects.all()
    programmes = Programme.objects.all()
    academic_years = AcademicYear.objects.all()
    years_of_study = YearOfStudy.objects.all()
    streams = Stream.objects.all()
    
    groups = None
    group_heading = None
    selected_values = {}

    if request.method == 'POST':
        level_id = request.POST.get('level')
        programme_id = request.POST.get('programme')
        academic_year_id = request.POST.get('academic_year')
        year_of_study_id = request.POST.get('year_of_study')
        stream_id = request.POST.get('stream')
        group_count = request.POST.get('group_count')

        # Save selected values to re-populate the form
        selected_values = {
            'level': level_id,
            'programme': programme_id,
            'academic_year': academic_year_id,
            'year_of_study': year_of_study_id,
            'stream': stream_id,
            'group_count': group_count,
        }

        try:
            group_count = int(group_count)
        except (ValueError, TypeError):
            group_count = 0

        # Retrieve the selected objects (if they exist)
        try:
            level = Level.objects.get(pk=level_id)
            programme = Programme.objects.get(pk=programme_id)
            academic_year = AcademicYear.objects.get(pk=academic_year_id)
            year_of_study = YearOfStudy.objects.get(pk=year_of_study_id)
            stream = Stream.objects.get(pk=stream_id)
        except (Level.DoesNotExist, Programme.DoesNotExist, AcademicYear.DoesNotExist,
                YearOfStudy.DoesNotExist, Stream.DoesNotExist):
            level = programme = academic_year = year_of_study = stream = None

        if all([level, programme, academic_year, year_of_study, stream]) and group_count > 0:
            # Filter students by the selected criteria
            students = list(Student.objects.filter(
                level=level,
                programme=programme,
                academic_year=academic_year,
                year_of_study=year_of_study,
                stream=stream
            ))

            # Shuffle students randomly before assigning to groups
            random.shuffle(students)

            # Create groups
            groups = [[] for _ in range(group_count)]
            for index, student in enumerate(students):
                groups[index % group_count].append(student)
            
            # Create a heading using the selected Programme, Level, Stream, and Year of Study
            group_heading = f"{programme} - {level} - {stream} - year {year_of_study}"

    context = {
        'levels': levels,
        'programmes': programmes,
        'academic_years': academic_years,
        'years_of_study': years_of_study,
        'streams': streams,
        'groups': groups,
        'group_heading': group_heading,
        'selected': selected_values,
    }
    return render(request, 'generate_groups.html', context)




def index(request):
    # Count total assignments and quizzes
    assignment_count = Assignment.objects.count()
    quiz_count = Quiz.objects.count()

    # Count assignments by programme
    assignment_per_programme = Assignment.objects.values('programme__name').annotate(count=Count('id'))
    
    # Count quizzes by programme
    quiz_per_programme = Quiz.objects.values('programme__name').annotate(count=Count('id'))
    
    # Count assignments by course
    assignment_per_course = Assignment.objects.values('course__name').annotate(count=Count('id'))
    
    # Count quizzes by course
    quiz_per_course = Quiz.objects.values('course__name').annotate(count=Count('id'))

    # Convert queryset results to dictionary for easier access in the template
    assignment_per_programme_dict = {item['programme__name']: item['count'] for item in assignment_per_programme}
    quiz_per_programme_dict = {item['programme__name']: item['count'] for item in quiz_per_programme}
    assignment_per_course_dict = {item['course__name']: item['count'] for item in assignment_per_course}
    quiz_per_course_dict = {item['course__name']: item['count'] for item in quiz_per_course}

    context = {
        'assignment_count': assignment_count,
        'quiz_count': quiz_count,
        'assignment_per_programme': assignment_per_programme_dict,
        'quiz_per_programme': quiz_per_programme_dict,
        'assignment_per_course': assignment_per_course_dict,
        'quiz_per_course': quiz_per_course_dict
    }

    return render(request, 'index.html', context)
