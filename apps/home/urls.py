# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    path('students', views.students, name='students'),
    path('students/<int:student_id>/', views.student_detail, name='student_detail'),
    path('courses', views.courses, name='courses'),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('sessions', views.sessions, name='sessions'),
    path('sessions/<int:session_id>/', views.session_detail, name='session_detail'),
    path('scholarships', views.scholarships, name='scholarships'),
    path('scholarships/<int:scholarship_id>/', views.scholarship_detail, name='scholarship_detail'),
    path('events', views.events, name='events'),
    # path('courses/<int:course_id>/', views.course_detail, name='course_detail'),



    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
