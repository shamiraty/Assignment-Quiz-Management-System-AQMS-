# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('find_assignment/', views.find_assignment, name='find_assignment'),
    path('download/<path:file_path>/', views.download_file, name='download_file'),
    path('group-students/', views.group_students, name='group_students'),
    path('', views.index, name='index'),
    
]