from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from .forms import *
from .promeli_filechcker import *
from django.contrib import messages
import os, re

def filename(value):
    return os.path.basename(value.file.name)

@staff_member_required(login_url='login')
def change_points_promela_direct(request,id_in_url):
    object=StudentTask.objects.get(id=id_in_url)
    snumber_in_url=object.snumber
    task_id_in_url=object.task_id
    old_points=object.points
    if request.method=='POST':
        form = TransformersForm(request.POST)
        if form.is_valid():
            object=StudentTask.objects.get(id=id_in_url)
            object.points=form.cleaned_data['NewPoints']
            object.save()
            messages.success(request, 'Pomyślnie zmieniono punkty.')
            return redirect('promela-sended-list' )
    else:
        form=TransformersForm()
    return render(request,'upload/transformers.html', {'form': form,'snumber':snumber_in_url,'zadanie':task_id_in_url, 'old_points':old_points})

@staff_member_required(login_url='login')
def task_promela_upload_teacher(request):
    if request.method=='POST':
        form = TeacherTaskForm(request.POST, request.FILES)
        if form.is_valid():
            mo = re.compile(r'^[\w_\s]*$')
            check_name = form.cleaned_data['task_name']
            res = re.findall(mo, check_name)
            if not res:
                messages.warning(request, "Niepoprawna nazwa zadania.")
            else:
                form.save(commit=False)
                form.tname = request.user.username
                form.save()
                messages.success(request, 'Pomyślnie dodano zadanie.')
    else:
        form=TeacherTaskForm()
    return render(request,'Promela/task_promela_upload.html', {'form': form})


@login_required
def task_promela_upload(request):
    if request.method=='POST':
        form = StudentTaskForm(request.POST, request.FILES)
        if form.is_valid():
            object = form.save(commit=False)
            if StudentTask.objects.filter(snumber = request.user.snumber, task_id = object.task_id).exists():
                messages.warning(request,"Nie można dodać 2 razy tego samego zadania.")
            elif TeacherTask.objects.get(id = object.task_id.id).date_end < timezone.now():
                messages.warning(request,"Nie można oddać zadania po czasie.")
            else:
                object.snumber = request.user.snumber
                object.group_id = request.user.group_id               
                object.save()
                messages.success(request, 'Pomyślnie oddano zadanie.')
    else:
        form= StudentTaskForm()
    return render(request, 'upload/task_sended_upload.html', {'form': form})

@staff_member_required(login_url='login')
def task_Promela_student_sended_list(request):
    promela_funck()
    sended=StudentTask.objects.all()
    for task in sended:
        task.task_file.name = (os.path.basename(task.task_file.name))
        task.output_file.name = (os.path.basename(task.output_file.name))
    return render(request,'Promela/task_Promela_sended_list.html',{'sended': sended})

@login_required
def task_list_promela(request):
    sended=TeacherTask.objects.all()
    for task in sended:
        task.file.name = (os.path.basename(task.file.name))
    return render(request,'Promela/task_List_promela.html',{'sended': sended})

@login_required
def read_file_promela__task_list(request, file_to_open):
    f = open(r'task/promela/teacher_ltl/'+file_to_open, encoding="utf-8")
    result = []
    for line in f:
        result.append(line)
    f.close()
    return render(request,'upload/wyswietlanie.html',{'result': result},)


@login_required
def read_file_Promela_task_student(request, file_to_open):
    f = open(r'task/promela/student_files/'+file_to_open, encoding="utf-8")
    result = []
    for line in f:
        result.append(line)
    f.close()
    return render(request,'upload/wyswietlanie.html',{'result': result},)