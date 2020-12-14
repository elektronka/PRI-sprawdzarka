from rest_framework import viewsets
from rest_framework import permissions
from django.shortcuts import render, redirect
from upload import models
from .forms import SendedTasksForm
from .forms import TasksListForm
from .models import SendedTasks
from .models import TaskList
from api import serializers
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from .antyplagiat import *
from .xml_metric import xmlmetricf
from .Antyplagiat_Extended import *

class StudentViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = serializers.StudentSerializer

@staff_member_required(login_url='login')
def task_sended_list(request):
    sended=SendedTasks.objects.all()
    return render(request,'upload/task_sended_list.html',{'sended': sended})

@login_required
def task_sended_upload(request):
    if request.method=='POST':
        form = SendedTasksForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form=SendedTasksForm()
    return render(request,'upload/task_sended_upload.html', {'form': form})

@login_required
def read_file1(request, file_to_open):
    f = open(r'task/sendedtasks/'+file_to_open, encoding="utf-8")
    result = []
    for line in f:
        result.append(line)
    f.close()
    return render(request,'upload/wyswietlanie.html',{'result': result},)

def task_list(request):
    sended=TaskList.objects.all
    return render(request,'upload/task_List.html',{'sended': sended})

@staff_member_required(login_url='login')
def task_List_upload(request):
    if request.method=='POST':
        form = TasksListForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form=TasksListForm()
    return render(request,'upload/task_sended_upload.html', {'form': form})

@login_required
def read_file2(request, file_to_open):
    f = open(r'task/tasklist/'+file_to_open, encoding="utf-8")
    result = []
    for line in f:
        result.append(line)
    f.close()
    return render(request,'upload/wyswietlanie.html',{'result': result})

"""
@staff_member_required(login_url='login')
def plagiat(request):
    result_list = []
    file_content=""
    Lista=[]
    for file in SendedTasks.objects.all():
        Lista.append(file)
    dlug=len(Lista)
    for i in range(dlug):
        for j in range (i+1,dlug,1):
            file_content = ""
            plagiarism = ProgramFile("Bartłomiej Nowak", "434162", "15")
            file1, file2 = plagiarism.get_file(Lista[i].task.name, Lista[j].task.name)
            name_surname1, nr_index1, count_pkt1 = plagiarism.ReadReport(file1)
            name_surname2, nr_index2, count_pkt2 = plagiarism.ReadReport(file2)
            first_list, second_list = plagiarism.get_words(file1, file2)
            text_list1, text_list2 = plagiarism.get_textlist(first_list, second_list)
            if len(text_list1) != 0 and len(text_list2) != 0:
                to_check, count_of_the_same_or_similar = plagiarism.check_words(text_list1, text_list2)
                if len(text_list1) >= len(text_list2):
                    for checked in to_check:
                        result = plagiarism.check_the_similar_words(checked, text_list1)
                        count_of_the_same_or_similar += result
                    total = len(text_list1)
                    plagiarism_coefficient = round(count_of_the_same_or_similar * 100 / total, 2)
                else:
                    for checked in to_check:
                        result = plagiarism.check_the_similar_words(checked, text_list2)
                        count_of_the_same_or_similar += result
                    total = len(text_list2)
                    plagiarism_coefficient = round(count_of_the_same_or_similar * 100 / total, 2)
                if plagiarism_coefficient >= 30:
                    file_content += str(name_surname1)+ " " +str(nr_index1) + " całkowita ilość punktów "+ str(count_pkt1) +" "+str(xmlmetricf(Lista[i].task.name))+  " | "  +str(name_surname2) + " całkowita ilość punktów "+ str(count_pkt2) +" "+ str(nr_index2) + " "+str(xmlmetricf(Lista[j].task.name)) +" | " +"Procent podobieństwa " + str(plagiarism_coefficient)
                else:
                    file_content += str(name_surname1)+ " " +str(nr_index1) + " całkowita ilość punktów "+ str(count_pkt1) +" "+str(xmlmetricf(Lista[i].task.name))+  " | "  +str(name_surname2) + " całkowita ilość punktów "+ str(count_pkt2) +" "+ str(nr_index2) + " "+str(xmlmetricf(Lista[j].task.name)) +" | "
                    file_content +="Oba teksty mają "+ str(plagiarism_coefficient) + " procent podobnych słów. "
                    file_content +="Prace są różne! Nie stwierdzam plagiatu!!"
            else:
                file_content +="Nie można sprawdzić plagiatu dla pustych plików"
            result_list.append(file_content)
    return render(request,'upload/plagiat.html', {'result_list': result_list})
"""

