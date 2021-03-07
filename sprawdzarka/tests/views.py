from django.db.models.expressions import SQLiteNumericMixin
from django.shortcuts import redirect, render
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.utils import timezone
import codecs
from django.contrib import messages

def check_metric(file):
    test = []
    for line in file:
        sline = str(line.decode("utf-8"))
        test.append(sline)
        print(sline)
        if not ((sline.startswith('<pytanie>') and sline.endswith('</pytanie>\r\n')) or (sline.startswith('<odp>') and sline.endswith('</odp>\r\n')) or (sline.startswith('<odp>') and sline.endswith('</odp>'))):
            print(test)
            return False
    return True

def question(text):
    if text.startswith('<pytanie>') and text.endswith('</pytanie>'):
        return True
    else:
        return False

def answer(text):
    if text.startswith('<odp>') and text.endswith('</odp>'):
        return True
    else:
        return False

def load_data_from_txt(path):
    file = open('task/tests/'+path, 'r', encoding='utf-8')
    lines = file.read().splitlines()
    questions = []
    answers = []
    question_id = 0
    letter = 65
    print(lines)
    for line in lines:
        if question(line):
            question_id += 1
            letter = 65
            line = line.replace('<pytanie>','')
            line = line.replace('</pytanie>','')
            questions.append([question_id,line])
        elif answer(line):
            line = line.replace('<odp>','')
            line = line.replace('</odp>','')
            if '<poprawna>' in line:
                line = line.replace('<poprawna>','')
                answers.append([question_id,line,chr(letter),True])
            else:
                answers.append([question_id,line,chr(letter),False])
            letter += 1
    return (questions,answers)

@login_required
def tests_home(request):
    return render(request, 'tests/home.html')

@login_required
def all_tests(request):
    if request.user.is_staff:
        all = TestFileModel.objects.all()
    else:
        all = TestFileModel.objects.filter(group_id = request.user.group_id)
    return render(request, 'tests/all.html', {'all': all})

@staff_member_required
def new_test(request):
    if request.method=='POST':
        form = TestFileForm(request.POST, request.FILES)
        if form.is_valid():
            test_file = form.save(commit=False)
            path = str(test_file.file)
            if check_metric(codecs.EncodedFile(request.FILES['file'],"utf-8")):
                form.save()
                questions, answers = load_data_from_txt(path)
                id = TestFileModel.objects.get(name = test_file.name)
                for line in questions:
                    new_question = TestQuestionModel()
                    new_question.test_id = int(id.id)
                    new_question.question_id = line[0]
                    new_question.content = line[1]
                    new_question.save()
                for line in answers:
                    new_answer = QuestionAnswerModel()
                    new_answer.test_id = int(id.id)
                    new_answer.question_id = line[0]
                    new_answer.content = line[1]
                    new_answer.letter = line[2]
                    new_answer.is_right = line[3]
                    new_answer.save()
                messages.success(request,'Dodano nowy test.')
                return redirect('tests_home')
            else:
                messages.warning(request,'Niepoprawna metryczka.')
    else:
        form = TestFileForm()
    return render(request, 'tests/new_test.html', {'form':form})
@login_required
def test(request, test_id, question_id):
    this_test = TestFileModel.objects.get(id = test_id)
    date_start = this_test.date_start
    date_end = this_test.date_end
    all_ids = TestQuestionModel.objects.filter(test_id = test_id)
    now = timezone.now()
    color = ''
    if now >= date_start and now <= date_end:
        if StudentPointsTest.objects.filter(test_id = test_id, snumber = request.user.snumber).exists():
            return render(request, 'tests/denied.html')
        else:
            question = TestQuestionModel.objects.get(test_id = test_id, question_id = question_id)
            if request.method == "POST":
                form = TestViewForm(request.POST, test_id = test_id, question_id = question_id, user = request.user.snumber)
                if form.is_valid():
                    obj = form.save(commit = False)
                    if StudentAnswerModel.objects.filter(test_id = test_id,question_id = question_id, snumber = request.user.snumber).exists():
                        StudentAnswerModel.objects.filter(test_id = test_id,question_id = question_id, snumber = request.user.snumber).update(answer = obj.answer)
                        
                    else:
                        
                        obj.snumber = request.user.snumber
                        obj.test_id = test_id
                        obj.question_id = question_id
                        obj.save()
                    if timezone.now() >= date_start and timezone.now() <= date_end:
                        if TestQuestionModel.objects.filter(test_id = test_id, question_id = question_id+1).exists():
                            return redirect('/tests/'+str(test_id)+'/'+str(question_id+1))
                        else:
                            '''
                            points = 0
                            student_answers = StudentAnswerModel.objects.filter(test_id = test_id)
                            correct_answers = QuestionAnswerModel.objects.filter(test_id = test_id, is_right = True)
                            for student, correct in zip(student_answers,correct_answers):
                                if student.answer == correct.letter:
                                    points += 1
                                    StudentAnswerModel.objects.filter(id = student.id).update(is_right = True)
                
                            end_result = StudentPointsTest()
                            end_result.snumber = request.user.snumber
                            end_result.points = points
                            end_result.test_id = test_id
                            end_result.save()
                            '''
        
                            return redirect('/tests/confirm/'+str(test_id))
                    else:
                        return redirect('/tests/end/'+str(test_id))
            else:
                if StudentAnswerModel.objects.filter(test_id = test_id,question_id = question_id, snumber = request.user.snumber).exists():
                    #color = 'LimeGreen'
                    a = StudentAnswerModel.objects.get(test_id = test_id,question_id = question_id, snumber = request.user.snumber)
                    form = TestViewForm(test_id = test_id, question_id = question_id, user = request.user.snumber, instance = a)
                else:
                    #color = 'LightSteelBlue'
                    form = TestViewForm(test_id = test_id, question_id = question_id, user = request.user.snumber)
    else:
        return render(request, 'tests/denied.html')

    return render(request,'tests/test.html', {'form':form, 'question':question, 'all_ids':all_ids, 'test_id':test_id, 'color':color})

@login_required
def confirm_test(request, test_id):
    if not StudentPointsTest.objects.filter(test_id = test_id, snumber = request.user.snumber).exists():
        all_ids = TestQuestionModel.objects.filter(test_id = test_id)
        answers = StudentAnswerModel.objects.filter(test_id = test_id, snumber = request.user.snumber)
    else:
        return render(request, 'tests/denied.html')
    return render(request, 'tests/confirm.html', {'answers':answers,'test_id':test_id, 'all_ids':all_ids})

@login_required
def end_test(request, test_id):
    if not StudentPointsTest.objects.filter(test_id = test_id, snumber = request.user.snumber).exists():
        points = 0
        student_answers = StudentAnswerModel.objects.filter(test_id = test_id, snumber = request.user.snumber)
        correct_answers = QuestionAnswerModel.objects.filter(test_id = test_id, is_right = True)
        for student, correct in zip(student_answers,correct_answers):
            if student.answer == correct.letter:
                points += 1
                StudentAnswerModel.objects.filter(id = student.id).update(is_right = True)
                
        end_result = StudentPointsTest()
        end_result.snumber = request.user.snumber
        end_result.points = points
        end_result.test_id = test_id
        end_result.save()
        result = StudentPointsTest.objects.get(test_id = test_id, snumber = request.user.snumber)
        print(Account.objects.get(snumber = request.user.snumber).points)
        user_points = Account.objects.get(snumber = request.user.snumber).points + points
        Account.objects.filter(snumber = request.user.snumber).update(points = user_points)
    else:
        return render(request, 'tests/denied.html')
    return render(request, 'tests/end.html', {'result':result})