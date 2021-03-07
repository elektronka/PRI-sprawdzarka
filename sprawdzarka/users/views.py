from tests.models import StudentAnswerModel, StudentPointsTest
from Promela.models import StudentTask
from upload.models import Plagiat, SendedTasks, StudentsPoints
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import *
from .models import *
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
import re

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            mo = re.compile(r'^[0-9]{6}$')
            check_snumber = form.cleaned_data['snumber']
            res = re.findall(mo, check_snumber)
            if not res:
                messages.warning(request, "Niepoprawny format numeru indeksu.")
            else:
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Konto stworzone dla {username}!')
                return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if not request.user.is_staff:
        group = Group.objects.get(id = request.user.group_id)
    else:
        group = ''
    students = Account.objects.filter(group_id = request.user.group_id)
    result = []
    student_points = 0
    for student in students:
        all_points_xml = StudentsPoints.objects.filter(snumber = student.snumber)
        all_points_promela = StudentTask.objects.filter(snumber = student.snumber) 
        for i in all_points_xml:
            student_points += i.points
        for i in all_points_promela:
            student_points += i.points
        student_points+=student.points
        result.append([student.snumber,student_points])
    return render(request, 'users/profile.html', {'group':group, 'student_points':student_points})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Pomyślnie zmieniono hasło!')
            return redirect('profile')
            
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/changepasswd.html', {'form':form})

@staff_member_required
def active_groups(request):
    all = Group.objects.filter(is_active = True)
    return render(request, 'users/groups.html', {'all': all})

@staff_member_required
def all_groups(request):
    all = Group.objects.all()
    return render(request, 'users/groups.html', {'all': all})

@staff_member_required
def groups_choose(request):
    return render(request, 'users/groups_choose.html')

@staff_member_required(login_url='login')
def new_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            mo = re.compile(r'^[\w_\s]*$')
            check_name = form.cleaned_data['name']
            res = re.findall(mo, check_name)
            if not res:
                messages.warning(request, "Niepoprawna nazwa grupy.")
            else:
                mo_n = re.compile(r'^[0-9]{4}\/[0-9]{4}$')
                check_year = form.cleaned_data['year']
                res_n = re.findall(mo_n, check_year)
                if not res_n:
                    messages.warning(request, "Niepoprawny format daty.")
                else:
                    group = Group()
                    group.name = form.data['name']
                    group.year = form.data['year']
                    group.term = form.data['term']
                    group.save()
                    return redirect('all_groups')
    else:
        form = GroupForm()
    return render(request, 'users/new_group.html', {'form': form})

@login_required
def all_students(request, group_id):
    students = Account.objects.filter(group_id = group_id)
    result = []
    for student in students:
        all_points_xml = StudentsPoints.objects.filter(snumber = student.snumber)
        all_points_promela = StudentTask.objects.filter(snumber = student.snumber)
        student_points = 0
        for i in all_points_xml:
            student_points += i.points
        for i in all_points_promela:
            student_points += i.points
        student_points+=student.points

        result.append({'student':student.snumber,'points':student_points})

    return render(request, 'users/group.html', {'result':result})

def delete_group(request, group_id):
    if request.method == "POST":
        form = DeleteGroup(request.POST)
        if form.is_valid:
            Group.objects.filter(id = group_id).update(is_active=False)
            return redirect('active_groups')
    else:
        form = DeleteGroup()

    return render(request, 'users/delete.html')

    
def change_group(request, snumber):
    if request.method == "POST":
        form = ChangeGroup(request.POST)
        if form.is_valid:
            group_id = form.data['group_id']
            StudentsPoints.objects.filter(snumber = snumber).delete()
            StudentTask.objects.filter(snumber = snumber).delete()
            StudentAnswerModel.objects.filter(snumber = snumber).delete()
            StudentPointsTest.objects.filter(snumber = snumber).delete()
            Plagiat.objects.filter(snumber1 = snumber).delete()
            SendedTasks.objects.filter(snumber = snumber).delete()
            Account.objects.filter(snumber=snumber).update(group_id = group_id)
            Account.objects.filter(snumber=snumber).update(points = 0)
            return redirect('groups_choose')
    else:
        form = ChangeGroup()

    return render(request, 'users/change_group.html',{'form':form})