@staff_member_required(login_url='login')
def plagiat(request):
    result_list = []
    file_content = ""
    Lista = []
    for file in SendedTasks.objects.all():
        Lista.append(file)
    temp = []
    for i in range(len(Lista)):
        temp.append(Lista[i].task.name)
    files_and_enlargement = get_file(temp)
    for first_file in files_and_enlargement:
        for second_file in files_and_enlargement:
            if first_file != second_file:
                file_content += '\n'
                file_content += "Sprawdzam " + str(first_file) + " i " + str(second_file)
                file_content += '\n'
                if files_and_enlargement[first_file] == '.txt' and files_and_enlargement[second_file] == '.txt':
                    file1 = open(first_file, 'r', encoding="utf-8")
                    file2 = open(second_file, 'r', encoding="utf-8")
                    sprawozdanie = ReportFile()
                    name1, index1, punct1 = sprawozdanie.ReadReport(file1)
                    name2, index2, punct2 = sprawozdanie.ReadReport(file2)
                    words1, words2 = sprawozdanie.get_words(file1, file2)
                    text_list1, text_list2 = sprawozdanie.get_textlist(words1, words2)
                    if len(text_list1) > 0 and len(text_list2) > 0:
                        to_check, count_of_the_same_or_similar = sprawozdanie.check_words(text_list1, text_list2)
                        if len(text_list1) >= len(text_list2):
                            for checked in to_check:
                                result = sprawozdanie.check_the_similar_words(checked, text_list1)
                                count_of_the_same_or_similar += result
                            total = len(text_list1)
                            plagiarism_coefficient = round(count_of_the_same_or_similar * 100 / total, 2)
                        else:
                            for checked in to_check:
                                result = sprawozdanie.check_the_similar_words(checked, text_list2)
                                count_of_the_same_or_similar += result
                            total = len(text_list2)
                            plagiarism_coefficient = round(count_of_the_same_or_similar * 100 / total, 2)
                        if plagiarism_coefficient >= 30:
                            file_content += "Współczynnik podobieństwa tych plików to: " + str(plagiarism_coefficient) + "%"
                            file_content += '\n'
                            file_content += "PLAGIAT!!"
                            file_content += '\n'
                            file_content += "Autorzy podobnych prac:"
                            file_content += '\n'
                            file_content += str(name1) + " o numerze indeksu " + str(index1)
                            file_content += '\n'
                            file_content += str(name2) + " o numerze indeksu " + str(index2) + "|"
                            file_content += '\n'
                            file_content += '\n'
                        else:
                            file_content += "Współczynnik podobieństwa to: " + str(plagiarism_coefficient) + "%"
                            file_content += '\n'
                            file_content += "NIE MA PLAGIATU!!" + "|"
                            file_content += '\n'
                            file_content += '\n'
                        result_list.append(file_content)
                    else:
                        file_content += "Nie mogę sprawdzić podobieństwa dla pustych plików lub plików z niepoprawną strukturą" + "|"
                        file_content += '\n'
                        file_content += '\n'
                        result_list.append(file_content)

                elif files_and_enlargement[first_file] == '.pml' and files_and_enlargement[second_file] == '.pml':
                    file1 = open(first_file, 'r', encoding="utf-8")
                    file2 = open(second_file, 'r', encoding="utf-8")
                    similars = []
                    txt = ""
                    q = 101  # Liczba pierwsza
                    promela = PromelaFile()
                    words1, words2 = promela.get_words(file1, file2)
                    if len(words1) > 0 and len(words2) > 0:
                        if len(words1) >= len(words2):
                            txt = " ".join([str(i) for i in words1])
                            for word in words2:
                                indexes = []
                                indexes = promela.Rabin_Karp_algorithm(word, txt, q)
                                if len(indexes) > 0:
                                    if word not in similars:
                                        similars.append(word)
                                    else:
                                        continue
                            total = len(words1)
                            count_of_the_same_or_similar = len(similars)
                            plagiarism_coefficient = round(count_of_the_same_or_similar * 100 / total, 2)
                            if plagiarism_coefficient >= 30:
                                file_content += "Współczynnik podobieństwa tych programów to: " + str(plagiarism_coefficient) + "%"
                                file_content += '\n'
                                file_content += "PLAGIAT!!!" + "|"
                                file_content += '\n'
                                file_content += '\n'
                            else:
                                file_content += "Współczynnik podobieństwa to: " + str(plagiarism_coefficient) + "%"
                                file_content += '\n'
                                file_content += "NIE MA PLAGIATU!!" + "|"
                                file_content += '\n'
                                file_content += '\n'
                            result_list.append(file_content)
                        else:
                            txt = " ".join([str(i) for i in words2])
                            for word in words1:
                                indexes = []
                                indexes = promela.Rabin_Karp_algorithm(word, txt, q)
                                if len(indexes) > 0:
                                    if word not in similars:
                                        similars.append(word)
                                    else:
                                        continue
                            total = len(words2)
                            count_of_the_same_or_similar = len(similars)
                            plagiarism_coefficient = round(count_of_the_same_or_similar * 100 / total, 2)
                            if plagiarism_coefficient >= 30:
                                file_content += "Współczynnik podobieństwa tych programów to: " + str(plagiarism_coefficient) + "%"
                                file_content += '\n'
                                file_content += "PLAGIAT!!!" + "|"
                                file_content += '\n'
                                file_content += '\n'
                            else:
                                file_content += "Współczynnik podobieństwa to: " + str(plagiarism_coefficient) + "%"
                                file_content += '\n'
                                file_content += "NIE MA PLAGIATU!!" + "|"
                                file_content += '\n'
                                file_content += '\n'
                            result_list.append(file_content)
                    else:
                        file_content += "Nie mogę sprawdzić podobieństwa plików bez kodu źródłowego programu" + "|"
                        file_content += '\n'
                        result_list.append(file_content)

                else:
                    file_content += "Dwa pliki muszą być tego samego rozszerzenia!!!" + "|"
                    file_content += '\n'
                    result_list.append(file_content)
            else:
                continue
            result_list.append(file_content)
    return render(request, 'upload/plagiat.html', {'result_list': result_list})

