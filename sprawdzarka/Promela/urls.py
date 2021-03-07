from Promela import views
from django.urls import path
from rest_framework import routers

urlpatterns = [
    path('uploadpromela/',views.task_promela_upload, name='uploadPromela'),
    path('tasklistpromela/', views.task_list_promela, name='task-list-promela'),
    path('PromelaList/', views.task_Promela_student_sended_list, name='promela-sended-list'),
    path('PromelaList/changepoints/<int:id_in_url>/',views.change_points_promela_direct, name='change-points-promela-direct'),
    path('PromelaList/<str:file_to_open>', views.read_file_Promela_task_student, name='promela-sended-task'),
    path('taskpromelaupload/',views.task_promela_upload_teacher, name='task-upload-promela'),
    path('Promela/Studentstask/<str:file_to_open>',views.read_file_Promela_task_student, name='sended-promela-output'),
    path('tasklistpromela/<str:file_to_open>',views.read_file_promela__task_list, name ='ltl-open'),
    path('PromelaList/changepoints/<int:id_in_url>/',views.change_points_promela_direct, name='change-points-promela'),
]