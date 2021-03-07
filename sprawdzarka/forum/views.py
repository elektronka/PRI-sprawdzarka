from django.contrib.admin.views.decorators import staff_member_required
from django.db.models.fields import BLANK_CHOICE_DASH
from django.shortcuts import render, redirect
from .models import *
from upload.models import *
from django.contrib.auth.decorators import login_required
from .forms import *

@login_required
def all(request, choose):
    if choose == 'xml':
        all_questions = QuestionXml.objects.all()
    else:
        all_questions = QuestionPromela.objects.all()
    return render(request, 'forum/all_questions.html', {'all':all_questions,'choose':choose})

@staff_member_required
def new(request, choose):
    if choose == 'xml':
        all_questions = QuestionXml.objects.filter(has_teacher_answer = False)
    else:
        all_questions = QuestionPromela.objects.filter(has_teacher_answer = False)
    return render(request, 'forum/new_questions.html', {'all':all_questions,'choose':choose})


@login_required
def choose(request):
    return render(request, 'forum/choose.html')

@login_required
def question(request,choose,id):
    if choose == 'xml':
        this_question = QuestionXml.objects.get(id = id)
    else:
        this_question = QuestionPromela.objects.get(id = id)
    no_answer = ''
    teacher_answers = []
    answers = []
    check = False
    if Answer.objects.filter(question_id = id, section = choose).exists():
        answers = Answer.objects.filter(question_id = id, section = choose, has_teacher_answered = False)
        if Answer.objects.filter(question_id = id, section = choose, has_teacher_answered = True).exists():
            teacher_answers = Answer.objects.filter(question_id = id, section = choose, has_teacher_answered = True)
            check = True
    else:
        no_answer = "Nie ma jeszcze odpowiedzi do tego pytania"

    return render(request, 'forum/question.html', {'this_question': this_question,'answers': answers,'no_answer':no_answer, 'teacher_answers': teacher_answers, 'check':check, 'choose':choose})

@login_required
def home(request, choose):
    return render(request, 'forum/home.html', {'choose':choose}) 

@login_required
def question_fake(request,choose):
    if choose == 'xml':
        if request.method == "POST":
            form = AddQuestionXmlForm(request.POST)
            object = form.save(commit = False)
            object.asking_student=request.user.username
            object.save()
            return redirect('/forum/all/xml')
        else:
            form = AddQuestionXmlForm()
    else:
        if request.method == "POST":
            form = AddQuestionPromelaForm(request.POST)
            object = form.save(commit = False)
            object.asking_student=request.user.username
            object.save()
            return redirect('/forum/all/promela')
        else:
            form = AddQuestionPromelaForm()
            
    return render(request, 'forum/add_question_fake.html', {'form': form})

@login_required
def add_question(request,choose,id):
    if choose == 'xml':
        if request.method == "POST":
            form = AddQuestionXmlFormNew(request.POST)
            if form.is_valid():
                object = form.save(commit=False)
                object.task_id=TaskList.objects.get(id = id)
                object.asking_student=request.user.username
                object.save()
                return redirect('/forum/all/')
        else:
            form=AddQuestionXmlFormNew()
    else:
        if request.method == "POST":
            form = AddQuestionPromelaFormNew(request.POST)
            if form.is_valid():
                object = form.save(commit=False)
                object.task_id=TeacherTask.objects.get(id = id)
                object.asking_student=request.user.username
                object.save()
                return redirect('/forum/all/')
        else:
            form=AddQuestionPromelaFormNew()
    return render(request, 'forum/questionForm.html', {'form': form})

@login_required
def add_answer(request, choose, id):
    if request.method == "POST":
        form = AddAnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.who_answered = request.user.username
            answer.section = choose
            answer.question_id = id
            if request.user.group_id == '0':
                if choose == 'xml':
                    QuestionXml.objects.filter(id = id).update(has_teacher_answer = True)
                else:
                    QuestionPromela.objects.filter(id = id).update(has_teacher_answer = True)
                answer.has_teacher_answered = True
            answer.save()
            return redirect('/forum/all/'+choose)
    else:
        form=AddAnswerForm()         
    return render(request, 'forum/add_answer_form.html',{'form': form}) 



