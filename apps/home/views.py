# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.db.models import Count
from apps.student.models import *


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def students(request):
    students = Student.objects.all()
    context = {'students': students}

    html_template = loader.get_template('student/students.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def student_detail(request, student_id):
    student = Student.objects.get(id=student_id)
    sessions = SessionEnrollment.objects.filter(student=student)
    scholarships = ScholarshipEnrollment.objects.filter(student=student)
    events = ManzilEventAttendee.objects.filter(student=student)
    context = {
        'student': student,
        'sessions': sessions,
        'scholarships': scholarships,
        'events': events,
    }
    html_template = loader.get_template('student/student_detail.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def courses(request):
    courses = Course.objects.all().annotate(student_count=Count('studentcourse'))
    context = {'courses': courses}

    html_template = loader.get_template('student/courses.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def course_detail(request, course_id):
    course = Course.objects.get(pk=course_id)
    students = StudentCourse.objects.filter(course=course).select_related('student')
    context = {'course': course, 'students': students}
    html_template = loader.get_template('student/course_detail.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def sessions(request):
    sessions = Session.objects.all().annotate(student_count=Count('sessionenrollment'))
    context = {'sessions': sessions}

    html_template = loader.get_template('student/sessions.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def session_detail(request, session_id):
    session = Session.objects.get(id=session_id)
    students = SessionEnrollment.objects.filter(session=session).select_related('student')
    context = {'session': session, 'students': students}
    html_template = loader.get_template('student/session_detail.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def scholarships(request):
    scholarships = Scholarship.objects.all().annotate(student_count=Count('scholarshipenrollment'))
    context = {'scholarships': scholarships}

    html_template = loader.get_template('student/scholarships.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def events(request):
    events = ManzilEvent.objects.all().annotate(student_count=Count('manzileventattendee'))
    context = {'events': events}

    html_template = loader.get_template('student/events.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
