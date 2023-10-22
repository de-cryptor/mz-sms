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
    path('courses', views.courses, name='courses'),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),


    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
